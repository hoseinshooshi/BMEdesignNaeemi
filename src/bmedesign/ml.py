import numpy as np
from sklearn.ensemble import RandomForestRegressor

def train_demo_model():
    """Train a clearly synthetic demonstration model.

    Replace X/y with validated anthropometric data for real research.
    """
    rng = np.random.default_rng(42)
    n = 400
    X = rng.normal(
        loc=[180, 85, 160],
        scale=[12, 6, 12],
        size=(n, 3),
    )
    y = 0.48 * X[:, 0] + 0.18 * X[:, 1] + 0.08 * X[:, 2] + rng.normal(0, 3, n)
    model = RandomForestRegressor(n_estimators=150, random_state=42)
    model.fit(X, y)
    return model

def predict_missing_dimension(model, hand_length, hand_breadth, forearm_length):
    x = np.array([[hand_length, hand_breadth, forearm_length]])
    return float(model.predict(x)[0])
