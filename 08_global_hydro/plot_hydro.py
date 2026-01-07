#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Global Hydrodynamic Coefficients Visualization

Generates publication-quality plots for wave excitation force and moment
(heave force and pitch moment) from global hydrodynamic coefficient data.

Data source: Maxsurf Motions Global Hydrodynamic Coefficients output
Motion modes: Mode 3 (Heave), Mode 5 (Pitch)

Author: Ali Özden Işık
Institution: Istanbul Technical University - Naval Architecture and Marine Engineering
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# =============================================================================
# ACADEMIC STYLE SETTINGS
# =============================================================================

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 12,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14
})


def read_data():
    """
    Read and parse hydrodynamic coefficient data from file.
    
    Returns
    -------
    pd.DataFrame or None
        DataFrame with columns: Freq3, Amp3, Freq5, Amp5
        Returns None if file cannot be read.
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(script_dir, 'hydro_data.txt')
        
        # Manual parsing for decimal comma format
        parsed_data = []
        with open(data_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if not parts:
                    continue
                # Replace comma with dot and convert to float
                row = [float(p.replace(',', '.')) for p in parts]
                parsed_data.append(row)
        
        df = pd.DataFrame(parsed_data, columns=['Freq3', 'Amp3', 'Freq5', 'Amp5'])
        
        # Sort by frequency
        df = df.sort_values(by='Freq3')
        
        return df

    except Exception as e:
        print(f"Error reading data: {e}")
        return None


def plot_subplots(df):
    """
    Generate stacked subplot layout with force and moment plots.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing frequency and amplitude data
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Extract data
    freq = df['Freq3'].values
    amp3 = df['Amp3'].values
    amp5 = df['Amp5'].values
    freq5 = df['Freq5'].values

    # Plot 1: Wave Excitation Force (Mode 3 - Heave)
    ax1.plot(freq, amp3, 'b-', linewidth=1.5, label='Mode 3: Heave Force')
    ax1.set_ylabel(r'Excitation Force ($kN/m$)', fontsize=12)
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    ax1.legend(loc='upper left')
    ax1.set_title('Wave Excitation Force vs Encounter Frequency', fontsize=14)

    # Plot 2: Wave Excitation Moment (Mode 5 - Pitch)
    ax2.plot(freq5, amp5, 'r-', linewidth=1.5, label='Mode 5: Pitch Moment')
    ax2.set_xlabel(r'Encounter Frequency ($\omega_e$) [rad/s]', fontsize=12)
    ax2.set_ylabel(r'Excitation Moment ($kNm/m$)', fontsize=12)
    ax2.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    ax2.legend(loc='upper left')
    ax2.set_title('Wave Excitation Moment vs Encounter Frequency', fontsize=14)

    plt.tight_layout()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'academic_plot_subplots.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Subplot figure saved: {output_path}")


def plot_dual_axis(df):
    """
    Generate dual-axis plot with force and moment on same figure.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing frequency and amplitude data
    """
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Extract data
    freq = df['Freq3'].values
    amp3 = df['Amp3'].values
    amp5 = df['Amp5'].values
    
    # Plot Mode 3 (Force) on left axis
    color = 'tab:blue'
    ax1.set_xlabel('Encounter Frequency (rad/s)', fontsize=12)
    ax1.set_ylabel('Wave Excitation Force (kN/m)', color=color, fontsize=12)
    line1, = ax1.plot(freq, amp3, color=color, linewidth=2, label='Mode 3: Heave Force')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Create secondary axis sharing x
    ax2 = ax1.twinx() 
    
    # Plot Mode 5 (Moment) on right axis
    color = 'tab:red'
    ax2.set_ylabel('Wave Excitation Moment (kNm/m)', color=color, fontsize=12) 
    line2, = ax2.plot(freq, amp5, color=color, linewidth=2, label='Mode 5: Pitch Moment')
    ax2.tick_params(axis='y', labelcolor=color)

    # Combined legend
    lines = [line1, line2]
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', frameon=True, fancybox=True, framealpha=0.9)

    plt.title('Wave Excitation Force and Moment', fontsize=14, pad=15)
    plt.tight_layout()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'academic_plot_dual.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Dual-axis figure saved: {output_path}")


if __name__ == "__main__":
    df = read_data()
    if df is not None:
        plot_subplots(df)
        plot_dual_axis(df)
        print("\nAll figures generated successfully!")
