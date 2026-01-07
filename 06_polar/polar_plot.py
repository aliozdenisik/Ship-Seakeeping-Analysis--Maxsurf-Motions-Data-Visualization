#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Polar Diagram Visualization for Ship Motion Response

Generates polar plots showing RMS motion values as a function of wave heading angle.
Useful for visualizing directional seakeeping performance characteristics.

Data source: Maxsurf Motions summary table
Motion parameter: RMS Pitch acceleration (configurable)

Author: Ali Özden Işık
Institution: Istanbul Technical University - Naval Architecture and Marine Engineering
"""

import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# DATA INPUT
# =============================================================================

# Wave heading angles (degrees) and corresponding RMS values
wave_heading_deg = np.array([0, 30, 60, 90, 120, 150, 180])
rms_values = np.array([0.002752, 0.001787, 0.002782, 0.002648, 0.006373, 0.003533, 0.003095])

# Motion parameter label (modify as needed for different parameters)
motion_label = 'RMS Pitch Acceleration'
motion_unit = 'rad/s²'

# =============================================================================
# POLAR PLOT GENERATION
# =============================================================================

# Convert degrees to radians
wave_heading_rad = np.deg2rad(wave_heading_deg)

# Create polar figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Plot data
ax.plot(wave_heading_rad, rms_values, 'bo-', linewidth=2, markersize=8, label='Measured Values')

# Configure polar plot
ax.set_theta_zero_location('N')  # 0 degrees at top (head seas)
ax.set_theta_direction(-1)       # Clockwise direction
ax.set_title(f'{motion_label}', pad=20, fontsize=14, fontweight='bold')
ax.set_xlabel('Wave Heading Angle (deg)', fontsize=11)
ax.set_ylabel(f'{motion_label} ({motion_unit})', fontsize=11, labelpad=30)

# Grid configuration
ax.grid(True, linestyle='--', alpha=0.7)

# Legend
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Save figure
plt.tight_layout()
output_filename = f'polar_plot_{motion_label.replace(" ", "_")}.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
print(f"Figure saved: {output_filename}")

# Display figure
plt.show()
