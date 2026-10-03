# ASTROID-X
## Mathematical Framework

---

# 1. Introduction

The astroid is a four-cusped algebraic curve with several equivalent
mathematical representations.

It can be studied as:

- a parametric curve,
- an implicit algebraic curve,
- a polar curve,
- a hypocycloid,
- and an envelope of line segment
The purpose of this document is to establish the mathematical
framework that will later be implemented computationally in ASTROID-X.

The central standard astroid is defined using a positive scale
parameter `a`.

---

# 2. Geometric Origin

The astroid can be generated as a hypocycloid.

Consider a circle of radius `a/4` rolling without slipping inside a
fixed circle of radius `a`.

Since

    a / (a/4) = 4,

the resulting hypocycloid contains four cusps.

The four cusp points are

    (a, 0)
    (0, a)
    (-a, 0)
    (0, -a)

This immediately establishes the characteristic four-fold symmetry of
the astroid.

The hypocycloid interpretation is important because it gives a
geometric explanation for the shape rather than treating the equation
as an arbitrary formula.

---

# 3. Parametric Representation

The standard parametric representation of the astroid is

    x(t) = a cos^3(t)
    y(t) = a sin^3(t)

where

    0 <= t < 2π.

Here `t` acts as a parameter describing the position of a point as it
moves around the curve.

The scale parameter `a` controls the overall size of the astroid.

For `a > 0`, the maximum absolute values of both coordinates are `a`.

---

# 4. Important Parameter Values

Several parameter values correspond directly to the cusp points.

For `t = 0`:

    x = a
    y = 0

giving

    (a, 0).

For `t = π/2`:

    x = 0
    y = a

giving

    (0, a).

For `t = π`:

    x = -a
    y = 0

giving

    (-a, 0).

For `t = 3π/2`:

    x = 0
    y = -a

giving

    (0, -a).

These points will later be used to verify symmetry, extrema, and
singular behavior computationally.

---

# 5. Derivation of the Implicit Equation

Starting from the parametric equations,

    x = a cos^3(t)

and

    y = a sin^3(t),

divide by `a`:

    x/a = cos^3(t)
    y/a = sin^3(t).

Taking the power `2/3` gives

    |x/a|^(2/3) = cos^2(t)

and

    |y/a|^(2/3) = sin^2(t).

Adding the two equations gives

    |x/a|^(2/3) + |y/a|^(2/3)
    = cos^2(t) + sin^2(t).

Using the identity

    cos^2(t) + sin^2(t) = 1,

we obtain

    |x/a|^(2/3) + |y/a|^(2/3) = 1.

Therefore the implicit equation is

    |x|^(2/3) + |y|^(2/3) = a^(2/3).

Equivalently,

    |x|^(2/3) / a^(2/3)
    +
    |y|^(2/3) / a^(2/3)
    = 1.

This establishes the equivalence between the parametric and implicit
representations.

---

# 6. Why the Parametric Representation Is Important Computationally

The parametric representation provides a direct mechanism for
sampling the curve.

Given a collection of parameter values

    t_1, t_2, ..., t_n,

the corresponding coordinates are calculated using

    x_i = a cos^3(t_i)
    y_i = a sin^3(t_i).

This makes the representation particularly useful for:

- plotting the curve,
- numerical differentiation,
- tangent calculations,
- normal calculations,
- curvature calculations,
- arc-length calculations,
- numerical area estimation,
- and local cusp analysis.

Therefore the parametric representation will form the computational
foundation of ASTROID-X.

---

# 7. First Computational Validation

One of the first experiments will test whether points generated from
the parametric equations satisfy the implicit equation.

For each sampled value of `t`, calculate

    x = a cos^3(t)
    y = a sin^3(t)

and evaluate

    F(x, y)
    =
    |x|^(2/3) + |y|^(2/3) - a^(2/3).

For an exact mathematical calculation,

    F(x, y) = 0.

In numerical computation, floating-point arithmetic may produce a small
non-zero value.

Therefore the computational validation will examine the magnitude of

    |F(x, y)|

rather than expecting exact machine zero.

This experiment will establish the numerical consistency between the
two representations.

---

# 8. Connection to Generalized Curves

The astroid can be viewed as a special member of the generalized
family

    |x/a|^p + |y/b|^p = 1.

The astroid corresponds to

    p = 2/3

with

    a = b.

This provides a natural direction for later experiments.

By changing `p`, ASTROID-X will investigate how the geometry of the
curve changes.

The generalized family will be studied only after the fundamental
properties of the standard astroid have been established.

---

# 9. Mathematical Investigation Pipeline

The mathematical analysis will follow the sequence

    Parametric Representation
            ↓
    Implicit Representation
            ↓
    Symmetry
            ↓
    Derivatives
            ↓
    Tangents and Normals
            ↓
    Concavity
            ↓
    Curvature
            ↓
    Arc Length
            ↓
    Area
            ↓
    Singularities and Cusps
            ↓
    Algebraic Structure
            ↓
    Generalized Curves

Each stage will be derived mathematically before being implemented
computationally.

---

# 10. Key Principle

ASTROID-X will not treat visualization as the final objective.

The computational workflow is

    Mathematical Theory
            ↓
    Analytical Derivation
            ↓
    Numerical Implementation
            ↓
    Visualization
            ↓
    Validation
            ↓
    Interpretation

---

# 11. Differential Structure

The parametric representation

    x(t) = a cos^3(t)
    y(t) = a sin^3(t)

allows the differential properties of the astroid to be derived
directly with respect to the parameter `t`.

---

## 11.1 First Derivatives

Differentiating the x-coordinate gives

    dx/dt = -3a cos^2(t) sin(t).

Differentiating the y-coordinate gives

    dy/dt = 3a sin^2(t) cos(t).

Therefore the velocity vector is

    r'(t)
    =
    (-3a cos^2(t) sin(t),
      3a sin^2(t) cos(t)).

This vector describes the instantaneous direction of motion along the
parametric curve.

---

## 11.2 Tangent Slope

For a parametric curve,

    dy/dx = (dy/dt) / (dx/dt).

Substituting the first derivatives gives

    dy/dx
    =
    [3a sin^2(t) cos(t)]
    /
    [-3a cos^2(t) sin(t)].

After simplification,

    dy/dx = -tan(t).

Therefore the slope of the astroid is directly related to the
parameter.

In the first quadrant,

    0 < t < π/2,

the tangent slope is negative.

As `t` approaches zero,

    dy/dx → 0,

corresponding to a horizontal tangent near `(a, 0)`.

As `t` approaches `π/2`,

    dy/dx → -∞,

corresponding to a vertical tangent near `(0, a)`.

---

## 11.3 Second Derivative

To investigate concavity, differentiate the first derivative with
respect to `t`:

    d/dt(-tan(t)) = -sec^2(t).

For a parametric curve,

    d²y/dx²
    =
    [d/dt(dy/dx)] / (dx/dt).

Therefore,

    d²y/dx²
    =
    [-sec²(t)]
    /
    [-3a cos²(t) sin(t)].

Using

    sec²(t) = 1/cos²(t),

we obtain

    d²y/dx²
    =
    1 / [3a cos^4(t) sin(t)].

For the interior of the first quadrant,

    a > 0,
    sin(t) > 0,
    cos(t) > 0.

Therefore,

    d²y/dx² > 0.

Hence the first-quadrant branch of the astroid is concave upward when
represented as a graph `y(x)`.

---

## 11.4 Concavity and Global Geometry

The sign of the second derivative describes the local concavity of a
branch represented as a function `y(x)`.

It should not be confused with a global classification of the entire
astroid.

The astroid contains four cusp singularities, where the usual smooth
curve analysis breaks down.

Therefore ASTROID-X will distinguish between:

- graph concavity,
- local differential behavior,
- curvature,
- and global geometric properties.

This distinction will become particularly important during the
singularity analysis.

---

## 11.5 Differential Investigation

The differential structure provides the foundation for later
experiments involving:

- tangent fields,
- normal fields,
- curvature,
- radius of curvature,
- cusp detection,
- and local behavior.

The computational workflow will evaluate these quantities for a dense
set of parameter values and compare numerical observations with their
analytical expressions.
---

# 12. Tangent, Normal, and Curvature

The first derivatives provide the fundamental differential structure
needed to investigate the local geometry of the astroid.

---

## 12.1 Tangent Vector

From the parametric representation,

    x(t) = a cos^3(t)
    y(t) = a sin^3(t),

the derivative vector is

    r'(t)
    =
    (-3a cos^2(t) sin(t),
      3a sin^2(t) cos(t)).

This vector is tangent to the curve wherever it is non-zero.

Its direction determines the instantaneous direction of motion along
the astroid.

---

## 12.2 Speed

The magnitude of the derivative vector is

    |r'(t)|
    =
    sqrt((dx/dt)^2 + (dy/dt)^2).

Substitution gives

    |r'(t)|
    =
    3a |sin(t) cos(t)|.

Therefore,

    |r'(t)| = 3a |sin(t) cos(t)|.

The speed becomes zero at

    t = 0,
    π/2,
    π,
    3π/2.

These parameter values correspond exactly to the four cusp points.

Thus the parameterization itself provides an initial indication of
singular behavior at the cusps.

---

## 12.3 Unit Tangent

Away from the cusp points, the unit tangent vector is

    T(t) = r'(t) / |r'(t)|.

In the first quadrant, where both `sin(t)` and `cos(t)` are positive,
this simplifies to

    T(t) = (-cos(t), sin(t)).

The sign convention changes between different quadrants because the
speed contains an absolute value.

The computational implementation will therefore handle the raw tangent
vector globally and normalize it numerically.

---

## 12.4 Normal Direction

A vector perpendicular to a tangent vector

    T = (T_x, T_y)

can be constructed as

    N = (-T_y, T_x).

The normal vector provides the direction in which the curve bends.

The sign of the normal is not unique; both a normal vector and its
negative represent perpendicular directions.

A consistent convention will be selected for visualization.

---

## 12.5 Curvature

For a regular parametric plane curve, curvature is given by

    κ
    =
    |x' y'' - y' x''|
    /
    (x'^2 + y'^2)^(3/2).

For the astroid,

    x' = -3a cos^2(t) sin(t)

and

    y' = 3a sin^2(t) cos(t).

The second derivatives are

    x''
    =
    3a(2 cos(t) sin^2(t) - cos^3(t))

and

    y''
    =
    3a(2 sin(t) cos^2(t) - sin^3(t)).

Substituting into the curvature formula and simplifying gives

    κ(t)
    =
    1 / [3a |sin(t) cos(t)|].

Using

    |sin(2t)| = 2|sin(t) cos(t)|,

this can also be written as

    κ(t)
    =
    2 / [3a |sin(2t)|].

This formula is valid on the smooth portions of the curve.

---

## 12.6 Behavior Near the Cusps

At the four cusp parameters,

    t = 0,
    π/2,
    π,
    3π/2,

the denominator of the curvature expression approaches zero.

Therefore,

    κ(t) → ∞

as the curve approaches a cusp.

This indicates that the curvature becomes unbounded near the singular
points.

The curvature therefore provides a quantitative method for detecting
the exceptional geometry of the cusps.

---

## 12.7 Radius of Curvature

The radius of curvature is defined by

    ρ = 1/κ.

Therefore,

    ρ(t)
    =
    3a |sin(t) cos(t)|

or equivalently,

    ρ(t)
    =
    (3a/2)|sin(2t)|.

Thus,

    κ → ∞

and

    ρ → 0

near the cusp points.

The radius of curvature will later be visualized and compared with
the geometry of the curve.

---

## 12.8 Differential-Geometric Investigation

The tangent, normal, curvature, and radius of curvature will form a
major computational section of ASTROID-X.

The planned workflow is:

    Parametric Curve
          ↓
    First Derivatives
          ↓
    Tangent Vector
          ↓
    Unit Tangent
          ↓
    Normal Direction
          ↓
    Curvature
          ↓
    Radius of Curvature
          ↓
    Behavior Near Cusps

The computational results will be compared with the analytical
expressions derived above.
---

# 13. Center of Curvature and Evolute

The curvature analysis can be extended by determining the center of the
osculating circle at each regular point of the astroid.

---

## 13.1 Osculating Circle

At a smooth point of a curve, the osculating circle is the circle that
locally approximates the curve's bending.

Its radius is the radius of curvature

    ρ = 1/κ.

For the astroid,

    ρ(t)
    =
    3a |sin(t) cos(t)|.

The center of this circle lies along the normal direction from the
point on the curve.

---

## 13.2 Center of Curvature

For a regular parametric curve

    r(t) = (x(t), y(t)),

the center of curvature can be written as

    C(t) = r(t) + ρ(t) N(t),

where `N(t)` is the appropriately oriented unit normal vector.

The exact sign of the normal depends on the orientation convention.

Therefore, when implementing the center of curvature computationally,
the normal direction must be handled consistently.

---

## 13.3 Evolute

The locus of all centers of curvature is called the evolute of the
original curve.

Thus,

    original curve
          ↓
    curvature
          ↓
    centers of curvature
          ↓
       evolute

The evolute provides another way to study how the curvature of the
original curve changes.

---

## 13.4 Astroid Evolute Investigation

For the astroid, the center-of-curvature coordinates can be derived
symbolically from the parametric equations.

The derivation will be performed explicitly rather than relying on a
pre-existing geometric description.

The computational investigation will then compare:

1. the original astroid,
2. numerically calculated centers of curvature,
3. the analytically derived evolute.

This comparison will test whether the numerical construction agrees
with the analytical result.

---

## 13.5 Why the Evolute Matters

The evolute is useful because it converts information about local
curvature into a geometric object.

Instead of plotting curvature only as a scalar function

    κ(t),

we can visualize where the centers of curvature are located.

This provides a geometric interpretation of curvature.

The evolute will therefore be used as a bridge between:

    differential geometry
              ↓
        numerical geometry
              ↓
        visual analysis.

---

## 13.6 Computational Experiment

The future experiment will perform the following steps:

    1. Sample parameter values t.
    2. Calculate points on the astroid.
    3. Calculate tangent vectors.
    4. Calculate unit normals.
    5. Calculate curvature.
    6. Calculate radius of curvature.
    7. Construct centers of curvature.
    8. Plot the centers.
    9. Compare the resulting locus with the analytical evolute.

Special care will be required near the four cusp points because the
astroid is not regular there.

---

## 13.7 Numerical Stability

The curvature contains a denominator involving

    |sin(t) cos(t)|.

Near the cusp parameters this quantity becomes very small.

Consequently, direct numerical calculations can become unstable or
produce very large values.

The implementation will therefore avoid evaluating curvature exactly
at the singular parameter values.

This is an important numerical-analysis principle:

    Mathematical singularity
            +
    finite-precision arithmetic
            =
    potential numerical instability.

The project will explicitly investigate this behavior rather than
hiding it.
---

# 14. Arc Length and Enclosed Area

The astroid provides two important exact geometric quantities that can
be used as validation targets for numerical computation:

- total arc length,
- enclosed area.

These quantities will later be independently approximated using
numerical methods.

---

## 14.1 Arc Length of a Parametric Curve

For a parametric curve

    x = x(t)
    y = y(t),

the arc length over an interval `[t0, t1]` is

    L
    =
    ∫ sqrt((dx/dt)^2 + (dy/dt)^2) dt.

For the astroid,

    x = a cos^3(t)
    y = a sin^3(t).

The derivatives are

    dx/dt = -3a cos^2(t) sin(t)

and

    dy/dt = 3a sin^2(t) cos(t).

Therefore,

    sqrt((dx/dt)^2 + (dy/dt)^2)
    =
    3a |sin(t) cos(t)|.

Thus the complete arc length is

    L
    =
    ∫[0,2π] 3a |sin(t) cos(t)| dt.

---

## 14.2 Using Symmetry

The astroid has four-fold rotational symmetry.

Therefore the arc length of the complete curve can be obtained by
calculating the first-quadrant arc length and multiplying by four.

For

    0 <= t <= π/2,

both sine and cosine are non-negative.

Therefore,

    L
    =
    4 ∫[0,π/2] 3a sin(t) cos(t) dt.

Using

    ∫ sin(t) cos(t) dt
    =
    (1/2) sin^2(t),

we obtain

    L
    =
    12a [(1/2) sin^2(t)] [0,π/2].

Hence,

    L = 6a.

Therefore the exact perimeter of the astroid is

    L = 6a.

This result will later serve as a numerical validation target.

---

## 14.3 Numerical Arc-Length Experiment

The exact result provides a known target for numerical computation.

A numerical experiment will approximate

    L = ∫ |r'(t)| dt

using sampled values of `t`.

The experiment will repeat the approximation using increasing numbers
of sample points.

For example:

    N = 100
    N = 500
    N = 1000
    N = 5000

The numerical values should approach the theoretical result

    L = 6a.

The absolute error will be calculated as

    error = |L_numerical - 6a|.

This creates a convergence experiment rather than a single numerical
calculation.

---

## 14.4 Area of a Parametric Closed Curve

For a closed parametric curve, the signed area can be calculated using

    A
    =
    (1/2)
    |∫[0,2π] (x y' - y x') dt|.

For the astroid,

    x = a cos^3(t)
    y = a sin^3(t),

    x' = -3a cos^2(t) sin(t)

and

    y' = 3a sin^2(t) cos(t).

First,

    x y'
    =
    3a^2 cos^4(t) sin^2(t).

Also,

    y x'
    =
    -3a^2 sin^4(t) cos^2(t).

Therefore,

    x y' - y x'
    =
    3a^2
    [cos^4(t) sin^2(t)
     +
     sin^4(t) cos^2(t)].

Factoring gives

    x y' - y x'
    =
    3a^2 sin^2(t) cos^2(t).

Therefore,

    A
    =
    (3a^2/2)
    ∫[0,2π] sin^2(t) cos^2(t) dt.

Using

    sin^2(t) cos^2(t)
    =
    (1/4) sin^2(2t),

the integral evaluates to

    π/4.

Hence,

    A
    =
    (3a^2/2)(π/4).

Therefore,

    A = 3πa^2/8.

This is the exact enclosed area of the astroid.

---

## 14.5 Numerical Area Experiment

The theoretical result

    A = 3πa^2/8

will be used as a validation target.

The numerical experiment will approximate the parametric area
integral using discrete samples.

The resolution will then be increased and the numerical result will be
compared with the exact value.

The absolute error will be calculated as

    error
    =
    |A_numerical - 3πa^2/8|.

The relative error may also be calculated as

    relative error
    =
    |A_numerical - A_exact| / |A_exact|.

---

## 14.6 Why Arc Length and Area Are Important

Arc length and area provide two different types of numerical
validation.

Arc length depends on the local differential quantity

    |r'(t)|,

while area depends on the global geometry of the closed curve.

Therefore, successfully recovering both values provides evidence that
the computational representation captures both local and global
properties of the astroid.

The planned validation pipeline is:

    Exact Analytical Formula
              ↓
       Numerical Approximation
              ↓
         Error Calculation
              ↓
       Increase Resolution
              ↓
        Convergence Analysis