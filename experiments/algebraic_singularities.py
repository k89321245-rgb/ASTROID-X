"""
ASTROID-X
Experiment E16: Algebraic Singularities

Purpose:
    Detect the four cusp points of the astroid directly
    from its implicit algebraic equation.

Implicit astroid:

    F(x, y) =
        (x^2 + y^2 - a^2)^3
        + 27a^2 x^2 y^2

A singular point satisfies:

    F(x, y) = 0

and

    grad F(x, y) = (0, 0)

The expected singular points are:

    (a, 0)
    (0, a)
    (-a, 0)
    (0, -a)
"""

import numpy as np
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from astroid import (
    implicit_astroid,
    implicit_astroid_gradient,
)


a = 5.0


# Expected cusp locations
cusps = [
    (a, 0),
    (0, a),
    (-a, 0),
    (0, -a)
]


print("ASTROID-X")
print("Experiment E16: Algebraic Singularities")
print("=" * 55)

print(f"Scale parameter a = {a}")

print()
print("Singularity Verification")
print("-" * 55)

for x, y in cusps:

    value = implicit_astroid(x, y, a)

    Fx, Fy = implicit_astroid_gradient(x, y, a)

    gradient_norm = np.sqrt(
        Fx**2 + Fy**2
    )

    print()
    print(f"Point: ({x:.1f}, {y:.1f})")

    print(
        f"F(x, y) = "
        f"{value:.6e}"
    )

    print(
        f"F_x(x, y) = "
        f"{Fx:.6e}"
    )

    print(
        f"F_y(x, y) = "
        f"{Fy:.6e}"
    )

    print(
        f"||grad F|| = "
        f"{gradient_norm:.6e}"
    )


print()
print("Theoretical Conditions")
print("-" * 55)

print("A singular point must satisfy:")
print()
print("F(x, y) = 0")
print("||grad F(x, y)|| = 0")

print()
print("Expected singular points:")
print()

for point in cusps:
    print(point)