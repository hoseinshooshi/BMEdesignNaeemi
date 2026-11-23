from bmedesign.anthropometry import AnthropometricInput
from bmedesign.orthosis import build_orthosis

def test_orthosis_has_geometry():
    m = AnthropometricInput(185, 82, 170, 245, 230)
    mesh = build_orthosis(m)
    assert len(mesh.vertices) > 0
    assert len(mesh.faces) > 0
