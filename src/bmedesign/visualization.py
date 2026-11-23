import matplotlib.pyplot as plt

def plot_mesh(mesh, title="Parametric wrist-hand orthosis"):
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_trisurf(
        mesh.vertices[:, 0], mesh.vertices[:, 1], mesh.vertices[:, 2],
        triangles=mesh.faces, linewidth=0.1, alpha=0.85
    )
    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.set_zlabel("Z (mm)")
    ax.set_title(title)
    return fig
