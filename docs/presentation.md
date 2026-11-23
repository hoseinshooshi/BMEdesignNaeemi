# Presentation outline

## Slide 1 — Problem
Why conventional one-size-fits-all orthoses can be inefficient for individual anthropometry.

## Slide 2 — Why computational design?
Python allows repeatable parameter changes, automation and rapid design iteration.

## Slide 3 — Inputs
Hand length, hand breadth, wrist circumference, forearm length and forearm circumference.

## Slide 4 — Design pipeline
Anthropometry → Python calculations → parametric geometry → STL → engineering metrics.

## Slide 5 — Parametric geometry
Changing measurements or wall thickness automatically changes the generated model.

## Slide 6 — Ventilation
Perforation/lattice patterns can reduce material and improve ventilation; this repository currently keeps the pattern interface ready for a robust boolean/lattice implementation.

## Slide 7 — Machine learning
ML can estimate a missing anthropometric dimension. It is a supporting component, not a replacement for measurement.

## Slide 8 — Results
Compare variants using volume, estimated mass, surface area and open-area ratio once perforation geometry is enabled.

## Slide 9 — Limitations
Simplified anatomy, synthetic ML demonstration data, no clinical validation and no mechanical/FEA validation.

## Slide 10 — Future work
Patient-specific 3D scan, real anthropometric datasets, lattice optimization, FEA and additive-manufacturing constraints.
