"""
ASTROID-X
Experiment E17: Generalized Exponent p

Purpose:
    Investigate how changing the exponent p changes the
    geometry of the generalized superellipse family.

Family:

    |x/a|^p + |y/a|^p = 1

The astroid corresponds to:

    p = 2/3

Special cases:

    p = 1  -> diamond
    p = 2  -> circle
"""

import numpy as np
import matplotlib.pyplot as plt


a = 5.0

p_values = [
    0.5,
    2 / 3,
    1.0,
    1.5,
    2.0,
    3.0
]


theta = np.linspace(
    0,
    2 * np.pi,
    2000
)


plt.figure(figsize=(10, 10))


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

    plt.plot(
        x,
        y,
        label=f"p = {p:.3f}"
    )


plt.xlabel("x")
plt.ylabel("y")

plt.title(
    "Generalized Astroid Family: "
    "Effect of Exponent p"
)

plt.axis("equal")
plt.grid(True)
plt.legend()

plt.show()


print("ASTROID-X")
print("Experiment E17: Generalized Exponent p")
print("=" * 55)

print(f"Scale parameter a = {a}")

print()
print("Exponent values investigated")
print("-" * 55)

for p in p_values:

    print(f"p = {p:.6f}")

print()
print("Special cases")
print("-" * 55)

print("p = 2/3  -> Astroid")
print("p = 1    -> Diamond")
print("p = 2    -> Circle")
print("p > 2    -> Square-like superellipse")