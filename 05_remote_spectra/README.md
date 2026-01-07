# 05 - Remote Location Spectra

## Overview

This module generates **response spectra** at a designated remote location (crew compartment), enabling comfort and operability assessment at specific vessel positions.

## Theory

Remote location spectra combine multiple motion components:

- Vertical displacement spectrum
- Vertical velocity spectrum  
- Vertical acceleration spectrum
- Relative motion spectra (for slamming assessment)

## Input Data

- `data.txt` - Tab-separated spectral density values

## Generated Plots

### Main Multi-Axis Plot

Combined view with separate y-axes for:

- Wave spectrum (m²/(rad/s))
- Linear motion spectrum (m²/(rad/s))
- Velocity spectrum ((m/s)²/(rad/s))
- Acceleration spectrum ((m/s²)²/(rad/s))

### Subplot Layout  

Individual panels for each spectral component:

- S Wave
- S V.Disp (Vertical Displacement)
- S V.Vel (Vertical Velocity)
- S V.Accel (Vertical Acceleration)
- S V.Rel Disp (Relative Displacement)
- S V.Rel Vel (Relative Velocity)
- S V.Rel Accel (Relative Acceleration)

## Output Files

- `remote_spectra_main.png` - Multi-axis combined plot
- `remote_spectra_subplots.png` - 7-panel individual view

## Applications

- Crew comfort assessment
- Helicopter landing operability
- Relative bow motion for slamming prediction
