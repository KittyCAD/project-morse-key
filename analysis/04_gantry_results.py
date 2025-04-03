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
from typing import List
import matplotlib.pyplot as plt
from zooplotlib import style
import numpy as np

# Physical constants.
G: float = 9.81
MM_TO_M: float = 1/1000
LEADSCREW_PITCH_MM: float = 1.75

# Test data.
THETA_DEG: List[float] = [0, 180, 360, 540, 720, 900]
FORCE_G: List[float] = [0, 26, 53, 100, 114, 170]

# Target parameters.
TARGET_FORCE_G: float = 80
TARGET_DISPLACEMENT_MM: float = 2
TARGET_STIFFNESS: float = (TARGET_FORCE_G * G * MM_TO_M) / TARGET_DISPLACEMENT_MM

def plot_fx() -> None:
    # Generate force-displacement plot from gantry test data.
    style.use_zoo_style()

    # Convert angular displacements to linear.
    x = np.multiply(THETA_DEG, LEADSCREW_PITCH_MM / 360)

    # Convert force to Newtons.
    f = np.multiply(FORCE_G, G * MM_TO_M)

    # Fit linear model.
    coeffs = np.polyfit(x, f, 1)
    
    # Calculate R-squared.
    y_mean = np.mean(f)
    ss_tot = np.sum((f - y_mean) ** 2)
    ss_res = np.sum((f - np.polyval(coeffs, x)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    # Create plot.
    fig, ax = plt.subplots()
    
    # Plot measured data.
    ax.plot(
        x,
        f,
        label="Measured Points",
        linestyle="none",
        marker="o",
    )

    # Plot fitted line.
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = np.polyval(coeffs, x_fit)
    ax.plot(
        x_fit,
        y_fit,
        label=f"Fitted: {coeffs[0]:.2f} N/mm, $r^2$ = {r_squared:.2f}",
        linestyle="--",
        color="#ff1f5b",
    )

    # Plot target reference.
    ax.plot(
        TARGET_DISPLACEMENT_MM,
        TARGET_FORCE_G * G * MM_TO_M,
        linestyle="none",
        marker="o",
        color="#00cd6c",
        label="Target Reference Point",
    )

    # Plot target stiffness line.
    x_target = np.linspace(min(x), max(x), 100)
    y_target = np.multiply(TARGET_STIFFNESS, x_target)
    ax.plot(
        x_target,
        y_target,
        color="#00cd6c",
        label=f"Target: {TARGET_STIFFNESS:.2f} N/mm",
    )

    ax.set_title("Force-Displacement Characteristic")
    ax.set_xlabel("Lead Screw Displacement [mm]")
    ax.set_ylabel("Force [N]")
    ax.legend()

    plt.savefig("09-test-results.png")
    plt.close()

if __name__ == "__main__":
    plot_fx()