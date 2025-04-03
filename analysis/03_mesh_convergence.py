# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy",
#     "scipy",
#     "zooplotlib",
#     "zooplotly",
# ]
#
# [tool.uv.sources]
# zooplotlib = { git = "ssh://git@github.com/KittyCAD/zooplotlib.git" }
# zooplotly = { git = "ssh://git@github.com/KittyCAD/zooplotly.git" }
# ///
from typing import Dict, List
import matplotlib.pyplot as plt
from zooplotlib import style
import numpy as np

# Mesh configurations for global refinement studies.
MESHES: List[Dict[str, float]] = [
    {
        "iteration": 1,
        "mesh_max": 5,
        "mesh_min": 2,
        "d_max": 2.248,  # Maximum deflection in mm.
        "sigma_max": 3.751,  # Maximum von Mises stress in MPa.
    },
    {
        "iteration": 2,
        "mesh_max": 2.5,
        "mesh_min": 1,
        "d_max": 2.291,
        "sigma_max": 3.853,
    },
    {
        "iteration": 3,
        "mesh_max": 1.25,
        "mesh_min": 0.5,
        "d_max": 2.324,
        "sigma_max": 4.083,
    },
    {
        "iteration": 4,
        "mesh_max": 0.625,
        "mesh_min": 0.25,
        "d_max": 2.332,
        "sigma_max": 4.342,
    },
]

# Additional test with local refinement in high-stress regions.
LOCAL_REFINEMENT: List[Dict[str, float]] = [
    {
        "iteration": 5,
        "mesh_max": 1.25,
        "mesh_min": 0.5,
        "refinement": 0.25,
        "d_max": 2.33,
        "sigma_max": 4.346,
    }
]

def plot_convergence() -> None:
    # Generate mesh convergence plots for deflection and stress.
    style.use_zoo_style()

    # Create figure and axis.
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

    # Extract data for global mesh refinement.
    mesh_densities = [1 / m["mesh_min"] for m in MESHES]
    deflections = [m["d_max"] for m in MESHES]
    stresses = [m["sigma_max"] for m in MESHES]

    # Plot deflection results.
    ax1.plot(mesh_densities, deflections, ".-", label="Global Mesh")

    # Add data labels for deflection points.
    for i, mesh in enumerate(MESHES):
        txt = f"Max: {mesh['mesh_max']}mm\nMin: {mesh['mesh_min']}mm"
        ax1.annotate(
            txt,
            (mesh_densities[i], deflections[i]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            fontsize=8,
        )

    # Add local refinement results for deflection.
    local_mesh_density = 1 / LOCAL_REFINEMENT[0]["refinement"]
    local_deflection = LOCAL_REFINEMENT[0]["d_max"]
    ax1.plot(
        local_mesh_density,
        local_deflection,
        "o",
        markerfacecolor="none",
        label="Inc. Local Refinement",
    )

    # Label local refinement point.
    txt = f"Max: {LOCAL_REFINEMENT[0]['mesh_max']}mm\nMin: {LOCAL_REFINEMENT[0]['mesh_min']}mm\nRefinement: {LOCAL_REFINEMENT[0]['refinement']}mm"
    ax1.annotate(
        txt,
        (local_mesh_density, local_deflection),
        textcoords="offset points",
        xytext=(0, -35),
        ha="center",
        fontsize=8,
    )

    # Plot stress results.
    ax2.plot(mesh_densities, stresses, ".-", label="Global Mesh")
    local_stress = LOCAL_REFINEMENT[0]["sigma_max"]
    ax2.plot(
        local_mesh_density,
        local_stress,
        "o",
        markerfacecolor="none",
        label="Inc. Local Refinement",
    )

    # Configure plot formatting.
    ax1.set_ylabel("Maximum Deflection [mm]")
    ax1.set_title("Mesh Convergence | Deflection")
    ax1.set_ylim(0, 3)
    ax1.legend()

    ax2.set_xlabel("Mesh Density [mm-1]")
    ax2.set_ylabel("Maximum Stress [MPa]")
    ax2.set_title("Mesh Convergence | Von Mises Stress") 
    ax2.set_ylim(0, 5)
    ax2.legend()

    # Save output and cleanup.
    plt.savefig("mesh-convergence.png")
    plt.close()

if __name__ == "__main__":
    plot_convergence()