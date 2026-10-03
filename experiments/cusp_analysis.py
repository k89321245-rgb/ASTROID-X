"""
ASTROID-X
Experiment E12: Cusp and Singularity Analysis

Purpose:
    Study the local behavior of the astroid near the cusp (a, 0).

Astroid:
    x = a cos^3(t)
    y = a sin^3(t)

Local theoretical result near (a, 0):
    y^2 ~ (8 / (27a)) (a - x)^3

Equivalent form:
    |y| ~ sqrt(8 / (27a)) (a - x)^(3/2)

The experiment:
    1. Generates the astroid near the cusp.
    2. Compares it with the local approximation.
    3. Calculates approximation error.
    4. Estimates the cusp exponent using log-log analysis.
    5. Displays both visualizations.
"""

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. PARAMETERS
# ============================================================

# Scale parameter of the astroid
a = 5.0


# ============================================================
# 2. GENERATE THE ASTROID NEAR THE CUSP
# ============================================================

# The cusp (a, 0) corresponds to t = 0.
#
# We use a relatively small interval around t = 0
# because the local approximation is only valid near the cusp.

t = np.linspace(-0.5, 0.5, 1000)

# Exact parametric astroid
x = a * np.cos(t) ** 3
y = a * np.sin(t) ** 3


# ============================================================
# 3. LOCAL CUSP APPROXIMATION
# ============================================================

# From our mathematical derivation:
#
# y^2 ~ (8 / (27a)) (a - x)^3
#
# Therefore:
#
# |y| ~ sqrt(8 / (27a)) (a - x)^(3/2)

dx = a - x

y_approx = np.sqrt(8 / (27 * a)) * dx ** (3 / 2)


# ============================================================
# 4. CALCULATE APPROXIMATION ERROR
# ============================================================

# We compare the magnitude of the exact y-value
# with the magnitude predicted by the local approximation.

actual_y = np.abs(y)

error = np.abs(actual_y - y_approx)

max_error = np.max(error)
mean_error = np.mean(error)


# ============================================================
# 5. PRINT BASIC RESULTS
# ============================================================

print("ASTROID-X")
print("Experiment E12: Cusp and Singularity Analysis")
print("=" * 50)

print(f"Scale parameter a = {a}")

print()
print("Local Approximation Error")
print("-" * 50)

print(f"Maximum approximation error = {max_error:.6e}")
print(f"Mean approximation error    = {mean_error:.6e}")


# ============================================================
# 6. FIGURE 1 — CUSP AND LOCAL APPROXIMATION
# ============================================================

plt.figure(figsize=(9, 6))

# Exact astroid
plt.plot(
    x,
    y,
    label="Astroid"
)

# Positive local approximation
plt.plot(
    x,
    y_approx,
    "--",
    label="Local approximation"
)

# Negative local approximation
plt.plot(
    x,
    -y_approx,
    "--"
)

# Mark the cusp
plt.scatter(
    [a],
    [0],
    label="Cusp (a, 0)"
)

plt.xlabel("x")
plt.ylabel("y")

plt.title("Astroid Cusp and Local Approximation")

plt.axis("equal")
plt.grid(True)
plt.legend()


# ============================================================
# 7. LOG-LOG ANALYSIS
# ============================================================

# The theoretical relationship is:
#
# |y| ~ C(a - x)^(3/2)
#
# Taking logarithms:
#
# log(|y|)
#     ~ log(C) + (3/2) log(a - x)
#
# Therefore, the slope of a log-log plot
# should approach 3/2 = 1.5 near the cusp.


# Remove values too close to zero.
#
# log(0) is undefined, so these points must be excluded.

mask = (
    (dx > 1e-8)
    & (actual_y > 1e-8)
)

log_dx = np.log(dx[mask])
log_y = np.log(actual_y[mask])


# Fit:
#
# log(|y|) = slope * log(a - x) + intercept

slope, intercept = np.polyfit(
    log_dx,
    log_y,
    1
)


# ============================================================
# 8. PRINT LOG-LOG RESULTS
# ============================================================

print()
print("Log-Log Analysis")
print("-" * 50)

print(f"Estimated exponent   = {slope:.6f}")
print("Theoretical exponent = 1.500000")

print()
print("Interpretation:")
print(
    "The estimated exponent should be reasonably close "
    "to the theoretical value 1.5."
)


# ============================================================
# 9. FIGURE 2 — LOG-LOG ANALYSIS
# ============================================================

plt.figure(figsize=(8, 6))

# Numerical data
plt.scatter(
    log_dx,
    log_y,
    s=8,
    label="Astroid data"
)

# Fitted straight line
plt.plot(
    log_dx,
    slope * log_dx + intercept,
    label=f"Linear fit (slope = {slope:.4f})"
)

plt.xlabel("log(a - x)")
plt.ylabel("log(|y|)")

plt.title("Cusp Scaling: Log-Log Analysis")

plt.grid(True)
plt.legend()


# ============================================================
# 10. DISPLAY BOTH FIGURES
# ============================================================

# Calling plt.show() only once at the end allows
# both figures to be created before the program waits.

plt.show()