# Methodology

## 1. Input

The model accepts hand length, hand breadth, wrist circumference, forearm length and forearm circumference.

## 2. Parametric design

The measurements are converted into elliptical cross-sections. These cross-sections are interpolated along the longitudinal axis to create a tapered shell. Wall thickness is a direct design parameter.

This is intentionally a simplified computational representation rather than a clinical anatomical fit.

## 3. Engineering metrics

For a mesh with volume V and material density rho:

m = rho V

When V is expressed in cm³ and rho in g/cm³, the resulting mass is in grams.

## 4. Design comparison

The same anthropometric input can be used to generate multiple design variants by changing thickness and ventilation pattern parameters. A future extension can implement actual boolean perforations or lattice cells and compare open-area ratio and structural performance.

## 5. Machine learning

ML is positioned upstream of geometry generation: when one anthropometric measurement is missing, a trained regression model can estimate it from other measurements. The demonstration model in this repository uses synthetic data only. A research version should use an appropriate public anthropometric dataset, such as ANSUR II, and report train/test metrics and population limitations.
