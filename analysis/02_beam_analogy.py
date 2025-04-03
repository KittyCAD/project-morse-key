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
import matplotlib.pyplot as plt
from zooplotlib import style
import numpy as np

E_PLA = 2.75e9  # Pa
E_PLA_CF = 3.95e9  # Pa


def compute_deflection(
    length: float,
    force: float,
    elasticity: float,
    inertia: float,
) -> float:
    # Compute the deflection of a beam.
    return force * length**3 / (3 * elasticity * inertia)


def compute_moment_of_inertia(b: float, d: float) -> float:
    return b * d**3 / 12


def plot_stiffness():
    style.use_zoo_style()

    # Set material.
    e = E_PLA

    # Set beam dimension range.
    l_range = np.arange(50 / 1000, 100 / 1000, 1 / 1000)
    b_beam = 10 / 1000
    d_beam = np.arange(3 / 1000, 5 / 1000, 0.5 / 1000)

    # Set applied force.
    f_applied = 0.78  # N

    # Build array out outputs. We want an array of deflection arrays; one per depth.
    deflections = []
    for depth in d_beam:
        inertia = compute_moment_of_inertia(b_beam, depth)

        local_deflections = []
        for length in l_range:
            local_deflections.append(
                compute_deflection(
                    length,
                    f_applied,
                    e,
                    inertia,
                )
            )
        deflections.append(local_deflections)

    # Plot the deflection.
    fig, ax = plt.subplots()

    # Create figure and axis.
    for idx, depth in enumerate(d_beam):
        ax.plot(
            np.multiply(l_range, 1000),
            np.multiply(deflections[idx], 1000),
            label=f"Depth: {depth * 1000:.1f} mm",
        )

    # Customize the plot.
    ax.set_title(f"Deflection | PLA, E={e / 1e9}MPa")
    ax.set_xlabel("Arm/Cantilever Length [mm]")
    ax.set_ylabel("Deflection [mm]")
    ax.set_ylim(0, 5)
    ax.legend()

    # Save the plot.
    plt.savefig("08-beam-deflection.png")
    plt.close()

    # Save results to file.
    with open("08-beam-deflection.txt", "w") as f:
        f.write("Arm Length [mm],Depth [mm],Deflection [mm]\n")
        for idx, depth in enumerate(d_beam):
            for idx2, length in enumerate(l_range):
                f.write(f"{length * 1000},{depth * 1000},{deflections[idx][idx2]}\n")


if __name__ == "__main__":
    plot_stiffness()
