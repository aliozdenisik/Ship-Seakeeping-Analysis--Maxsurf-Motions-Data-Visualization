#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remote Location Response Spectra Visualization

Generates publication-quality plots for motion response spectra at a specified
remote location (crew compartment) including displacement, velocity, acceleration,
and relative motion components.

Data source: Maxsurf Motions Remote Location Spectrum output
Location: Officer cabin (port side, off-centerline)

Author: Ali Özden Işık
Institution: Istanbul Technical University - Naval Architecture and Marine Engineering
"""

import matplotlib.pyplot as plt
import numpy as np
import os


def parse_data(filename):
    """
    Parse tab-separated data file with European decimal format (comma).
    
    Parameters
    ----------
    filename : str
        Path to the data file
        
    Returns
    -------
    np.ndarray
        Parsed data array with shape (n_rows, n_columns)
    """
    data = []
    with open(filename, 'r') as f:
        for line in f:
            if not line.strip():
                continue
            # Replace decimal comma with dot
            line = line.replace(',', '.')
            parts = line.strip().split()
            row = [float(p) for p in parts]
            data.append(row)
    return np.array(data)


def plot_spectra(data, output_file):
    """
    Generate combined multi-axis plot for remote location spectra.
    
    Parameters
    ----------
    data : np.ndarray
        Parsed spectral data
    output_file : str
        Output filename for the figure
    """
    # Set academic style
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
    plt.rcParams['font.size'] = 12
    
    # Series headers and visualization styles
    headers = [
        "S Wave", 
        "S V.Disp", 
        "S V.Vel", 
        "S V.Accel", 
        "S V.Rel Disp", 
        "S V.Rel Vel", 
        "S V.Rel Accel"
    ]

    # Color palette
    colors = ['black', 'blue', 'green', 'cyan', 'red', 'orange', 'brown']
    linestyles = ['-', '-', '-', '-', '-', '-', '-']
    
    fig, ax_wave = plt.subplots(figsize=(12, 8))
    fig.subplots_adjust(left=0.30)  # Make room for stacked left-side axes

    # Create twin axes for different physical quantities
    ax_mot = ax_wave.twinx()
    ax_vel = ax_wave.twinx()
    ax_acc = ax_wave.twinx()

    # Position twin axes on the left side
    for ax in [ax_mot, ax_vel, ax_acc]:
        ax.yaxis.set_label_position("left")
        ax.yaxis.set_ticks_position("left")

    # Offset the spines for visual separation
    offset_step = 60
    ax_mot.spines["left"].set_position(("outward", offset_step))
    ax_vel.spines["left"].set_position(("outward", offset_step * 2))
    ax_acc.spines["left"].set_position(("outward", offset_step * 3))

    # Axis labels with proper units
    ax_wave.set_ylabel(r"Wave Spectral Density $m^2/(rad/s)$")
    ax_mot.set_ylabel(r"Linear Motion Spectral Density $m^2/(rad/s)$")
    ax_vel.set_ylabel(r"Linear Velocity Spectral Density $(m/s)^2/(rad/s)$")
    ax_acc.set_ylabel(r"Linear Acceleration Spectral Density $(m/s^2)^2/(rad/s)$")
    ax_wave.set_xlabel("Encounter Frequency (rad/s)")
    
    # X-axis limit for readability
    ax_wave.set_xlim(0.35, 1.9)
    
    # Plot each data series on appropriate axis
    lines = []
    
    for i in range(7):
        x_col = i * 2
        y_col = i * 2 + 1
        x = data[:, x_col]
        y = data[:, y_col]
        
        # Determine target axis based on physical quantity
        if i == 0:                  # S Wave
            target_ax = ax_wave
        elif i in [1, 4]:           # V.Disp, V.Rel Disp
            target_ax = ax_mot
        elif i in [2, 5]:           # V.Vel, V.Rel Vel
            target_ax = ax_vel
        elif i in [3, 6]:           # V.Accel, V.Rel Accel
            target_ax = ax_acc
        else:
            target_ax = ax_wave
            
        l, = target_ax.plot(x, y, label=headers[i], color=colors[i], 
                           linestyle=linestyles[i], linewidth=1.5)
        lines.append(l)

    ax_wave.set_title("Remote Location Spectra")
    ax_wave.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    
    # Combined legend
    labs = [l.get_label() for l in lines]
    ax_wave.legend(lines, labs, loc='upper right', frameon=True, fontsize=9)
    
    # Save figure
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Main plot saved to {output_file}")


def plot_subplots(data, output_file):
    """
    Generate individual subplot for each spectral component.
    
    Parameters
    ----------
    data : np.ndarray
        Parsed spectral data
    output_file : str
        Output filename for the figure
    """
    # Set academic style
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
    plt.rcParams['font.size'] = 10
    
    # Series headers
    headers = [
        "S Wave", 
        "S V.Disp", 
        "S V.Vel", 
        "S V.Accel", 
        "S V.Rel Disp", 
        "S V.Rel Vel", 
        "S V.Rel Accel"
    ]
    
    # Y-axis labels with units
    y_labels = [
        r"Wave Spectral Density $m^2/(rad/s)$",
        r"Linear Motion Spectral Density $m^2/(rad/s)$",
        r"Linear Velocity Spectral Density $(m/s)^2/(rad/s)$",
        r"Linear Acceleration Spectral Density $(m/s^2)^2/(rad/s)$",
        r"Relative Motion Spectral Density $m^2/(rad/s)$",
        r"Relative Velocity Spectral Density $(m/s)^2/(rad/s)$",
        r"Relative Acceleration Spectral Density $(m/s^2)^2/(rad/s)$"
    ]
    
    colors = ['black', 'blue', 'green', 'red', 'orange', 'purple', 'brown']
    
    # 4 rows, 2 columns grid
    fig, axes = plt.subplots(4, 2, figsize=(12, 14))
    axes = axes.flatten()
    
    for i in range(7):
        ax = axes[i]
        x_col = i * 2
        y_col = i * 2 + 1
        x = data[:, x_col]
        y = data[:, y_col]
        
        ax.plot(x, y, color=colors[i], linewidth=1.5)
        ax.set_title(headers[i])
        ax.set_xlabel("Encounter Frequency (rad/s)")
        ax.set_ylabel(y_labels[i])
        ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
        
        # Set X-axis limit (extended range for relative acceleration)
        if headers[i] != "S V.Rel Accel":
            ax.set_xlim(left=0.35, right=1.9)
        else:
            ax.set_xlim(left=0.35, right=3.0) 
            
    # Turn off the last empty subplot
    axes[7].axis('off')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.close()
    print(f"Subplots saved to {output_file}")


if __name__ == "__main__":
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(script_dir, "data.txt")
    
    # Parse data and generate figures
    data = parse_data(data_file)
    plot_spectra(data, os.path.join(script_dir, "remote_spectra_main.png"))
    plot_subplots(data, os.path.join(script_dir, "remote_spectra_subplots.png"))
    
    print("\nAll figures generated successfully!")
