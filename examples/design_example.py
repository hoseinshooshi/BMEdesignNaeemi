import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from bmedesign.anthropometry import AnthropometricInput
from bmedesign.orthosis import build_orthosis
from bmedesign.metrics import estimate_metrics
from bmedesign.visualization import plot_mesh
from bmedesign.ml import train_wrist_model, predict_wrist_circumference


def main():
    # Measurements remain defined here. ML estimates the missing wrist size.
    base = {
        "hand_length_mm": 185,
        "hand_breadth_mm": 82,
        "forearm_length_mm": 245,
        "forearm_circumference_mm": 230,
    }

    project_root = Path(__file__).resolve().parents[1]
    model = train_wrist_model(project_root / "data")
    estimated_wrist_mm = predict_wrist_circumference(
        model,
        hand_length_mm=base["hand_length_mm"],
        hand_breadth_mm=base["hand_breadth_mm"],
        forearm_circumference_mm=base["forearm_circumference_mm"],
    )
    measurements = AnthropometricInput(
        **base, wrist_circumference_mm=estimated_wrist_mm
    )

    mesh = build_orthosis(measurements, pattern="solid", thickness_mm=3.0)
    metrics = estimate_metrics(mesh)
    output_dir = project_root / "output"
    output_dir.mkdir(exist_ok=True)
    mesh.export(output_dir / "wrist_hand_orthosis.stl")

    print("=== BMEdesignNaeemi: ML-assisted wrist orthosis ===")
    print(f"Training population: {model.training_population}")
    print(f"Training samples: {int(model.metrics['n_samples'])}")
    print(f"Holdout MAE: {model.metrics['mae_mm']:.2f} mm")
    print(f"Holdout RMSE: {model.metrics['rmse_mm']:.2f} mm")
    print(f"Holdout R2: {model.metrics['r2']:.3f}")
    print(f"ML-estimated wrist circumference: {estimated_wrist_mm:.2f} mm")
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")
    print(f"STL: {output_dir / 'wrist_hand_orthosis.stl'}")

    fig = plot_mesh(mesh)
    fig.savefig(output_dir / "wrist_hand_orthosis.png", dpi=180, bbox_inches="tight")


if __name__ == "__main__":
    main()
