# 04 - Remote Location RAOs

## Overview

This module generates RAO plots at a **remote location** (crew compartment) rather than the center of gravity. This is critical for comfort assessment at specific locations on the vessel.

## Theory

Remote location motions combine CG motions with rotational contributions:

```
η_remote = η_CG + r × θ
```

where:

- η_remote = motion at remote location
- η_CG = motion at center of gravity
- r = position vector from CG to remote location
- θ = rotational motion vector

## Remote Location Definition

| Parameter | Value |
|-----------|-------|
| Location | Officer Cabin (Port) |
| x-offset | Forward from CG |
| y-offset | Port side offset |
| z-offset | Above waterline |

## Generated Plots

- **Longitudinal RAO** - Surge motion transfer function
- **Lateral RAO** - Sway motion transfer function
- **Vertical RAO** - Combined heave + pitch contribution
- **Roll RAO** - Roll angle transfer function
- **Pitch RAO** - Pitch angle transfer function

## Output Files

- `rao_plot_dataset1.png` - Combined RAO plot
- `rao_dataset1_subplots.png` - Individual RAO panels

## Usage

Modify `DATA_STRING_1` in the script to input different remote location data from Maxsurf.
