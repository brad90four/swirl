from math import cos, radians, sin

import click
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from cycler import cycler
from numpy import arange

# Spirograph trajectories calculated from https://en.wikipedia.org/wiki/Spirograph


def component(angle: float, inner_radius: float = 0.1, outer_radius: float = 1.0, rho: float = 0.2) -> float:
    """
    Calculate the X and Y components of position for a given input angle.

    Args:
        angle (float): The angle of rotation of the inner circle in relation to the outer circle.
        inner_radius (float, optional): Radius of the inner circle. Defaults to 0.1.
        outer_radius (float, optional): Radius of the outer circle. Defaults to 1.0.
        rho (float, optional): Distance away from the center of the inner circle. Defaults to 0.05.

    Returns:
        float: X component of position
    """
    radius_ratio = rho / inner_radius
    k = inner_radius / outer_radius
    x = outer_radius * ((1 - k) * cos(radians(angle)) + radius_ratio * k * cos(radians(angle) * ((1 - k) / k)))
    y = outer_radius * ((1 - k) * sin(radians(angle)) - radius_ratio * k * sin(radians(angle) * ((1 - k) / k)))
    return x, y


@click.group(invoke_without_command=True)
@click.pass_context
def swirl(ctx: click.core.Context) -> None:
    """
    CLI entry point. Will plot a single default spirograph if left blank without a subcommand.

    \f

    Args:
        ctx (click.core.Context): Context passed by click to determine if subcommand is empty.
    """
    if ctx.invoked_subcommand is None:
        single()


@swirl.command("single", short_help="Create single figure")
@click.option("--inner", default=0.1, help="Size of the inner circle.", type=float)
@click.option("--outer", default=1.0, help="Size of the outer circle.", type=float)
def single(inner: float, outer: float) -> None:
    """
    Function to plot and display a default spirograph.

    \f

    Args:
        inner (float, optional): Radius of the inner circle. Defaults to 0.1.
        outer (float, optional): Radius of the outer circle. Defaults to 1.0.
    """
    X = []  # noqa: N806
    Y = []  # noqa: N806
    for t in range(361):
        X.append(component(t, inner, outer)[0])
        Y.append(component(t, inner, outer)[1])
    plt.plot(X, Y, linewidth=0.2, color="k")
    plt.axis("off")
    plt.show()


@swirl.command("multi", short_help="Create multiple figures")
@click.option("--inner", default=0.1, help="Size of the inner circle.", type=float)
@click.option("--outer", default=1.0, help="Size of the outer circle.", type=float)
def multi(inner: float, outer: float) -> None:
    """
    A helper function to plot multiple graphs by incrementing the 'rho' dimension.

    \f

    Args:
        inner (float, optional): Radius of the inner circle. Defaults to 0.1.
        outer (float, optional): Radius of the outer circle. Defaults to 1.0.
    """
    plt.rc("axes", prop_cycle=(cycler("color", mcolors.BASE_COLORS)))
    for rho_change in arange(-inner * 2, inner * 2, inner / 20):
        X = []  # noqa: N806
        Y = []  # noqa: N806
        for t in range(361):
            X.append(component(t, inner, outer, rho_change)[0])
            Y.append(component(t, inner, outer, rho_change)[1])
        plt.plot(X, Y, linewidth=0.2)
        plt.axis("off")
    plt.show()


if __name__ == "__main__":
    swirl()
