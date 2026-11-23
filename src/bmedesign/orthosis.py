from .anthropometry import AnthropometricInput
from .geometry import shell_mesh, add_ventilation_pattern

def build_orthosis(measurements: AnthropometricInput, pattern="solid",
                   thickness_mm=3.0):
    measurements.validate()

    # Educational scaling rule: distal support uses hand breadth,
    # proximal support follows forearm circumference.
    wrist_width = measurements.wrist_circumference_mm / 3.141592653589793
    forearm_width = measurements.forearm_circumference_mm / 3.141592653589793

    length = measurements.forearm_length_mm * 0.65 + measurements.hand_length_mm * 0.35
    wrist_depth = wrist_width * 0.82
    forearm_depth = forearm_width * 0.82

    mesh = shell_mesh(
        length_mm=length,
        wrist_width_mm=wrist_width,
        forearm_width_mm=forearm_width,
        wrist_depth_mm=wrist_depth,
        forearm_depth_mm=forearm_depth,
        thickness_mm=thickness_mm,
    )
    return add_ventilation_pattern(mesh, pattern=pattern)
