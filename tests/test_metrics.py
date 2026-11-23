from bmedesign.anthropometry import AnthropometricInput
from bmedesign.orthosis import build_orthosis
from bmedesign.metrics import estimate_metrics

def test_metrics_are_positive():
    m = AnthropometricInput(185, 82, 170, 245, 230)
    metrics = estimate_metrics(build_orthosis(m))
    assert metrics["volume_mm3"] > 0
    assert metrics["surface_area_mm2"] > 0
