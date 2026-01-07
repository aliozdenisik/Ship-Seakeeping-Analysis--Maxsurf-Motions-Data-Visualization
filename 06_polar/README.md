# 06 - Polar Diagrams

## Overview

This module generates **polar plots** showing motion RMS values as a function of wave heading angle. These diagrams provide a comprehensive view of directional seakeeping performance.

## Theory

Polar diagrams display how ship motion statistics vary with wave heading:

- 0° = Following seas (waves from stern)
- 90° = Beam seas (waves from side)
- 180° = Head seas (waves from bow)

## Motion Parameters

The script can generate polar plots for:

- RMS Heave motion (m)
- RMS Heave velocity (m/s)
- RMS Heave acceleration (m/s²)
- RMS Pitch motion (deg)
- RMS Pitch velocity (deg/s)
- RMS Pitch acceleration (deg/s²)
- Added resistance (kN)

## Input Data

Data is defined directly in the script:

```python
wave_heading_deg = np.array([0, 30, 60, 90, 120, 150, 180])
rms_values = np.array([...])  # Corresponding RMS values
```

## Output Files

- `polar_rms_heave_motion.png`
- `polar_rms_heave_velocity.png`
- `polar_rms_heave_acceleration.png`
- `polar_rms_pitch_motion.png`
- `polar_rms_pitch_velocity.png`
- `polar_rms_pitch_acceleration.png`
- `polar_added_resistance.png`

## Interpretation

- Larger radial values indicate higher motion at that heading
- Beam seas (90°) typically show maximum roll
- Head/following seas (0°/180°) typically show maximum pitch
