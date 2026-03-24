# Astrophysics and Cosmology

Computational models exploring fundamental concepts in astrophysics and cosmology through simulation and visualization.

## Overview

This repository contains projects focused on black hole physics and solar physics, combining theoretical relations with numerical modeling to produce interpretable physical insights.

**Stack:** Python, Numpy, Matplotlib, SciPy, Astropy, SunPy

## Project Areas

### Solar Physics

1. **Blackbody Radiation and Solar Intensity**
Models Planck spectral radiance and Stefan-Boltzmann flux for the quiet Sun, penumbra, and umbra. Quantifies why sunspots appear dark: a temperature drop from 5778 K to 3800 K reduces emitted flux by ~81% via the T⁴ dependence.  

2. **Solar EUV Imaging and Region Extraction**
Python model using SunPy and Astropy to visualize solar EUV imagery (AIA 171 Å), extracting and plotting a region of interest from full-disk observations using helioprojective coordinates, enabling localized analysis of solar structures.

`See Solar-Physics/`

### Black Holes

1. **Black Hole Thermodynamics**
Visualizes Hawking temperature (T ∝ 1/M), horizon area (A ∝ M²), and Bekenstein-Hawking entropy (S ∝ M²) for Schwarzschild black holes across stellar-mass to supermassive scales.

`See Black-Holes/`

## Notes

All models assume idealized conditions to isolate core physical behavior.
