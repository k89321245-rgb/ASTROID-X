"""
ASTROID-X
Experiment E15: Normal Behavior

Purpose:
    Study the tangent and normal directions of the astroid
    and verify numerically that they are perpendicular.

Astroid:

    x = a cos^3(t)
    y = a sin^3(t)

Tangent vector:

    r'(t) =
        (-3a cos^2(t) sin(t),
          3a sin^2(t) cos(t))

Inward unit normal:

    N = (-sin(t), -cos(t))

Expected result:

    T . N = 0
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from astroid import unit_normal


# ============================================================
# 1. PARAMETERS
# ============================================================

a = 5.0

# Avoid the exact cusp points because r'(t) = 0 there.
epsilon = 0.01

t = np.linspace(
    epsilon,
    2 * np.pi - epsilon,
    800
)


# ============================================================
# 2. ASTROID
# ============================================================

x = a * np.cos(t) ** 3
y = a * np.sin(t) ** 3


# ============================================================
# 3. TANGENT VECTOR
# ============================================================

dx = -3 * a * np.cos(t) ** 2 * np.sin(t)

dy = 3 * a * np.sin(t) ** 2 * np.cos(t)


# ============================================================
# 4. TANGENT VECTOR MAGNITUDE
# ============================================================

speed = np.sqrt(
    dx ** 2 + dy ** 2
)


# ============================================================
# 5. UNIT TANGENT VECTOR
# ============================================================

Tx = dx / speed
Ty = dy / speed


# ============================================================
# 6. INWARD UNIT NORMAL VECTOR
# ============================================================

nx, ny = unit_normal(t)


# ============================================================
# 7. DOT PRODUCT
# ============================================================

dot_product = (
    Tx * nx
    +
    Ty * ny
)

max_dot_product = np.max(
    np.abs(dot_product)
)


# ============================================================
# 8. PRINT RESULTS
# ============================================================

print("ASTROID-X")
print("Experiment E15: Normal Behavior")
print("=" * 50)

print(f"Scale parameter a = {a}")

print()
print("Perpendicularity Check")
print("-" * 50)

print(
    f"Maximum |T . N| = "
    f"{max_dot_product:.6e}"
)

print()
print("Theoretical value = 0")


# ============================================================
# 9. NORMALIZE NORMAL VECTOR
# ============================================================

normal_length = np.sqrt(
    nx ** 2 + ny ** 2
)

print()
print("Normal Vector Check")
print("-" * 50)

print(
    f"Maximum | ||N|| - 1 | = "
    f"{np.max(np.abs(normal_length - 1)):.6e}"
)


# ============================================================
# 10. VISUALIZATION
# ============================================================

plt.figure(figsize=(9, 9))

# Astroid
plt.plot(
    x,
    y,
    label="Astroid"
)


# Choose fewer points for clearer arrows
step = 40

# Scale of the displayed vectors
vector_scale = 0.7


# Tangent vectors
plt.quiver(
    x[::step],
    y[::step],
    Tx[::step] * vector_scale,
    Ty[::step] * vector_scale,
    angles="xy",
    scale_units="xy",
    scale=1,
    width=0.003,
    label="Unit tangent"
)


# Inward normal vectors
plt.quiver(
    x[::step],
    y[::step],
    nx[::step] * vector_scale,
    ny[::step] * vector_scale,
    angles="xy",
    scale_units="xy",
    scale=1,
    width=0.003,
    label="Inward unit normal"
)


plt.xlabel("x")
plt.ylabel("y")

plt.title("Astroid Tangent and Normal Fields")

plt.axis("equal")
plt.grid(True)
plt.legend()

plt.show()