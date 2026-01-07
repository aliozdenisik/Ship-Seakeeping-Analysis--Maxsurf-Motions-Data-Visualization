# 08 - Global Hydrodynamic Coefficients

## Overview

This module generates plots for **global (integrated) hydrodynamic coefficients** representing the entire vessel's hydrodynamic behavior.

## Theory

Global coefficients are obtained by integrating sectional values along the ship length:

```
A₃₃ = ∫ a₃₃(x) dx    (Total added mass)
B₃₃ = ∫ b₃₃(x) dx    (Total damping)
```

## Coupling Effects

The heave-pitch coupled equations of motion include:

- A₃₃, A₃₅ - Added mass (heave, heave-pitch coupling)
- A₅₃, A₅₅ - Added mass (pitch-heave coupling, pitch)
- B₃₃, B₃₅, B₅₃, B₅₅ - Damping coefficients
- C₃₃, C₃₅, C₅₃, C₅₅ - Stiffness coefficients

## Input Data

- `hydro_data.txt` - Global coefficient values vs frequency

## Generated Figures

- **Subplot Layout** - Mode 3 (Heave) and Mode 5 (Pitch) excitation
- **Dual-Axis Plot** - Force and moment on same figure

## Output Files

- `academic_plot_subplots.png` - Stacked heave/pitch plots
- `academic_plot_dual.png` - Combined dual-axis view

## Key Parameters

| Mode | Description | Unit |
|------|-------------|------|
| Mode 3 | Heave excitation force | kN/m |
| Mode 5 | Pitch excitation moment | kNm/m |

## Usage

```bash
python plot_hydro.py
```

## References

- Newman, J.N. (1977). Marine Hydrodynamics. MIT Press.
- Faltinsen, O.M. (1990). Sea Loads on Ships and Offshore Structures. Cambridge University Press.
