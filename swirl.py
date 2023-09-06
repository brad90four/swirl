# swirl

from math import cos, radians, sin

import click  # noqa: F401
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from cycler import cycler
from numpy import arange

# Spirograph trajectories calculated from https://en.wikipedia.org/wiki/Spirograph


def x_component(angle: float, inner_radius: float = 0.1, outer_radius: float = 1.0, rho: float = 0.05) -> float:
    """
    Calculate the x component of position for a given input angle.

    Args:
        angle (float): The angle of rotation of the inner circle in relation to the outer circle.
        inner_radius (float, optional): Radius of the inner circle. Defaults to 0.1.
        outer_radius (float, optional): Radius of the outer circle. Defaults to 1.0.
        rho (float, optional): Distance away from the edge of the inner circle. Defaults to 0.05.

    Returns:
        float: X component of position
    """
    radius_ratio = rho / inner_radius
    k = inner_radius / outer_radius
    return outer_radius * ((1 - k) * cos(radians(angle)) + radius_ratio * k * cos(radians(angle) * ((1 - k) / k)))


def y_component(angle: float, inner_radius: float = 0.1, outer_radius: float = 1.0, rho: float = 0.05) -> float:
    """
    Calculate the y component of position for a given input angle.

    Args:
        angle (float): The angle of rotation of the inner circle in relation to the outer circle.
        inner_radius (float, optional): Radius of the inner circle. Defaults to 0.1.
        outer_radius (float, optional): Radius of the outer circle. Defaults to 1.0.
        rho (float, optional): Distance away from the edge of the inner circle. Defaults to 0.05.

    Returns:
        float: Y component of position
    """
    radius_ratio = rho / inner_radius
    k = inner_radius / outer_radius
    return outer_radius * ((1 - k) * sin(radians(angle)) - radius_ratio * k * sin(radians(angle) * ((1 - k) / k)))


def multi_plot(inner_radius: float, outer_radius: float) -> None:
    """
    A helper function to plot multiple graphs by incrementing the 'rho' dimension.

    Args:
        inner_radius (float, optional): _description_. Defaults to 0.1.
        outer_radius (float, optional): _description_. Defaults to 1.0.
    """
    plt.rc("axes", prop_cycle=(cycler("color", mcolors.BASE_COLORS)))
    for rho_change in arange(0, 0.1, 0.005):
        X = []  # noqa: N806
        Y = []  # noqa: N806
        for t in range(360):
            X.append(x_component(t, inner_radius, outer_radius, rho_change))
            Y.append(y_component(t, inner_radius, outer_radius, rho_change))
        plt.plot(X, Y, linewidth=0.2)
        plt.axis("off")


multi_plot(0.05, 1.0)
plt.show()
