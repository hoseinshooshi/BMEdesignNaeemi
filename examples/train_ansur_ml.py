import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from bmedesign.ml import train_both_sexes


def main():
    models = train_both_sexes("data")
    print("=== ANSUR II Wrist-Circumference Prediction ===")
    for sex, result in models.items():
        print(f"\n[{sex.upper()}]")
        print(f"Samples: {int(result.metrics['n_samples'])}")
        print(f"MAE:    {result.metrics['mae_mm']:.2f} mm")
        print(f"RMSE:   {result.metrics['rmse_mm']:.2f} mm")
        print(f"R²:     {result.metrics['r2']:.4f}")


if __name__ == "__main__":
    main()
