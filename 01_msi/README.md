# 01 - Motion Sickness Incidence (MSI) Analysis

## Overview

This module evaluates passenger and crew comfort by comparing vertical acceleration responses against **ISO 2631** severe discomfort boundaries.

## Theory

Motion Sickness Incidence (MSI) quantifies the percentage of occupants likely to experience motion sickness after exposure to oscillatory motion. The analysis uses encounter frequency-based acceleration spectra and compares them against standardized comfort limits.

## Input Data

- `MSI.xlsx` - Excel workbook with sheets for each wave heading angle (90°, 180°)
- Each sheet contains encounter frequency and corresponding acceleration values

## Output Figures

- `MSI_Graph_90deg.png` - Beam seas comfort assessment
- `MSI_Graph_180deg.png` - Head seas comfort assessment

## Key Parameters

| Parameter | Description |
|-----------|-------------|
| Exposure Time | 30 min, 2 hrs, 8 hrs limits |
| Location | Officer Cabin (Port side) |
| Motion | Vertical acceleration |

## References

- ISO 2631-1:1997 - Mechanical vibration and shock evaluation
