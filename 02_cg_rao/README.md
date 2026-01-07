# 02 - CG Response Amplitude Operators (RAOs)

## Overview

This module generates **Response Amplitude Operator** plots at the vessel's center of gravity. RAOs represent the transfer function between wave amplitude and motion response.

## Theory

The RAO (also called transfer function) is defined as:

```
|H(ω)|² = |η(ω) / ζ(ω)|²
```

where:

- η(ω) = motion response amplitude
- ζ(ω) = wave amplitude
- ω = encounter frequency

## Generated Plots

- **Heave RAO** - Vertical displacement per unit wave amplitude (η₃/ζₐ)
- **Pitch RAO** - Angular displacement per unit wave amplitude (η₅/ζₐ)
- **Roll RAO** - Roll angle per unit wave amplitude (η₄/ζₐ)
- **Added Resistance** - Mean resistance increase in waves

## Output Files

- `rao_grafik.png` - Combined RAO plot with dual axes
- `rao_grafik.pdf` - Vector format for publication

## Academic Usage

RAOs are fundamental for spectral analysis:

```
S_response(ωₑ) = |H(ωₑ)|² × S_wave(ωₑ)
```

## References

- Salvesen, N., Tuck, E.O., & Faltinsen, O. (1970). Ship motions and sea loads. SNAME Trans.
