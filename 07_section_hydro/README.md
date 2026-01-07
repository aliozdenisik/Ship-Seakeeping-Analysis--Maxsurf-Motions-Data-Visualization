# 07 - Section Hydrodynamic Coefficients

## Overview

This module generates plots for **sectional (2D) hydrodynamic coefficients** computed using Strip Theory. These represent the per-unit-length hydrodynamic properties of each hull cross-section.

## Theory

### Strip Theory Methodology

Strip theory (Salvesen, Tuck & Faltinsen, 1970) divides the hull into 2D slices and calculates:

1. **Added Mass (aᵢⱼ)** - Hydrodynamic inertia of water accelerated with the hull
2. **Damping (bᵢⱼ)** - Energy dissipation through wave radiation
3. **Stiffness (cᵢⱼ)** - Hydrostatic restoring forces
4. **Wave Excitation Forces** - Forces from incident waves

### Wave Excitation Components

- **Froude-Krylov Force** - Pressure integration of undisturbed incident wave
- **Diffraction Force** - Wave scattering by the body

## Scripts

| File | Description |
|------|-------------|
| `section_hydro_plot.py` | Multi-panel coefficient visualization |
| `section_hydro_academic.py` | Publication-quality academic format |
| `process_hydro_data.py` | Alternative data processing script |
| `Figure_Captions.md` | Academic figure captions for publication |

## Output Folders

- `output/beam_seas/` - 90° wave heading results
- `output/head_seas/` - 180° wave heading results

## Generated Figures

1. **Fig 1** - Added Mass & Damping (2-panel)
2. **Fig 2** - Wave Excitation Forces (4-panel: FK amp, D amp, FK phase, D phase)
3. **Fig 3** - FK vs Diffraction comparison (overlay)
4. **Fig 4** - Complete coefficient summary (6-panel)
5. **Fig 5** - Combined dual-axis plot
6. **Fig 6** - Excitation amplitude with markers

## Coefficient Notation

| Symbol | Description | Unit |
|--------|-------------|------|
| a₃₃ | Sectional added mass (heave) | t/m |
| b₃₃ | Sectional damping (heave) | t/(m·s) |
| c₃₃ | Sectional stiffness (heave) | t/(m·s²) |
| F_FK | Froude-Krylov force amplitude | kN/m² |
| F_D | Diffraction force amplitude | kN/m² |
| φ | Phase angle | deg |

## References

- Salvesen, N., Tuck, E.O., & Faltinsen, O. (1970). Ship motions and sea loads. SNAME Trans., Vol. 78, pp. 250-287.
