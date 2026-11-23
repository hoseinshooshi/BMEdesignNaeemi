from pathlib import Path
from dataclasses import dataclass
import re

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

FEATURES = [
    "handlength",
    "handbreadth",
    "radialestylionlength",
    "forearmcircumferenceflexed",
]
TARGET = "wristcircumference"

@dataclass
class ANSURModel:
    sex: str
    model: RandomForestRegressor
    feature_names: list[str]
    target_name: str
    metrics: dict[str, float]

def _normalize_column(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(name).strip().lower())

def load_ansur_csv(path: str | Path) -> pd.DataFrame:
    """Load one original ANSUR II public CSV and normalize column names."""
    df = pd.read_csv(path, encoding="cp1252")
    df.columns = [_normalize_column(c) for c in df.columns]
    return df

def prepare_ansur(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Select the hand/forearm measurements used for wrist-size prediction."""
    missing = [c for c in FEATURES + [TARGET] if c not in df.columns]
    if missing:
        raise ValueError(f"Missing ANSUR II columns: {missing}")
    work = df[FEATURES + [TARGET]].apply(pd.to_numeric, errors="coerce").dropna()
    return work[FEATURES], work[TARGET]

def train_ansur_model(csv_path: str | Path, sex: str, test_size: float = 0.20,
                      random_state: int = 42) -> ANSURModel:
    """Train a wrist-circumference regressor on real ANSUR II measurements."""
    df = load_ansur_csv(csv_path)
    X, y = prepare_ansur(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    model = RandomForestRegressor(
        n_estimators=300, random_state=random_state,
        min_samples_leaf=3, n_jobs=-1
    )
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    metrics = {
        "mae_mm": float(mean_absolute_error(y_test, pred)),
        "rmse_mm": float(np.sqrt(mean_squared_error(y_test, pred))),
        "r2": float(r2_score(y_test, pred)),
        "n_samples": float(len(X)),
    }
    return ANSURModel(sex, model, FEATURES, TARGET, metrics)

def predict_wrist_circumference(model: ANSURModel, hand_length_mm: float,
                                hand_breadth_mm: float, forearm_length_mm: float,
                                forearm_circumference_mm: float) -> float:
    """Predict wrist circumference in millimetres."""
    X = pd.DataFrame([[
        hand_length_mm, hand_breadth_mm,
        forearm_length_mm, forearm_circumference_mm
    ]], columns=FEATURES)
    return float(model.model.predict(X)[0])

def train_both_sexes(data_dir: str | Path) -> dict[str, ANSURModel]:
    """Train independent models for the male and female ANSUR II files."""
    data_dir = Path(data_dir)
    return {
        "male": train_ansur_model(data_dir / "ANSUR II MALE Public.csv", "male"),
        "female": train_ansur_model(data_dir / "ANSUR II FEMALE Public.csv", "female"),
    }
