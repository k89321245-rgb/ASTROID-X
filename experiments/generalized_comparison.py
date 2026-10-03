"""
ASTROID-X
Experiment E18: Generalized Curve Comparison

Purpose:
    Quantitatively compare the generalized family

        |x/a|^p + |y/a|^p = 1

    for several exponent values.

    We compare:
        1. Enclosed area
        2. Maximum radial distance

    The analytical area is

        A(p) =
        4 a^2 Gamma(1 + 1/p)^2
        / Gamma(1 + 2/p)

    The astroid corresponds to p = 2/3.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma


a = 5.0

p_values = np.array([
    0.5,
    2 / 3,
    1.0,
    1.5,
    2.0,
    3.0
])


theta = np.linspace(
    0,
    2 * np.pi,
    5000
)


areas = []
radial_maxima = []


print("ASTROID-X")
print("Experiment E18: Generalized Curve Comparison")
print("=" * 60)

print(f"Scale parameter a = {a}")

print()
print(
    "p-value        "
    "Analytical Area        "
    "Maximum Radius"
)

print("-" * 60)


for p in p_values:

    denominator = (
        np.abs(np.cos(theta)) ** p
        +
        np.abs(np.sin(theta)) ** p
    )

    r = a / (
        denominator ** (1 / p)
    )

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    area = (
        4
        * a**2
        * gamma(1 + 1 / p)**2
        / gamma(1 + 2 / p)
    )

    radial_max = np.max(
        np.sqrt(x**2 + y**2)
    )

    areas.append(area)
    radial_maxima.append(radial_max)

    print(
        f"{p:<14.6f}"
        f"{area:<22.6f}"
        f"{radial_max:.6f}"
    )


areas = np.array(areas)
radial_maxima = np.array(radial_maxima)


# --------------------------------------------------
# Area comparison
# --------------------------------------------------

plt.figure(figsize=(9, 6))

plt.plot(
    p_values,
    areas,
    "o-",
    label="Analytical area"
)

plt.axvline(
    2 / 3,
    linestyle="--",
    label="Astroid p = 2/3"
)

plt.xlabel("Exponent p")
plt.ylabel("Enclosed area")

plt.title(
    "Enclosed Area vs Generalized Exponent"
)

plt.grid(True)
plt.legend()

plt.show()


# --------------------------------------------------
# Radial distance comparison
# --------------------------------------------------

plt.figure(figsize=(9, 6))

plt.plot(
    p_values,
    radial_maxima,
    "o-",
    label="Maximum radial distance"
)

plt.axhline(
    a,
    linestyle="--",
    label="Maximum possible radius = a"
)

plt.xlabel("Exponent p")
plt.ylabel("Maximum radial distance")

plt.title(
    "Maximum Radial Distance vs Exponent"
)

plt.grid(True)
plt.legend()

plt.show()


# --------------------------------------------------
# Astroid-specific validation
# --------------------------------------------------

astroid_index = np.argmin(
    np.abs(p_values - 2 / 3)
)

astroid_area = areas[astroid_index]

theoretical_astroid_area = (
    3 * np.pi * a**2 / 8
)

area_error = abs(
    astroid_area - theoretical_astroid_area
)

print()
print("Astroid Validation")
print("-" * 60)

print(
    f"Generalized formula at p = 2/3 = "
    f"{astroid_area:.12f}"
)

print(
    f"Known astroid area = "
    f"{theoretical_astroid_area:.12f}"
)

print(
    f"Absolute difference = "
    f"{area_error:.6e}"
)