"""
ASTROID-X
Experiment E14: Radial Distance Behavior

Purpose:
    Investigate how the distance from the origin changes
    as a point moves around the astroid.

Astroid:
    x = a cos^3(t)
    y = a sin^3(t)

Radial distance:
    r(t) = sqrt(x^2 + y^2)

Theoretical result:
    r(t) = a sqrt(1 - (3/4) sin^2(2t))

Expected:
    r_max = a
    r_min = a/2
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from astroid import radial_distance


# ============================================================
# 1. PARAMETERS
# ============================================================

a = 5.0

# Parameter covering the complete astroid
t = np.linspace(0, 2 * np.pi, 2000)


# ============================================================
# 2. GENERATE THE ASTROID
# ============================================================

x = a * np.cos(t) ** 3
y = a * np.sin(t) ** 3


# ============================================================
# 3. NUMERICAL RADIAL DISTANCE
# ============================================================

r_numerical = np.sqrt(x**2 + y**2)


# ============================================================
# 4. THEORETICAL RADIAL DISTANCE
# ============================================================

r_theoretical = radial_distance(t, a)


# ============================================================
# 5. COMPARE THE TWO EXPRESSIONS
# ============================================================

difference = np.abs(
    r_numerical - r_theoretical
)

max_difference = np.max(difference)


# ============================================================
# 6. FIND MINIMUM AND MAXIMUM
# ============================================================

r_min = np.min(r_numerical)
r_max = np.max(r_numerical)

t_min = t[np.argmin(r_numerical)]
t_max = t[np.argmax(r_numerical)]


# ============================================================
# 7. THEORETICAL VALUES
# ============================================================

theoretical_min = a / 2
theoretical_max = a


# ============================================================
# 8. PRINT RESULTS
# ============================================================

print("ASTROID-X")
print("Experiment E14: Radial Distance Behavior")
print("=" * 50)

print(f"Scale parameter a = {a}")

print()
print("Radial Distance")
print("-" * 50)

print(f"Numerical minimum r = {r_min:.6f}")
print(f"Theoretical minimum = {theoretical_min:.6f}")

print()

print(f"Numerical maximum r = {r_max:.6f}")
print(f"Theoretical maximum = {theoretical_max:.6f}")

print()

print("Representation Check")
print("-" * 50)

print(
    f"Maximum difference between expressions = "
    f"{max_difference:.6e}"
)

print()

print("Parameter locations")
print("-" * 50)

print(f"t at numerical minimum = {t_min:.6f}")
print(f"t at numerical maximum = {t_max:.6f}")


# ============================================================
# 9. PLOT RADIAL DISTANCE
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    t,
    r_numerical,
    label="Numerical radial distance"
)

plt.plot(
    t,
    r_theoretical,
    "--",
    label="Theoretical radial distance"
)

plt.axhline(
    theoretical_min,
    linestyle=":",
    label="Theoretical minimum = a/2"
)

plt.axhline(
    theoretical_max,
    linestyle=":",
    label="Theoretical maximum = a"
)

plt.xlabel("Parameter t")
plt.ylabel("Radial distance r")

plt.title("Astroid Radial Distance")

plt.grid(True)
plt.legend()

plt.show()


# ============================================================
# 10. POLAR-STYLE GEOMETRIC VISUALIZATION
# ============================================================

plt.figure(figsize=(8, 8))

plt.plot(
    x,
    y,
    label="Astroid"
)

# Plot the minimum-radius circle for reference
theta = np.linspace(0, 2 * np.pi, 500)

circle_x = theoretical_min * np.cos(theta)
circle_y = theoretical_min * np.sin(theta)

plt.plot(
    circle_x,
    circle_y,
    "--",
    label="r = a/2"
)

# Plot the maximum-radius circle for reference

circle_x_max = theoretical_max * np.cos(theta)
circle_y_max = theoretical_max * np.sin(theta)

plt.plot(
    circle_x_max,
    circle_y_max,
    "--",
    label="r = a"
)

plt.scatter(
    [0],
    [0],
    label="Origin"
)

plt.xlabel("x")
plt.ylabel("y")

plt.title("Astroid Between Radial Bounds")

plt.axis("equal")
plt.grid(True)
plt.legend()

plt.show()