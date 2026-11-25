"""ANSUR-II Random Forest model for estimating wrist circumference (mm)."""
from dataclasses import dataclass
from pathlib import Path
import re
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

FEATURES = ["handlength", "handbreadth", "forearmcircumferenceflexed"]
TARGET = "wristcircumference"

@dataclass
class ANSURModel:
    model: RandomForestRegressor
    feature_names: list[str]
    target_name: str
    metrics: dict[str, float]
    training_population: str

def _normalize_column(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(name).strip().lower())

def load_ansur_csv(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists() or path.stat().st_size == 0:
        raise ValueError(f"ANSUR II data file is missing or empty: {path}")
    try:
        df = pd.read_csv(path, encoding="utf-8-sig")
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding="cp1252")
    df.columns = [_normalize_column(c) for c in df.columns]
    return df

def prepare_ansur(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    missing = [c for c in FEATURES + [TARGET] if c not in df.columns]
    if missing:
        raise ValueError(f"Missing ANSUR II columns: {missing}")
    work = df[FEATURES + [TARGET]].apply(pd.to_numeric, errors="coerce")
    work = work.replace([np.inf, -np.inf], np.nan).dropna()
    work = work[(work[FEATURES + [TARGET]] > 0).all(axis=1)]
    if len(work) < 50:
        raise ValueError(f"Not enough valid ANSUR II records: {len(work)}")
    return work[FEATURES], work[TARGET]

def train_wrist_model(data_dir: str | Path, test_size: float = 0.20,
                      random_state: int = 42) -> ANSURModel:
    """Train from every valid ANSUR II sex-specific CSV present in data_dir."""
    data_dir = Path(data_dir)
    frames, populations = [], []
    for sex, filename in (("female", "ANSUR II FEMALE Public.csv"),
                          ("male", "ANSUR II MALE Public.csv")):
        try:
            X_part, y_part = prepare_ansur(load_ansur_csv(data_dir / filename))
        except (ValueError, pd.errors.EmptyDataError, FileNotFoundError):
            continue
        frames.append(pd.concat([X_part, y_part.rename(TARGET)], axis=1))
        populations.append(sex)
    if not frames:
        raise FileNotFoundError(f"No valid ANSUR II CSV files found in {data_dir}")
    data = pd.concat(frames, ignore_index=True).drop_duplicates()
    X, y = data[FEATURES], data[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state)
    model = RandomForestRegressor(n_estimators=500, min_samples_leaf=3,
                                  max_features=1.0, random_state=random_state,
                                  n_jobs=-1)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    metrics = {
        "mae_mm": float(mean_absolute_error(y_test, pred)),
        "rmse_mm": float(np.sqrt(mean_squared_error(y_test, pred))),
        "r2": float(r2_score(y_test, pred)),
        "n_samples": float(len(data)),
        "n_test": float(len(X_test)),
    }
    return ANSURModel(model, FEATURES.copy(), TARGET, metrics, "+".join(populations))

def predict_wrist_circumference(model: ANSURModel, hand_length_mm: float,
                                hand_breadth_mm: float,
                                forearm_circumference_mm: float) -> float:
    values = [hand_length_mm, hand_breadth_mm, forearm_circumference_mm]
    if any(not np.isfinite(v) or v <= 0 for v in values):
        raise ValueError("ML input measurements must be finite and positive.")
    X = pd.DataFrame([values], columns=FEATURES)
    return float(model.model.predict(X)[0])
