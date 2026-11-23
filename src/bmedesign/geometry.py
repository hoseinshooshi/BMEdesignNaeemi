import math
import numpy as np
import trimesh

def _ring(center_x, center_y, z, rx, ry, n=48):
    theta = np.linspace(0, 2 * math.pi, n, endpoint=False)
    return np.column_stack([
        center_x + rx * np.cos(theta),
        center_y + ry * np.sin(theta),
        np.full(n, z),
    ])

def shell_mesh(length_mm, wrist_width_mm, forearm_width_mm,
               wrist_depth_mm, forearm_depth_mm, thickness_mm=3.0,
               n=64, segments=24):
    """Create a tapered closed elliptical shell along the z axis."""
    outer = []
    inner = []
    for i in range(segments + 1):
        t = i / segments
        width = wrist_width_mm * (1-t) + forearm_width_mm * t
        depth = wrist_depth_mm * (1-t) + forearm_depth_mm * t
        z = t * length_mm
        outer.append(_ring(0, 0, z, width/2, depth/2, n))
        inner.append(_ring(0, 0, z, max(width/2-thickness_mm, 0.5),
                           max(depth/2-thickness_mm, 0.5), n))

    vertices = np.vstack(outer + inner)
    faces = []
    ring_count = segments + 1

    def idx(layer, i, j):
        return layer * ring_count * n + i * n + j

    for layer in (0, 1):
        for i in range(segments):
            for j in range(n):
                a, b = idx(layer, i, j), idx(layer, i, (j+1)%n)
                c, d = idx(layer, i+1, (j+1)%n), idx(layer, i+1, j)
                faces.extend([(a,b,c), (a,c,d)] if layer == 0 else [(a,c,b), (a,d,c)])

    # close distal/proximal annular rims
    for end in (0, segments):
        for j in range(n):
            a, b = idx(0,end,j), idx(0,end,(j+1)%n)
            c, d = idx(1,end,(j+1)%n), idx(1,end,j)
            faces.extend([(a,b,c), (a,c,d)])

    return trimesh.Trimesh(vertices=vertices, faces=np.asarray(faces), process=True)

def add_ventilation_pattern(mesh, pattern="perforated"):
    """Return a geometry-preserving demo mesh.

    Boolean hole cutting is intentionally avoided so the example remains
    portable across machines without external boolean engines.
    """
    return mesh
