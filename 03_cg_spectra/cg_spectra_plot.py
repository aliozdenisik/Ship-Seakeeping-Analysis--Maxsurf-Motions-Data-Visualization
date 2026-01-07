#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CG Motion Response Spectra Visualization

Generates academic publication-quality plots for center of gravity motion
response spectra including wave spectrum, heave, pitch, and added resistance.

Data source: Maxsurf Motions CG Spectrum analysis output
Analysis condition: Bretschneider spectrum, Sea State 5

Author: Ali Özden Işık
Institution: Istanbul Technical University - Naval Architecture and Marine Engineering
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import os

# =============================================================================
# DATA LOADING
# =============================================================================

script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_dir, 'spectra_data.csv')

df = pd.read_csv(data_file, sep=';', decimal=',')

print(f"Data file loaded: {data_file}")
print(f"Total rows: {len(df)}")

# Extract all columns
wave_freq = df['S_Wave_X'].values          # Wave spectrum (encounter frequency)
wave_sd = df['S_Wave_Y'].values

heave_freq = df['S_Heave_X'].values
heave_sd = df['S_Heave_Y'].values

pitch_freq = df['S_Pitch_X'].values
pitch_sd = df['S_Pitch_Y'].values

added_res_freq = df['S_Added_Res_X'].values
added_res_sd = df['S_Added_Res_Y'].values

wave_wf_freq = df['S_Wave_WF_X'].values    # Wave spectrum (wave frequency)
wave_wf_sd = df['S_Wave_WF_Y'].values

# =============================================================================
# ACADEMIC FIGURE SETTINGS
# =============================================================================

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'legend.fontsize': 9,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'axes.linewidth': 0.6,
    'grid.linewidth': 0.4,
    'lines.linewidth': 1.0,
    'axes.spines.top': True,
    'axes.spines.right': True,
})

# Color palette matching Maxsurf output
colors = {
    'wave': '#0000CD',       # Dark blue (S Wave)
    'heave': '#00CED1',      # Cyan/Turquoise (S Heave)
    'pitch': '#DC143C',      # Crimson red (S Pitch)
    'added_res': '#6B8E23',  # Olive green (S Added resistance)
    'wave_wf': '#FF69B4'     # Hot pink (S Wave - wave freq.)
}

# =============================================================================
# FIGURE 1: 2x2 SUBPLOT LAYOUT
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('CG Motion Response Spectra', fontsize=12, fontweight='bold', y=0.98)

# ---- Subplot 1: Wave Spectral Density ----
ax1 = axes[0, 0]
ax1.plot(wave_freq, wave_sd, color=colors['wave'], linewidth=1.0, linestyle='-', label='S Wave (Enc.)')
ax1.plot(wave_wf_freq, wave_wf_sd, color=colors['wave_wf'], linewidth=1.2, linestyle=':', label='S Wave (Wave freq.)')
ax1.set_xlabel(r'Frequency, $\omega$ [rad/s]')
ax1.set_ylabel(r'$S_{wave}$ [m$^2$/(rad/s)]')
ax1.set_title('(a) Wave Spectrum', fontsize=11)
ax1.legend(loc='upper right', fontsize=8)
ax1.grid(True, linestyle=':', alpha=0.5, linewidth=0.4)
ax1.set_xlim([0, 2.0])
ax1.set_ylim([0, 2.4])
ax1.xaxis.set_major_locator(MultipleLocator(0.4))
ax1.yaxis.set_major_locator(MultipleLocator(0.4))

# ---- Subplot 2: Heave Motion Spectrum ----
ax2 = axes[0, 1]
ax2.plot(heave_freq, heave_sd, color=colors['heave'], linewidth=1.0)
ax2.set_xlabel(r'Encounter Frequency, $\omega_e$ [rad/s]')
ax2.set_ylabel(r'$S_{heave}$ [m$^2$/(rad/s)]')
ax2.set_title('(b) Heave Motion Spectrum', fontsize=11)
ax2.grid(True, linestyle=':', alpha=0.5, linewidth=0.4)
ax2.set_xlim([0, 2.0])
ax2.set_ylim([0, 7])
ax2.xaxis.set_major_locator(MultipleLocator(0.4))
ax2.yaxis.set_major_locator(MultipleLocator(1))

# ---- Subplot 3: Pitch Motion Spectrum ----
ax3 = axes[1, 0]
ax3.plot(pitch_freq, pitch_sd, color=colors['pitch'], linewidth=1.0)
ax3.set_xlabel(r'Encounter Frequency, $\omega_e$ [rad/s]')
ax3.set_ylabel(r'$S_{pitch}$ [deg$^2$/(rad/s)]')
ax3.set_title('(c) Pitch Motion Spectrum', fontsize=11)
ax3.grid(True, linestyle=':', alpha=0.5, linewidth=0.4)
ax3.set_xlim([0, 2.0])
ax3.set_ylim([0, 0.7])
ax3.xaxis.set_major_locator(MultipleLocator(0.4))
ax3.yaxis.set_major_locator(MultipleLocator(0.1))

# ---- Subplot 4: Added Resistance Spectrum ----
ax4 = axes[1, 1]
ax4.plot(added_res_freq, added_res_sd, color=colors['added_res'], linewidth=1.0)
ax4.set_xlabel(r'Encounter Frequency, $\omega_e$ [rad/s]')
ax4.set_ylabel(r'$S_{R_{aw}}$ [kN/(rad/s)]')
ax4.set_title('(d) Added Resistance Spectrum', fontsize=11)
ax4.grid(True, linestyle=':', alpha=0.5, linewidth=0.4)
ax4.set_xlim([0, 2.0])
ax4.set_ylim([0, 2800])
ax4.xaxis.set_major_locator(MultipleLocator(0.4))
ax4.yaxis.set_major_locator(MultipleLocator(400))

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(os.path.join(script_dir, 'cg_spectra_academic.png'), dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig(os.path.join(script_dir, 'cg_spectra_academic.pdf'), bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.show()

print("\n" + "="*60)
print("4-Panel figure generated!")
print("="*60)

# =============================================================================
# FIGURE 2: COMBINED MULTI-AXIS PLOT (5 DATA SERIES)
# =============================================================================

fig2, ax_main = plt.subplots(figsize=(14, 8))

# Create multiple y-axes
ax_added = ax_main                    # Added Resistance (left, primary)
ax_pitch = ax_main.twinx()            # Pitch (left outer)
ax_heave = ax_main.twinx()            # Heave (right)
ax_wave = ax_main.twinx()             # Wave (right outer)

# Position the axes spines
ax_pitch.spines['left'].set_position(('outward', 60))
ax_pitch.yaxis.set_label_position('left')
ax_pitch.yaxis.tick_left()

ax_heave.spines['right'].set_position(('outward', 0))
ax_heave.yaxis.set_label_position('right')
ax_heave.yaxis.tick_right()

ax_wave.spines['right'].set_position(('outward', 60))
ax_wave.yaxis.set_label_position('right')
ax_wave.yaxis.tick_right()

# Plot all 5 data series
p1, = ax_wave.plot(wave_freq, wave_sd, color=colors['wave'], 
                   linewidth=1.2, linestyle='-', label='S Wave')
p2, = ax_heave.plot(heave_freq, heave_sd, color=colors['heave'], 
                    linewidth=1.2, linestyle='-', label='S Heave')
p3, = ax_pitch.plot(pitch_freq, pitch_sd, color=colors['pitch'], 
                    linewidth=1.2, linestyle='-', label='S Pitch')
p4, = ax_added.plot(added_res_freq, added_res_sd, color=colors['added_res'], 
                    linewidth=1.2, linestyle='-', label='S Added resistance')
p5, = ax_wave.plot(wave_wf_freq, wave_wf_sd, color=colors['wave_wf'], 
                   linewidth=1.4, linestyle=':', label='S Wave(Wave freq.)')

# Axis labels
ax_added.set_ylabel(r'Added Resistance Spectral Density  kN/(rad/s)', fontsize=10)
ax_pitch.set_ylabel(r'Angular Motion Spectral Density  deg$^2$/(rad/s)', fontsize=10)
ax_heave.set_ylabel(r'Linear Motion Spectral Density  m$^2$/(rad/s)', fontsize=10)
ax_wave.set_ylabel(r'Wave Spectral Density  m$^2$/(rad/s)', fontsize=10)

ax_main.set_xlabel(r'Wave, Encounter Frequency  rad/s', fontsize=11)

# Axis limits
ax_main.set_xlim([0, 2.0])
ax_added.set_ylim([0, 2800])
ax_pitch.set_ylim([0, 0.7])
ax_heave.set_ylim([0, 7])
ax_wave.set_ylim([0, 2.4])

# Grid
ax_main.grid(True, linestyle=':', alpha=0.4, linewidth=0.4)
ax_main.xaxis.set_major_locator(MultipleLocator(0.4))
ax_main.xaxis.set_minor_locator(MultipleLocator(0.1))

# Legend
lines = [p1, p2, p3, p4, p5]
labels = [l.get_label() for l in lines]
legend = ax_main.legend(lines, labels, loc='upper left', framealpha=0.95, fontsize=9,
                        title='CG spectra', title_fontsize=10, edgecolor='black',
                        fancybox=False)
legend.get_frame().set_linewidth(0.8)

# Title
ax_main.set_title('CG Motion Response Spectra', fontsize=12, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'cg_spectra_combined.png'), dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig(os.path.join(script_dir, 'cg_spectra_combined.pdf'), bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.show()

print("\nCombined figure also generated!")
print("Files: cg_spectra_combined.png and cg_spectra_combined.pdf")
