"""Train and evaluate the ANSUR II wrist-circumference model."""

from pathlib import Path
import sys

# Make the src layout importable when this script is run directly.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from bmedesign.ml import train_wrist_model


def main() -> None:
    data_dir = PROJECT_ROOT / "data"
    result = train_wrist_model(data_dir)

    print("=== ANSUR II Wrist-Circumference Prediction ===")
    print(f"Training population: {result.training_population}")
    print(f"Valid samples:      {int(result.metrics['n_samples'])}")
    print(f"Test samples:       {int(result.metrics['n_test'])}")
    print(f"MAE:                {result.metrics['mae_mm']:.2f} mm")
    print(f"RMSE:               {result.metrics['rmse_mm']:.2f} mm")
    print(f"R²:                 {result.metrics['r2']:.4f}")


if __name__ == "__main__":
    main()
