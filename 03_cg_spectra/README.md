# 03 - CG Motion Response Spectra

## Overview

This module generates **spectral density plots** for ship motions at the center of gravity, showing energy distribution across frequencies.

## Theory

The response spectrum is calculated by:

```
S_r(ωₑ) = |RAO(ωₑ)|² × S_wave(ωₑ)
```

The area under the response spectrum gives the variance (σ²) of the motion:

```
σ² = ∫ S_r(ω) dω
```

## Input Data

- `spectra_data.csv` - Spectral density values for wave, heave, pitch, and added resistance

## Generated Plots

### 4-Panel Academic Layout

- (a) Wave Spectrum - S_wave(ω) in m²/(rad/s)
- (b) Heave Motion Spectrum - S_heave(ωₑ) in m²/(rad/s)
- (c) Pitch Motion Spectrum - S_pitch(ωₑ) in deg²/(rad/s)
- (d) Added Resistance Spectrum - S_Raw(ωₑ) in kN/(rad/s)

### Combined Multi-Axis Plot

All spectra on single figure with multiple y-axes for direct comparison.

## Output Files

- `cg_spectra_academic.png/pdf` - 2×2 subplot layout
- `cg_spectra_combined.png/pdf` - Multi-axis overlay

## Key Insight
>
> The peak of the response spectrum may not coincide with the wave spectrum peak due to RAO resonance effects.

## References

- St. Denis, M., & Pierson, W.J. (1953). On the Motions of Ships in Confused Seas. SNAME Trans.
