"""
ASTROID-X
Core Mathematical Library

This module contains reusable analytical and differential-geometric
functions for the astroid curve.

Standard astroid:

    x = a cos^3(t)
    y = a sin^3(t)

Equivalent Cartesian equation:

    |x|^(2/3) + |y|^(2/3) = a^(2/3)

Implicit algebraic equation:

    (x^2 + y^2 - a^2)^3 + 27 a^2 x^2 y^2 = 0

The functions in this module are designed to be reused by the
experiments, tests, and future extensions of ASTROID-X.
"""

import numpy as np


def astroid_coordinates(t, a=5.0):
    """
    Compute parametric coordinates of the astroid.

    Parameters
    ----------
    t : array-like
        Parameter values in radians.
    a : float
        Scale parameter.

    Returns
    -------
    x : numpy.ndarray
        x-coordinates.
    y : numpy.ndarray
        y-coordinates.
    """

    t = np.asarray(t)

    x = a * np.cos(t) ** 3
    y = a * np.sin(t) ** 3

    return x, y


def astroid_derivatives(t, a=5.0):
    """
    Compute first derivatives of the parametric astroid.

    x'(t) = -3a cos^2(t) sin(t)

    y'(t) =  3a sin^2(t) cos(t)
    """

    t = np.asarray(t)

    dx_dt = (
        -3
        * a
        * np.cos(t) ** 2
        * np.sin(t)
    )

    dy_dt = (
        3
        * a
        * np.sin(t) ** 2
        * np.cos(t)
    )

    return dx_dt, dy_dt


def astroid_second_derivatives(t, a=5.0):
    """
    Compute second derivatives of the parametric astroid.

    Returns
    -------
    d2x_dt2 : numpy.ndarray
        Second derivative of x.
    d2y_dt2 : numpy.ndarray
        Second derivative of y.
    """

    t = np.asarray(t)

    d2x_dt2 = (
        3
        * a
        * np.cos(t)
        * (
            2 * np.sin(t) ** 2
            - np.cos(t) ** 2
        )
    )

    d2y_dt2 = (
        3
        * a
        * np.sin(t)
        * (
            2 * np.cos(t) ** 2
            - np.sin(t) ** 2
        )
    )

    return d2x_dt2, d2y_dt2


def tangent_slope(t):
    """
    Compute the tangent slope dy/dx.

    For the astroid:

        dy/dx = -tan(t)

    The result may diverge at vertical tangents.
    """

    t = np.asarray(t)

    return -np.tan(t)


def curvature(t, a=5.0):
    """
    Compute the curvature of the astroid.

    For smooth points:

        kappa = 1 / (3a |sin(t) cos(t)|)

    Curvature diverges at the four cusps.
    """

    t = np.asarray(t)

    denominator = (
        3
        * a
        * np.abs(np.sin(t) * np.cos(t))
    )

    with np.errstate(divide="ignore", invalid="ignore"):
        kappa = 1 / denominator

    return kappa


def curvature_from_derivatives(t, a=5.0):
    """
    Compute curvature directly from first and second derivatives.

    General planar parametric curvature formula:

        kappa =
            |x'y'' - y'x''|
            ----------------
            (x'^2 + y'^2)^(3/2)

    This provides an independent implementation for verification.
    """

    dx_dt, dy_dt = astroid_derivatives(t, a)

    d2x_dt2, d2y_dt2 = astroid_second_derivatives(t, a)

    numerator = np.abs(
        dx_dt * d2y_dt2
        -
        dy_dt * d2x_dt2
    )

    denominator = (
        dx_dt ** 2
        +
        dy_dt ** 2
    ) ** (3 / 2)

    with np.errstate(divide="ignore", invalid="ignore"):
        kappa = numerator / denominator

    return kappa


def radius_of_curvature(t, a=5.0):
    """
    Compute the radius of curvature.

        rho = 1 / kappa

    For the astroid:

        rho = 3a |sin(t) cos(t)|
    """

    t = np.asarray(t)

    rho = (
        3
        * a
        * np.abs(np.sin(t) * np.cos(t))
    )

    return rho


def radial_distance(t, a=5.0):
    """
    Compute the distance from the origin to the astroid.

    Starting from:

        r^2 = x^2 + y^2

    the astroid gives:

        r = a sqrt(
            1 - (3/4) sin^2(2t)
        )
    """

    t = np.asarray(t)

    r = (
        a
        * np.sqrt(
            1
            -
            (3 / 4)
            * np.sin(2 * t) ** 2
        )
    )

    return r


def unit_normal(t):
    """
    Compute an inward-pointing unit normal vector.

    N(t) = (-sin(t), -cos(t))

    The vector has unit magnitude and is perpendicular
    to the tangent vector.
    """

    t = np.asarray(t)

    nx = -np.sin(t)
    ny = -np.cos(t)

    return nx, ny


def implicit_astroid(x, y, a=5.0):
    """
    Evaluate the implicit algebraic equation of the astroid.

    F(x, y) =
        (x^2 + y^2 - a^2)^3
        + 27a^2 x^2 y^2

    Points on the astroid satisfy:

        F(x, y) = 0

    Parameters
    ----------
    x : array-like
        x-coordinate values.
    y : array-like
        y-coordinate values.
    a : float
        Scale parameter.

    Returns
    -------
    F : numpy.ndarray
        Value of the implicit equation.
    """

    x = np.asarray(x)
    y = np.asarray(y)

    q = (
        x ** 2
        +
        y ** 2
        -
        a ** 2
    )

    return (
        q ** 3
        +
        27
        * a ** 2
        * x ** 2
        * y ** 2
    )


def implicit_astroid_gradient(x, y, a=5.0):
    """
    Compute the gradient of the implicit astroid equation.

    For

        F(x, y) =
            (x^2 + y^2 - a^2)^3
            + 27a^2 x^2 y^2

    the gradient is:

        grad F = (F_x, F_y)

    where

        F_x =
            6x(x^2 + y^2 - a^2)^2
            + 54a^2 x y^2

        F_y =
            6y(x^2 + y^2 - a^2)^2
            + 54a^2 x^2 y
    """

    x = np.asarray(x)
    y = np.asarray(y)

    q = (
        x ** 2
        +
        y ** 2
        -
        a ** 2
    )

    Fx = (
        6
        * x
        * q ** 2
        +
        54
        * a ** 2
        * x
        * y ** 2
    )

    Fy = (
        6
        * y
        * q ** 2
        +
        54
        * a ** 2
        * x ** 2
        * y
    )

    return Fx, Fy