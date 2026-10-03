"""
ASTROID-X
Experiment E13: Cusp Scaling and Zoom Convergence

Purpose:
    Investigate whether the numerical cusp exponent approaches
    the theoretical value 3/2 as we zoom closer to the cusp.

Theoretical result:

    |y| ~ C(a - x)^(3/2)

Therefore:

    log(|y|) ~ log(C) + (3/2) log(a - x)

The experiment calculates the exponent for progressively
smaller neighborhoods around t = 0.
"""

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. PARAMETERS
# ============================================================

a = 5.0

# Different neighborhood sizes around the cusp t = 0
zoom_ranges = [
    0.50,
    0.25,
    0.10,
    0.05,
    0.025
]

theoretical_exponent = 1.5


# ============================================================
# 2. FUNCTION TO ESTIMATE THE EXPONENT
# ============================================================

def estimate_exponent(t_max):
    """
    Estimate the cusp exponent inside the interval
    [-t_max, t_max].
    """

    # Generate parameter values
    t = np.linspace(-t_max, t_max, 1000)

    # Exact astroid
    x = a * np.cos(t) ** 3
    y = a * np.sin(t) ** 3

    # Distance from the cusp in the x-direction
    dx = a - x

    # Magnitude of y
    abs_y = np.abs(y)

    # Remove values too close to zero
    # because log(0) is undefined.
    mask = (
        (dx > 1e-12)
        & (abs_y > 1e-12)
    )

    log_dx = np.log(dx[mask])
    log_y = np.log(abs_y[mask])

    # Linear regression:
    #
    # log(|y|) = m log(a-x) + c

    slope, intercept = np.polyfit(
        log_dx,
        log_y,
        1
    )

    return slope


# ============================================================
# 3. CALCULATE EXPONENT FOR EACH ZOOM LEVEL
# ============================================================

estimated_exponents = []

print("ASTROID-X")
print("Experiment E13: Cusp Scaling and Zoom Convergence")
print("=" * 55)

print(f"Scale parameter a = {a}")
print(f"Theoretical exponent = {theoretical_exponent}")

print()
print("Zoom Range      Estimated Exponent")
print("-" * 40)


for t_max in zoom_ranges:

    exponent = estimate_exponent(t_max)

    estimated_exponents.append(exponent)

    print(
        f"{t_max:<15.3f}"
        f"{exponent:.6f}"
    )


# ============================================================
# 4. CALCULATE ERRORS
# ============================================================

estimated_exponents = np.array(estimated_exponents)

absolute_errors = np.abs(
    estimated_exponents - theoretical_exponent
)

relative_errors = (
    absolute_errors / theoretical_exponent
) * 100


print()
print("Exponent Errors")
print("-" * 40)

for i, t_max in enumerate(zoom_ranges):

    print(
        f"t_max = {t_max:<6.3f} | "
        f"absolute error = {absolute_errors[i]:.6f} | "
        f"relative error = {relative_errors[i]:.4f}%"
    )


# ============================================================
# 5. PLOT: ESTIMATED EXPONENT VS ZOOM RANGE
# ============================================================

plt.figure(figsize=(9, 6))

plt.plot(
    zoom_ranges,
    estimated_exponents,
    "o-",
    label="Estimated exponent"
)

plt.axhline(
    theoretical_exponent,
    linestyle="--",
    label="Theoretical exponent = 1.5"
)

plt.xlabel("Maximum |t| in neighborhood")
plt.ylabel("Estimated cusp exponent")

plt.title("Cusp Exponent vs Zoom Level")

plt.grid(True)
plt.legend()

plt.show()