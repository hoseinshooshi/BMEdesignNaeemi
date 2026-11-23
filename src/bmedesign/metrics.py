def estimate_metrics(mesh, density_g_cm3=1.20):
    volume_mm3 = float(mesh.volume)
    surface_mm2 = float(mesh.area)
    volume_cm3 = abs(volume_mm3) / 1000.0
    mass_g = volume_cm3 * density_g_cm3
    return {
        "volume_mm3": abs(volume_mm3),
        "surface_area_mm2": surface_mm2,
        "estimated_mass_g": mass_g,
    }
