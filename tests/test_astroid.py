import sys
from pathlib import Path

import numpy as np

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from astroid import (
    astroid_coordinates,
    astroid_derivatives,
    astroid_second_derivatives,
    curvature,
    curvature_from_derivatives,
    implicit_astroid,
    implicit_astroid_gradient,
    radial_distance,
    radius_of_curvature,
    tangent_slope,
    unit_normal,
)


def test_parametric_coordinates_satisfy_cartesian_equation():
    t = np.linspace(0, 2 * np.pi, 1000)
    a = 5.0

    x, y = astroid_coordinates(t, a)

    lhs = (
        np.abs(x) ** (2 / 3)
        +
        np.abs(y) ** (2 / 3)
    )

    rhs = a ** (2 / 3)

    np.testing.assert_allclose(
        lhs,
        rhs,
        rtol=1e-12,
        atol=1e-12
    )


def test_first_derivatives():
    t = np.linspace(0.01, 2 * np.pi - 0.01, 500)
    a = 5.0
    h = 1e-6

    x_plus, y_plus = astroid_coordinates(t + h, a)
    x_minus, y_minus = astroid_coordinates(t - h, a)

    numerical_dx = (
        x_plus - x_minus
    ) / (2 * h)

    numerical_dy = (
        y_plus - y_minus
    ) / (2 * h)

    analytical_dx, analytical_dy = (
        astroid_derivatives(t, a)
    )

    np.testing.assert_allclose(
        numerical_dx,
        analytical_dx,
        rtol=1e-6,
        atol=1e-8
    )

    np.testing.assert_allclose(
        numerical_dy,
        analytical_dy,
        rtol=1e-6,
        atol=1e-8
    )


def test_second_derivatives():
    t = np.linspace(0.02, 2 * np.pi - 0.02, 500)
    a = 5.0
    h = 1e-5

    dx_plus, dy_plus = (
        astroid_derivatives(t + h, a)
    )

    dx_minus, dy_minus = (
        astroid_derivatives(t - h, a)
    )

    numerical_d2x = (
        dx_plus - dx_minus
    ) / (2 * h)

    numerical_d2y = (
        dy_plus - dy_minus
    ) / (2 * h)

    analytical_d2x, analytical_d2y = (
        astroid_second_derivatives(t, a)
    )

    np.testing.assert_allclose(
        numerical_d2x,
        analytical_d2x,
        rtol=1e-5,
        atol=1e-7
    )

    np.testing.assert_allclose(
        numerical_d2y,
        analytical_d2y,
        rtol=1e-5,
        atol=1e-7
    )


def test_tangent_slope():
    t = np.linspace(0.01, 2 * np.pi - 0.01, 500)

    dx_dt, dy_dt = astroid_derivatives(t)

    slope_from_derivatives = (
        dy_dt / dx_dt
    )

    slope_direct = tangent_slope(t)

    np.testing.assert_allclose(
        slope_from_derivatives,
        slope_direct,
        rtol=1e-12,
        atol=1e-12
    )


def test_unit_normal():
    t = np.linspace(0.01, 2 * np.pi - 0.01, 500)

    dx_dt, dy_dt = astroid_derivatives(t)
    nx, ny = unit_normal(t)

    normal_length = np.sqrt(
        nx ** 2 + ny ** 2
    )

    np.testing.assert_allclose(
        normal_length,
        1.0,
        rtol=1e-12,
        atol=1e-12
    )

    dot_product = (
        dx_dt * nx
        +
        dy_dt * ny
    )

    np.testing.assert_allclose(
        dot_product,
        0.0,
        rtol=1e-12,
        atol=1e-12
    )


def test_normal_vector_components():
    t = np.linspace(0, 2 * np.pi, 500)

    nx, ny = unit_normal(t)

    np.testing.assert_allclose(
        nx,
        -np.sin(t),
        rtol=1e-12,
        atol=1e-12
    )

    np.testing.assert_allclose(
        ny,
        -np.cos(t),
        rtol=1e-12,
        atol=1e-12
    )


def test_curvature_implementations_agree():
    t = np.linspace(
        0.01,
        2 * np.pi - 0.01,
        1000
    )

    kappa_simplified = curvature(t)
    kappa_general = curvature_from_derivatives(t)

    np.testing.assert_allclose(
        kappa_simplified,
        kappa_general,
        rtol=1e-12,
        atol=1e-12
    )


def test_curvature_is_positive_on_smooth_points():
    t = np.linspace(
        0.01,
        2 * np.pi - 0.01,
        1000
    )

    kappa = curvature(t)

    assert np.all(kappa > 0)


def test_radius_of_curvature():
    t = np.linspace(
        0.01,
        2 * np.pi - 0.01,
        500
    )

    kappa = curvature(t)
    rho = radius_of_curvature(t)

    np.testing.assert_allclose(
        rho,
        1 / kappa,
        rtol=1e-12,
        atol=1e-12
    )


def test_radial_distance_bounds():
    a = 5.0

    t = np.linspace(
        0,
        2 * np.pi,
        10000
    )

    r = radial_distance(t, a)

    theoretical_min = a / 2
    theoretical_max = a

    assert np.min(r) >= (
        theoretical_min - 1e-12
    )

    assert np.max(r) <= (
        theoretical_max + 1e-12
    )

    np.testing.assert_allclose(
        np.min(r),
        theoretical_min,
        rtol=1e-5,
        atol=1e-5
    )

    np.testing.assert_allclose(
        np.max(r),
        theoretical_max,
        rtol=1e-12,
        atol=1e-12
    )


def test_radial_distance_matches_coordinates():
    a = 5.0

    t = np.linspace(
        0,
        2 * np.pi,
        2000
    )

    x, y = astroid_coordinates(t, a)

    radial_from_coordinates = np.sqrt(
        x ** 2 + y ** 2
    )

    radial_from_formula = radial_distance(
        t,
        a
    )

    np.testing.assert_allclose(
        radial_from_formula,
        radial_from_coordinates,
        rtol=1e-12,
        atol=1e-12
    )


def test_implicit_astroid_at_cusps():
    a = 5.0

    cusp_points = [
        (a, 0.0),
        (0.0, a),
        (-a, 0.0),
        (0.0, -a),
    ]

    for x, y in cusp_points:
        value = implicit_astroid(
            x,
            y,
            a
        )

        np.testing.assert_allclose(
            value,
            0.0,
            rtol=1e-12,
            atol=1e-12
        )


def test_implicit_astroid_gradient_at_cusps():
    a = 5.0

    cusp_points = [
        (a, 0.0),
        (0.0, a),
        (-a, 0.0),
        (0.0, -a),
    ]

    for x, y in cusp_points:
        Fx, Fy = implicit_astroid_gradient(
            x,
            y,
            a
        )

        np.testing.assert_allclose(
            Fx,
            0.0,
            rtol=1e-12,
            atol=1e-12
        )

        np.testing.assert_allclose(
            Fy,
            0.0,
            rtol=1e-12,
            atol=1e-12
        )