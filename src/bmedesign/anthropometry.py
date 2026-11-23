from dataclasses import dataclass

@dataclass(frozen=True)
class AnthropometricInput:
    hand_length_mm: float
    hand_breadth_mm: float
    wrist_circumference_mm: float
    forearm_length_mm: float
    forearm_circumference_mm: float

    def validate(self) -> None:
        values = {
            "hand_length_mm": self.hand_length_mm,
            "hand_breadth_mm": self.hand_breadth_mm,
            "wrist_circumference_mm": self.wrist_circumference_mm,
            "forearm_length_mm": self.forearm_length_mm,
            "forearm_circumference_mm": self.forearm_circumference_mm,
        }
        for name, value in values.items():
            if value <= 0:
                raise ValueError(f"{name} must be positive.")

    @property
    def wrist_radius_mm(self) -> float:
        return self.wrist_circumference_mm / (2.0 * 3.141592653589793)

    @property
    def forearm_radius_mm(self) -> float:
        return self.forearm_circumference_mm / (2.0 * 3.141592653589793)
