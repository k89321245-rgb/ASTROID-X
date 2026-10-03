# ASTROID-X

## Computational Investigation of the Astroid Curve

ASTROID-X is a research-oriented computational mathematics project
focused on the geometric, analytical, differential, numerical, and
singularity properties of the classical astroid curve.

The project combines mathematical derivation with Python-based
experimentation, visualization, numerical validation, and
generalization.

The central mathematical object is the astroid

\[
x=a\cos^3(t),
\qquad
y=a\sin^3(t),
\]

which is equivalent to the Cartesian representation

\[
|x|^{2/3}+|y|^{2/3}=a^{2/3}.
\]

Rather than treating the astroid as only a plotting problem,
ASTROID-X investigates how its mathematical properties emerge from
different representations and how those properties can be verified
computationally.

---

## Research Question

> How does the astroid behave geometrically, analytically,
> differentially, and locally near its singularities, and how can
> those properties be verified through computational experiments and
> graphical analysis?

A secondary objective is to investigate how these properties change
when the astroid is generalized into the family

\[
\left|\frac{x}{a}\right|^p+
\left|\frac{y}{a}\right|^p=1.
\]

---

## Core Research Philosophy

ASTROID-X follows the methodology

\[
\boxed{
\text{Theory}
\rightarrow
\text{Derivation}
\rightarrow
\text{Computation}
\rightarrow
\text{Visualization}
\rightarrow
\text{Validation}
\rightarrow
\text{Interpretation}
}
\]

Every major computational result is connected to a mathematical
expression or theoretical expectation.

The goal is therefore not simply to generate graphs, but to establish
a reproducible connection between mathematical theory and numerical
evidence.

---

## Project Objectives

ASTROID-X is designed to investigate the astroid through a sequence of
connected computational experiments.

The main objectives are:

- Verify the consistency of different mathematical representations.
- Analyze the global geometry and symmetry of the astroid.
- Derive and investigate tangent and normal behavior.
- Study concavity and curvature across the curve.
- Analyze the radius of curvature and evolute.
- Numerically validate perimeter and enclosed area.
- Investigate the local structure of the cusp singularities.
- Verify singular points using the implicit algebraic representation.
- Study radial behavior and geometric bounds.
- Investigate generalized curves controlled by the exponent \(p\).
- Compare measurable geometric properties across the generalized
  family.
- Establish a reproducible computational research methodology.

The project is organized so that each experiment has a mathematical
expectation, a computational implementation, a numerical result, and
a research interpretation.
---

## Mathematical Foundation

The standard astroid is represented parametrically by

\[
x=a\cos^3(t),
\qquad
y=a\sin^3(t),
\qquad
0\leq t<2\pi.
\]

Its Cartesian representation is

\[
|x|^{2/3}+|y|^{2/3}=a^{2/3}.
\]

The project also investigates its implicit algebraic form

\[
(x^2+y^2-a^2)^3+27a^2x^2y^2=0.
\]

Several important geometric quantities are derived from the
parametric representation.

### Tangent Slope

\[
\frac{dy}{dx}=-\tan(t).
\]

### Curvature

\[
\kappa(t)
=
\frac{1}{
3a|\sin(t)\cos(t)|
}.
\]

### Radius of Curvature

\[
\rho(t)
=
3a|\sin(t)\cos(t)|.
\]

### Arc Length

\[
L=6a.
\]

### Enclosed Area

\[
A=\frac{3\pi a^2}{8}.
\]

### Radial Distance

\[
r(t)
=
a\sqrt{
1-\frac34\sin^2(2t)
}.
\]

Therefore,

\[
\frac{a}{2}\leq r\leq a.
\]

### Local Cusp Behavior

Near the cusp \((a,0)\),

\[
|y|
\sim
\sqrt{\frac{8}{27a}}
(a-x)^{3/2}.
\]

This gives the characteristic semicubical scaling of the astroid
cusp.

### Generalized Family

ASTROID-X also investigates

\[
\left|\frac{x}{a}\right|^p+
\left|\frac{y}{a}\right|^p=1,
\]

with the standard astroid corresponding to

\[
p=\frac23.
\]

This generalized representation allows the effect of the exponent
\(p\) on geometric properties to be investigated computationally.
---

## Experimental Framework

ASTROID-X contains eighteen computational experiments organized into
five research stages.

### Stage I — Geometric Structure

| Experiment | Investigation |
|---|---|
| E01 | Parametric representation vs Cartesian equation |
| E02 | Symmetry analysis |
| E03 | Extrema and coordinate intercepts |

### Stage II — Differential Geometry

| Experiment | Investigation |
|---|---|
| E04 | Tangent and slope behavior |
| E05 | Concavity |
| E06 | Curvature |
| E07 | Curvature variation |
| E08 | Radius of curvature |
| E09 | Evolute |

### Stage III — Numerical Validation

| Experiment | Investigation |
|---|---|
| E10 | Arc-length numerical convergence |
| E11 | Area numerical convergence |

### Stage IV — Singularity and Local Analysis

| Experiment | Investigation |
|---|---|
| E12 | Cusp local behavior |
| E13 | Cusp scaling and convergence |
| E14 | Radial distance behavior |
| E15 | Normal behavior |
| E16 | Algebraic singularities |

### Stage V — Generalization

| Experiment | Investigation |
|---|---|
| E17 | Generalized exponent analysis |
| E18 | Generalized curve comparison |

The experiments are intentionally connected rather than independent.
Results from earlier stages provide the mathematical foundation for
later investigations.

The overall experimental progression is

\[
\boxed{
\text{Geometry}
\rightarrow
\text{Differential Geometry}
\rightarrow
\text{Numerical Validation}
\rightarrow
\text{Singularities}
\rightarrow
\text{Generalization}
}
\]
---

## Project Structure

```text
ASTROID-X/
│
├── README.md
│
├── research/
│   ├── research_plan.md
│   ├── mathematical_framework.md
│   └── results_analysis.md
│
├── experiments/
│   ├── cusp_analysis.py
│   ├── cusp_scaling.py
│   ├── radial_behavior.py
│   ├── normal_behavior.py
│   ├── algebraic_singularities.py
│   ├── generalized_exponent.py
│   └── generalized_comparison.py
│
├── src/
│   └── ...
│
├── results/
│   ├── geometry/
│   ├── differential_geometry/
│   ├── numerical_analysis/
│   ├── singularities/
│   └── generalization/
│
├── tests/
│   └── ...
│
└── .gitignore

---

## Technology Stack

ASTROID-X is implemented using a scientific Python environment
designed for numerical computation, mathematical analysis, and
visualization.

### Programming Language

- **Python 3.14.7**

### Scientific Computing

- **NumPy** — numerical arrays, parameter sampling, and vectorized mathematical computation
- **SciPy** — numerical integration and computational validation
- **SymPy** — symbolic mathematics and algebraic verification

### Visualization

- **Matplotlib** — curve visualization, parameter analysis, convergence plots, and research figures

### Development Environment

- **Visual Studio Code**
- **Python virtual environment (`.venv`)**
- **Git / GitHub** for version control and project documentation

### Computational Approach

The project uses a combination of:

- Vectorized numerical computation
- Numerical integration
- Symbolic/algebraic verification
- Parametric curve generation
- Differential-geometric calculations
- Numerical convergence analysis
- Graphical visualization
- Local asymptotic analysis

The computational environment is isolated using a Python virtual
environment so that experiments can be reproduced independently of the
system-wide Python installation.
---

## Reproducibility

ASTROID-X is structured so that the computational experiments can be
reproduced from a clean Python environment.

### Environment Setup

The project uses a dedicated Python virtual environment:

```text
.venv/
---

## Key Results

The computational experiments produced numerical results that agree
closely with the theoretical properties of the astroid.

### Geometric and Differential Results

- The parametric representation was verified against the Cartesian
  representation of the astroid.
- The expected four-fold symmetry and coordinate intercepts were
  confirmed computationally.
- The tangent slope was verified as

\[
\frac{dy}{dx}=-\tan(t).
\]

- The curvature was found to follow

\[
\kappa(t)
=
\frac{1}{3a|\sin(t)\cos(t)|},
\]

with curvature increasing without bound near the cusp locations.
- The radius of curvature approaches zero near the cusps.
- The normal vector was numerically verified to be perpendicular to
  the tangent vector, with floating-point error on the order of
  \(10^{-16}\).

### Numerical Validation

The theoretical perimeter and enclosed area were investigated through
numerical convergence experiments.

The theoretical values are

\[
L=6a
\]

and

\[
A=\frac{3\pi a^2}{8}.
\]

The numerical experiments showed convergence toward these analytical
values as the computational resolution increased.

### Cusp Analysis

The local structure of the cusp at \((a,0)\) was investigated
numerically.

The theoretical scaling is

\[
|y|
\sim
\sqrt{\frac{8}{27a}}
(a-x)^{3/2}.
\]

The estimated scaling exponent converged toward

\[
1.5
\]

as the computational neighborhood around the cusp was reduced.

For example, the E13 experiment produced:

| Zoom Range | Estimated Exponent |
|---:|---:|
| 0.500 | 1.510479 |
| 0.250 | 1.502631 |
| 0.100 | 1.500421 |
| 0.050 | 1.500111 |
| 0.025 | 1.500028 |

This provides numerical evidence for the theoretical semicubical cusp
behavior.

### Algebraic Singularity Verification

Using the implicit algebraic representation,

\[
F(x,y)
=
(x^2+y^2-a^2)^3+27a^2x^2y^2,
\]

all four cusp points were verified to satisfy

\[
F(x,y)=0
\]

and

\[
\nabla F(x,y)=0.
\]

This confirms the singular nature of the four cusp locations within
the algebraic representation.

### Radial Behavior

For the standard astroid,

\[
r(t)
=
a\sqrt{
1-\frac34\sin^2(2t)
}.
\]

The computational experiment confirmed

\[
\frac{a}{2}\leq r\leq a.
\]

For \(a=5\),

\[
r_{\min}\approx2.500002,
\qquad
r_{\max}=5.000000,
\]

with the minimum occurring near

\[
t=\frac{\pi}{4}.
\]

### Generalized Curve Family

The generalized family

\[
\left|\frac{x}{a}\right|^p+
\left|\frac{y}{a}\right|^p=1
\]

was investigated for several values of \(p\).

For \(a=5\), the analytical area changes as follows:

| \(p\) | Area |
|---:|---:|
| 0.5 | 16.666667 |
| \(2/3\) | 29.452431 |
| 1.0 | 50.000000 |
| 1.5 | 68.446341 |
| 2.0 | 78.539816 |
| 3.0 | 88.331938 |

The standard astroid corresponds to

\[
p=\frac23,
\]

for which the computed area agrees with

\[
\frac{3\pi a^2}{8}.
\]

The generalized experiments demonstrate that changing the exponent
changes the geometry and measurable properties of the curve.
---

## Future Research Directions

The current version of ASTROID-X establishes a computational framework
for investigating the geometry, differential structure, singularities,
and generalized forms of the astroid.

Several directions can extend the investigation further.

### 1. Higher-Resolution Numerical Analysis

Increase numerical resolution and investigate how discretization,
floating-point precision, and sampling density affect the accuracy of
geometric measurements.

Possible investigations include:

- Higher-order numerical integration
- Error convergence rates
- Floating-point sensitivity
- Adaptive sampling near singularities

### 2. More Detailed Singularity Analysis

The cusp investigation can be extended to study local behavior using
additional numerical and symbolic techniques.

Possible directions include:

- Higher-order local expansions
- Comparison of cusp scaling across different representations
- Numerical detection of singular points
- Local geometric measurements near each cusp

### 3. Generalized Curve Geometry

The generalized family

\[
\left|\frac{x}{a}\right|^p+
\left|\frac{y}{a}\right|^p=1
\]

can be investigated in greater detail.

Future experiments could compare:

- Curvature distributions
- Radius of curvature
- Perimeter
- Enclosed area
- Radial distance
- Singular behavior
- Transition of geometric shape with \(p\)

### 4. Automated Mathematical Validation

The project could be extended so that mathematical identities are
automatically tested against numerical implementations.

For example:

\[
\text{Theory}
\longleftrightarrow
\text{Symbolic Derivation}
\longleftrightarrow
\text{Numerical Experiment}.
\]

This would reduce manual verification and provide a more systematic
validation pipeline.

### 5. Interactive Visualization

The existing static research figures could be extended into interactive
visualizations where parameters such as \(a\), \(p\), and \(t\) can be
changed dynamically.

This could allow users to observe:

- Curve deformation
- Tangent and normal movement
- Curvature variation
- Cusp behavior
- Changes across the generalized family

### 6. Extended Curve Families

The generalized superellipse-type family can serve as a starting point
for investigating other parameterized algebraic and parametric curves.

The same computational methodology could then be applied to compare
their:

- Geometry
- Differential properties
- Singularities
- Numerical behavior
- Mathematical representations

The long-term objective is to develop ASTROID-X from a focused
computational study of one classical curve into a reusable methodology
for computational investigation of parameterized curves.
---

## Project Status

**Current Status: Research Core Complete**

ASTROID-X currently contains:

- A complete mathematical research framework.
- Eighteen computational experiments.
- Numerical validation of key theoretical properties.
- Differential-geometric analysis.
- Local cusp and singularity analysis.
- Generalized exponent analysis.
- Detailed research documentation.
- Cross-experiment interpretation.
- A reproducible Python-based computational environment.

The core investigation has been completed, while the project remains
open for further numerical, symbolic, and visualization-based
extensions.

---

## Conclusion

ASTROID-X demonstrates how a classical mathematical curve can be
investigated through a combination of analytical mathematics and
computational experimentation.

The project moves systematically from mathematical theory to
derivation, implementation, numerical measurement, visualization,
validation, and interpretation.

The astroid is therefore treated not simply as a geometric object to
plot, but as a mathematical system whose properties can be examined
through multiple complementary representations.

The investigation connects:

\[
\boxed{
\text{Theory}
\rightarrow
\text{Derivation}
\rightarrow
\text{Computation}
\rightarrow
\text{Visualization}
\rightarrow
\text{Validation}
\rightarrow
\text{Interpretation}
}
\]

This methodology forms the central idea of ASTROID-X and provides a
foundation for extending the same computational approach to other
parameterized mathematical curves.

---

## Author

**ASTROID-X — Computational Mathematics Research Project**

Built using Python, numerical computation, mathematical analysis, and
scientific visualization.