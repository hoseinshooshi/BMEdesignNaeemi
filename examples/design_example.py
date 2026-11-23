import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from bmedesign.anthropometry import AnthropometricInput
from bmedesign.orthosis import build_orthosis
from bmedesign.metrics import estimate_metrics
from bmedesign.visualization import plot_mesh

def main():
    measurements = AnthropometricInput(
        hand_length_mm=185,
        hand_breadth_mm=82,
        wrist_circumference_mm=170,
        forearm_length_mm=245,
        forearm_circumference_mm=230,
    )

    mesh = build_orthosis(measurements, pattern="solid", thickness_mm=3.0)
    metrics = estimate_metrics(mesh)

    os.makedirs("output", exist_ok=True)
    mesh.export("output/wrist_hand_orthosis.stl")

    print("=== BMEdesignNaeemi ===")
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")
    print("STL: output/wrist_hand_orthosis.stl")

    fig = plot_mesh(mesh)
    fig.savefig("output/wrist_hand_orthosis.png", dpi=180, bbox_inches="tight")

if __name__ == "__main__":
    main()
