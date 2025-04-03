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

def plot_cherry_mx_switch_data():
    style.use_zoo_style()

    # Data for Cherry MX switches. Note this uses gram-force (gf) as the unit of force.
    switches = {
        'Red': {'force': 45, 'color': '#FF1F5B'},
        'Blue': {'force': 50, 'color': '#009ADE'},
        'Brown': {'force': 45, 'color': '#A6761D'},
        'Black': {'force': 60, 'color': '#000000'},
        'Clear': {'force': 55, 'color': '#FFFFFF'},  # Using white for clear
        'Grey [Tactile]': {'force': 80, 'color': '#A0B1BA'},
        'Grey [Linear]': {'force': 80, 'color': '#A0B1BA'},
        'Green': {'force': 70, 'color': '#00CD6C'},
        'White': {'force': 80, 'color': '#FFFFFF'}
    }

    # Prepare data for plotting.
    names = list(switches.keys())
    forces = [switches[name]['force'] for name in names]
    colors = [switches[name]['color'] for name in names]

    # Create figure and axis.
    bars = plt.bar(names, forces)

    # Color each bar according to the switch color.
    for bar, color in zip(bars, colors):
        bar.set_color(color)
        bar.set_edgecolor('black')
        bar.set_linewidth(1)
            

    # Customize the plot.
    plt.title('Cherry MX Switch Actuation Forces', pad=20)
    plt.xlabel('Switch Type')
    plt.ylabel('Actuation Force [gf]')
    
    # Rotate x-axis labels for better readability.
    plt.xticks(rotation=30, ha='right')

    # Save the plot.
    plt.savefig('01-cherry-mx-switches.png')
    plt.close()

if __name__ == "__main__":
    plot_cherry_mx_switch_data()