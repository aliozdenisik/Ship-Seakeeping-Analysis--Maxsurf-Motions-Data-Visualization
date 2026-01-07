#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motion Sickness Incidence (MSI) Visualization

Generates MSI assessment plots comparing vessel acceleration responses
against ISO 2631 severe discomfort boundaries for various exposure durations.

Data source: Maxsurf Motions analysis output
Reference: ISO 2631-1:1997 - Mechanical vibration and shock evaluation

Author: Ali Özden Işık
Institution: Istanbul Technical University - Naval Architecture and Marine Engineering
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# =============================================================================
# CONFIGURATION
# =============================================================================

# Get script directory path
script_dir = os.path.dirname(os.path.abspath(__file__))

# Search for MSI data file
excel_file = os.path.join(script_dir, 'MSI.xlsx')

# Search parent directory if not found in current location
if not os.path.exists(excel_file):
    excel_file = os.path.join(os.path.dirname(script_dir), 'MSI.xlsx')

# Verify file exists
if not os.path.exists(excel_file):
    print(f"ERROR: File not found!")
    print(f"  Searched locations:")
    print(f"  1. {os.path.join(script_dir, 'MSI.xlsx')}")
    print(f"  2. {os.path.join(os.path.dirname(script_dir), 'MSI.xlsx')}")
    exit(1)

print(f"Excel file found: {excel_file}")

# =============================================================================
# DATA LOADING
# =============================================================================

# Read Excel file
xls = pd.ExcelFile(excel_file)

print(f"Excel file loaded successfully. Found {len(xls.sheet_names)} sheets.\n")

# =============================================================================
# PLOT GENERATION
# =============================================================================

# Generate plot for each wave heading angle
for sheet_name in xls.sheet_names:
    print(f"Generating plot: {sheet_name} degrees...")
    
    # Read sheet data
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    
    # Extract data columns
    encounter_freq = df.iloc[:, 0]    # Encounter frequency (rad/s)
    iso_30min = df.iloc[:, 1]         # ISO 2631 30-minute limit
    iso_2hrs = df.iloc[:, 3]          # ISO 2631 2-hour limit
    iso_8hrs = df.iloc[:, 5]          # ISO 2631 8-hour limit
    officer_cabin = df.iloc[:, 7]     # Officer cabin response
    
    # Create figure
    plt.figure(figsize=(12, 8))
    
    # Plot ISO 2631 severe discomfort boundaries
    plt.plot(encounter_freq, iso_30min, 'r-', linewidth=2, 
             label='Severe discomfort boundary for 30 min. exposure (ISO 2631)')
    plt.plot(encounter_freq, iso_2hrs, 'k-', linewidth=2, 
             label='Severe discomfort boundary for 2 hrs. exposure (ISO 2631)')
    plt.plot(encounter_freq, iso_8hrs, 'b-', linewidth=2, 
             label='Severe discomfort boundary for 8 hrs. exposure (ISO 2631)')
    
    # Plot vessel response at remote location
    plt.plot(encounter_freq, officer_cabin, 'k-', linewidth=1.5, 
             label='Officer Cabin (Port)')
    
    # Configure grid
    plt.grid(True, linestyle='--', alpha=0.7, color='gray')
    
    # Axis labels
    plt.xlabel('Encounter Frequency (rad/s)', fontsize=12, fontweight='bold')
    plt.ylabel('Acceleration (m/s²)', fontsize=12, fontweight='bold')
    
    # Title
    plt.title(f'MSI - Wave Heading: {sheet_name}°', fontsize=14, fontweight='bold')
    
    # Legend
    plt.legend(loc='upper left', fontsize=9, framealpha=0.9)
    
    # Axis limits
    plt.ylim(bottom=0)
    plt.xlim(left=0)
    
    # Configure axis ordering
    ax = plt.gca()
    ax.set_axisbelow(True)
    
    # Optimize layout
    plt.tight_layout()
    
    # Save figure
    output_filename = f'MSI_Graph_{sheet_name}deg.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"  [OK] Saved: {output_filename}")
    
    # Display figure
    plt.show()
    
    # Close figure window
    plt.close()

print(f"\n[SUCCESS] All figures generated successfully!")
print(f"[INFO] Figures saved to current directory.")
