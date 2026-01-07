#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remote Location RAO (Response Amplitude Operator) Visualization

Generates publication-quality plots for Response Amplitude Operators at a remote
location (crew compartment). Configurable for different data sets with comparison
capability.

Data source: Maxsurf Motions Remote Location RAO output
Motion modes: Longitudinal, Lateral, Vertical, Roll, Pitch

Author: Ali Özden Işık
Institution: Istanbul Technical University - Naval Architecture and Marine Engineering
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os

# =============================================================================
# DATA INPUT
# =============================================================================

# Dataset 1: Primary data (tab-separated, comma decimal)
DATA_STRING_1 = """0,360002	0,165603	0,360002	0,000000	0,360002	1,336221	0,360002	0,000000	0,360002	1,022664
0,364446	0,169100	0,364446	0,000000	0,364446	1,346198	0,364446	0,000000	0,364446	1,022286
0,368891	0,172495	0,368891	0,000000	0,368891	1,354798	0,368891	0,000000	0,368891	1,021823
0,373335	0,175854	0,373335	0,000000	0,373335	1,363311	0,373335	0,000000	0,373335	1,021272
0,377779	0,179232	0,377779	0,000000	0,377779	1,372773	0,377779	0,000000	0,377779	1,020632
0,382223	0,182416	0,382223	0,000000	0,382223	1,379912	0,382223	0,000000	0,382223	1,019899
0,386668	0,185585	0,386668	0,000000	0,386668	1,387493	0,386668	0,000000	0,386668	1,019071
0,391112	0,188769	0,391112	0,000000	0,391112	1,396001	0,391112	0,000000	0,391112	1,018144
0,395556	0,191638	0,395556	0,000000	0,395556	1,401065	0,395556	0,000000	0,395556	1,017116
0,400001	0,194541	0,400001	0,000000	0,400001	1,407340	0,400001	0,000000	0,400001	1,015984
0,419048	0,205280	0,419048	0,000000	0,419048	1,423771	0,419048	0,000000	0,419048	1,009884
0,438095	0,212711	0,438095	0,000000	0,438095	1,421909	0,438095	0,000000	0,438095	1,001642
0,457143	0,214810	0,457143	0,000000	0,457143	1,388325	0,457143	0,000000	0,457143	0,991311
0,476191	0,210589	0,476191	0,000000	0,476191	1,320370	0,476191	0,000000	0,476191	0,978264
0,495238	0,197365	0,495238	0,000000	0,495238	1,199917	0,495238	0,000000	0,495238	0,962195
0,514286	0,174655	0,514286	0,000000	0,514286	1,027401	0,514286	0,000000	0,514286	0,942759
0,533333	0,144001	0,533333	0,000000	0,533333	0,819125	0,533333	0,000000	0,533333	0,919564
0,552381	0,108028	0,552381	0,000000	0,552381	0,598636	0,552381	0,000000	0,552381	0,892175
0,571429	0,071142	0,571429	0,000000	0,571429	0,403222	0,571429	0,000000	0,571429	0,860109
0,590476	0,037297	0,590476	0,000000	0,590476	0,277864	0,590476	0,000000	0,590476	0,822860
0,609524	0,008896	0,609524	0,000000	0,609524	0,252103	0,609524	0,000000	0,609524	0,779944
0,628571	0,012911	0,628571	0,000000	0,628571	0,286324	0,628571	0,000000	0,628571	0,730981
0,647619	0,028075	0,647619	0,000000	0,647619	0,322936	0,647619	0,000000	0,647619	0,675831
0,666667	0,037093	0,666667	0,000000	0,666667	0,339892	0,666667	0,000000	0,666667	0,614775
0,685714	0,041154	0,685714	0,000000	0,685714	0,336161	0,685714	0,000000	0,685714	0,548693
0,704762	0,041308	0,704762	0,000000	0,704762	0,314914	0,704762	0,000000	0,704762	0,479138
0,723810	0,038528	0,723810	0,000000	0,723810	0,280617	0,723810	0,000000	0,723810	0,408195
0,742857	0,033693	0,742857	0,000000	0,742857	0,237924	0,742857	0,000000	0,742857	0,338166
0,761905	0,027580	0,761905	0,000000	0,761905	0,191280	0,761905	0,000000	0,761905	0,271209
0,780952	0,020860	0,780952	0,000000	0,780952	0,144942	0,780952	0,000000	0,780952	0,209103
0,800000	0,014118	0,800000	0,000000	0,800000	0,103465	0,800000	0,000000	0,800000	0,153134
0,819048	0,007933	0,819048	0,000000	0,819048	0,072985	0,819048	0,000000	0,819048	0,104073
0,838095	0,003572	0,838095	0,000000	0,838095	0,061106	0,838095	0,000000	0,838095	0,062201
0,857143	0,004642	0,857143	0,000000	0,857143	0,066646	0,857143	0,000000	0,857143	0,027392
0,876190	0,007650	0,876190	0,000000	0,876190	0,077563	0,876190	0,000000	0,876190	0,000905
0,895238	0,009840	0,895238	0,000000	0,895238	0,085714	0,895238	0,000000	0,895238	0,022945
0,914286	0,010891	0,914286	0,000000	0,914286	0,088335	0,914286	0,000000	0,914286	0,039785
0,933333	0,010789	0,933333	0,000000	0,933333	0,084920	0,933333	0,000000	0,933333	0,052042
0,952381	0,009738	0,952381	0,000000	0,952381	0,076867	0,952381	0,000000	0,952381	0,060391
0,971429	0,007944	0,971429	0,000000	0,971429	0,065455	0,971429	0,000000	0,971429	0,065494
0,990476	0,006094	0,990476	0,000000	0,990476	0,055785	0,990476	0,000000	0,990476	0,067952
1,009524	0,004798	1,009524	0,000000	1,009524	0,050149	1,009524	0,000000	1,009524	0,068281
1,028571	0,004818	1,028571	0,000000	1,028571	0,051577	1,028571	0,000000	1,028571	0,066926
1,047619	0,005371	1,047619	0,000000	1,047619	0,052779	1,047619	0,000000	1,047619	0,064269
1,066667	0,006328	1,066667	0,000000	1,066667	0,057245	1,066667	0,000000	1,066667	0,060635
1,085714	0,006525	1,085714	0,000000	1,085714	0,056703	1,085714	0,000000	1,085714	0,056297
1,104762	0,006306	1,104762	0,000000	1,104762	0,054467	1,104762	0,000000	1,104762	0,051483
1,123810	0,005907	1,123810	0,000000	1,123810	0,052471	1,123810	0,000000	1,123810	0,046385
1,142857	0,005045	1,142857	0,000000	1,142857	0,046902	1,142857	0,000000	1,142857	0,041157
1,161905	0,004734	1,161905	0,000000	1,161905	0,045586	1,161905	0,000000	1,161905	0,035930
1,180952	0,004753	1,180952	0,000000	1,180952	0,045446	1,180952	0,000000	1,180952	0,030806
1,200000	0,004764	1,200000	0,000000	1,200000	0,044340	1,200000	0,000000	1,200000	0,025871
1,219048	0,004972	1,219048	0,000000	1,219048	0,045224	1,219048	0,000000	1,219048	0,021194
1,238095	0,004733	1,238095	0,000000	1,238095	0,042926	1,238095	0,000000	1,238095	0,016831
1,257143	0,004356	1,257143	0,000000	1,257143	0,039911	1,257143	0,000000	1,257143	0,012837
1,276190	0,004215	1,276190	0,000000	1,276190	0,039123	1,276190	0,000000	1,276190	0,009277
1,295238	0,003978	1,295238	0,000000	1,295238	0,036968	1,295238	0,000000	1,295238	0,006274
1,314286	0,003796	1,314286	0,000000	1,314286	0,035045	1,314286	0,000000	1,314286	0,004156
1,333333	0,003780	1,333333	0,000000	1,333333	0,034735	1,333333	0,000000	1,333333	0,003605
1,352381	0,003564	1,352381	0,000000	1,352381	0,032915	1,352381	0,000000	1,352381	0,004538
1,371429	0,003229	1,371429	0,000000	1,371429	0,030051	1,371429	0,000000	1,371429	0,005920
1,390476	0,003107	1,390476	0,000000	1,390476	0,028890	1,390476	0,000000	1,390476	0,007236
1,409524	0,003116	1,409524	0,000000	1,409524	0,028655	1,409524	0,000000	1,409524	0,008332
1,428571	0,002838	1,428571	0,000000	1,428571	0,025894	1,428571	0,000000	1,428571	0,009171
1,447619	0,002627	1,447619	0,000000	1,447619	0,024086	1,447619	0,000000	1,447619	0,009747
1,466667	0,002465	1,466667	0,000000	1,466667	0,022962	1,466667	0,000000	1,466667	0,010072
1,485714	0,002251	1,485714	0,000000	1,485714	0,021221	1,485714	0,000000	1,485714	0,010164
1,504762	0,000000	1,504762	0,000000	1,504762	0,000000	1,504762	0,000000	1,504762	0,010046
1,523810	0,000000	1,523810	0,000000	1,523810	0,000000	1,523810	0,000000	1,523810	0,009744
1,542857	0,000000	1,542857	0,000000	1,542857	0,000000	1,542857	0,000000	1,542857	0,009286
1,561905	0,000000	1,561905	0,000000	1,561905	0,000000	1,561905	0,000000	1,561905	0,008700
1,580952	0,000000	1,580952	0,000000	1,580952	0,000000	1,580952	0,000000	1,580952	0,008018
1,600000	0,000000	1,600000	0,000000	1,600000	0,000000	1,600000	0,000000	1,600000	0,007273
1,677778	0,000000	1,677778	0,000000	1,677778	0,000000	1,677778	0,000000	1,677778	0,004360
1,755556	0,000000	1,755556	0,000000	1,755556	0,000000	1,755556	0,000000	1,755556	0,003623
1,833333	0,000000	1,833333	0,000000	1,833333	0,000000	1,833333	0,000000	1,833333	0,004379
1,911111	0,000000	1,911111	0,000000	1,911111	0,000000	1,911111	0,000000	1,911111	0,004404
1,988889	0,000000	1,988889	0,000000	1,988889	0,000000	1,988889	0,000000	1,988889	0,003634
2,066667	0,000000	2,066667	0,000000	2,066667	0,000000	2,066667	0,000000	2,066667	0,002900
2,144444	0,000000	2,144444	0,000000	2,144444	0,000000	2,144444	0,000000	2,144444	0,002735
2,222222	0,000000	2,222222	0,000000	2,222222	0,000000	2,222222	0,000000	2,222222	0,002698
2,300000	0,000000	2,300000	0,000000	2,300000	0,000000	2,300000	0,000000	2,300000	0,002430
2,377778	0,000000	2,377778	0,000000	2,377778	0,000000	2,377778	0,000000	2,377778	0,002093
2,455556	0,000000	2,455556	0,000000	2,455556	0,000000	2,455556	0,000000	2,455556	0,001891
2,533333	0,000000	2,533333	0,000000	2,533333	0,000000	2,533333	0,000000	2,533333	0,001740
2,611111	0,000000	2,611111	0,000000	2,611111	0,000000	2,611111	0,000000	2,611111	0,001537
2,688889	0,000000	2,688889	0,000000	2,688889	0,000000	2,688889	0,000000	2,688889	0,001349
2,766667	0,000000	2,766667	0,000000	2,766667	0,000000	2,766667	0,000000	2,766667	0,001228
2,844444	0,000000	2,844444	0,000000	2,844444	0,000000	2,844444	0,000000	2,844444	0,001106
2,922222	0,000000	2,922222	0,000000	2,922222	0,000000	2,922222	0,000000	2,922222	0,000944
3,000000	0,000000	3,000000	0,000000	3,000000	0,000000	3,000000	0,000000	3,000000	0,000805"""

# Dataset 2 placeholder (same format)
DATA_STRING_2 = None

# =============================================================================
# PLOT CONFIGURATION
# =============================================================================

PLOT_CONFIG = {
    'main_title': 'Remote Location RAOs',
    'x_label': r'Encounter Frequency $\omega_e$ [rad/s]',
    'y_label': 'RAO (Transfer Function)',
    'figure_size': (10, 6),
    'dpi': 300,
    'font_size': 11,
    'legend_font_size': 9,
    'tick_font_size': 9,
    'line_width': 0.8,
    'grid_alpha': 0.25,
    'save_format': 'png',
    'main_plot_xlim': 1.2,
    'subplot_xlim': 2.0,
}

# RAO types and colors (academic standard palette)
RAO_CONFIG = {
    'Long. RAO': {'color': '#1f77b4', 'linestyle': '-', 'marker': None},
    'Lat. RAO': {'color': '#2ca02c', 'linestyle': '-', 'marker': None},
    'Vert. RAO': {'color': '#d62728', 'linestyle': '-', 'marker': None},
    'Roll RAO': {'color': '#9467bd', 'linestyle': '-', 'marker': None},
    'Pitch RAO': {'color': '#ff7f0e', 'linestyle': '-', 'marker': None},
}

# =============================================================================
# DATA PROCESSING FUNCTIONS
# =============================================================================

def parse_data(data_string):
    """
    Parse tab-separated data with European decimal format.
    
    Parameters
    ----------
    data_string : str
        Raw data string with tab separation and comma decimals
        
    Returns
    -------
    dict
        Dictionary containing RAO data for each motion mode
    """
    lines = data_string.strip().split('\n')
    
    data = {
        'Long. RAO': {'x': [], 'y': []},
        'Lat. RAO': {'x': [], 'y': []},
        'Vert. RAO': {'x': [], 'y': []},
        'Roll RAO': {'x': [], 'y': []},
        'Pitch RAO': {'x': [], 'y': []},
    }
    
    rao_keys = list(data.keys())
    
    for line in lines:
        values = line.split('\t')
        values = [float(v.replace(',', '.')) for v in values]
        
        for i, key in enumerate(rao_keys):
            data[key]['x'].append(values[i * 2])
            data[key]['y'].append(values[i * 2 + 1])
    
    # Convert to numpy arrays
    for key in data:
        data[key]['x'] = np.array(data[key]['x'])
        data[key]['y'] = np.array(data[key]['y'])
    
    return data

# =============================================================================
# PLOTTING FUNCTIONS
# =============================================================================

def setup_academic_style():
    """Configure matplotlib for academic publication format."""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman'],
        'mathtext.fontset': 'stix',
        'font.size': PLOT_CONFIG['font_size'],
        'axes.labelsize': PLOT_CONFIG['font_size'],
        'axes.titlesize': PLOT_CONFIG['font_size'] + 2,
        'legend.fontsize': PLOT_CONFIG['legend_font_size'],
        'xtick.labelsize': PLOT_CONFIG['tick_font_size'],
        'ytick.labelsize': PLOT_CONFIG['tick_font_size'],
        'figure.dpi': PLOT_CONFIG['dpi'],
        'savefig.dpi': PLOT_CONFIG['dpi'],
        'axes.linewidth': 0.8,
        'grid.linewidth': 0.5,
        'lines.linewidth': PLOT_CONFIG['line_width'],
    })


def create_single_rao_plot(data, filename='rao_plot_single.png', title_suffix=''):
    """
    Generate combined plot with all RAOs on single axes.
    
    Parameters
    ----------
    data : dict
        Parsed RAO data dictionary
    filename : str
        Output filename
    title_suffix : str
        Additional title text
    """
    setup_academic_style()
    
    fig, ax = plt.subplots(figsize=PLOT_CONFIG['figure_size'])
    
    for rao_name, rao_data in data.items():
        config = RAO_CONFIG[rao_name]
        ax.plot(rao_data['x'], rao_data['y'],
                color=config['color'],
                linestyle=config['linestyle'],
                marker=config['marker'],
                label=rao_name,
                linewidth=PLOT_CONFIG['line_width'])
    
    ax.set_xlabel(PLOT_CONFIG['x_label'])
    ax.set_ylabel(PLOT_CONFIG['y_label'])
    ax.set_title(f"{PLOT_CONFIG['main_title']}{title_suffix}")
    
    ax.legend(loc='upper right', framealpha=0.9, edgecolor='black', fancybox=False)
    ax.grid(True, alpha=PLOT_CONFIG['grid_alpha'], linestyle='--', linewidth=0.5)
    ax.set_xlim(0, PLOT_CONFIG['main_plot_xlim'])
    ax.set_ylim(bottom=0)
    
    ax.xaxis.set_minor_locator(MultipleLocator(0.1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))
    ax.grid(True, which='minor', alpha=0.1, linestyle=':', linewidth=0.3)
    
    plt.tight_layout()
    plt.savefig(filename, format=PLOT_CONFIG['save_format'], 
                dpi=PLOT_CONFIG['dpi'], bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.show()
    print(f"Figure saved: {filename}")


def create_separate_rao_plots(data, filename_prefix='rao_plot', title_suffix=''):
    """
    Generate individual subplots for each RAO type.
    
    Parameters
    ----------
    data : dict
        Parsed RAO data dictionary
    filename_prefix : str
        Output filename prefix
    title_suffix : str
        Additional title text
    """
    setup_academic_style()
    
    fig, axes = plt.subplots(2, 3, figsize=(14, 9))
    axes = axes.flatten()
    
    rao_names = list(data.keys())
    
    for i, rao_name in enumerate(rao_names):
        ax = axes[i]
        rao_data = data[rao_name]
        config = RAO_CONFIG[rao_name]
        
        ax.plot(rao_data['x'], rao_data['y'],
                color=config['color'],
                linestyle=config['linestyle'],
                marker=config['marker'],
                linewidth=PLOT_CONFIG['line_width'])
        
        ax.set_xlabel(PLOT_CONFIG['x_label'])
        ax.set_ylabel(f'{rao_name}')
        ax.set_title(rao_name)
        ax.grid(True, alpha=PLOT_CONFIG['grid_alpha'], linestyle='--', linewidth=0.5)
        ax.set_xlim(0, PLOT_CONFIG['subplot_xlim'])
        ax.set_ylim(bottom=0)
    
    # Hide last subplot
    axes[5].set_visible(False)
    
    fig.suptitle(f"{PLOT_CONFIG['main_title']}{title_suffix}", fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    filename = f"{filename_prefix}_subplots.{PLOT_CONFIG['save_format']}"
    plt.savefig(filename, format=PLOT_CONFIG['save_format'], 
                dpi=PLOT_CONFIG['dpi'], bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.show()
    print(f"Figure saved: {filename}")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Remote Location RAO Plot Generator")
    print("=" * 60)
    
    # Parse primary dataset
    print("\n[1] Processing primary dataset...")
    data1 = parse_data(DATA_STRING_1)
    
    # Generate single combined figure
    print("\n[2] Generating combined figure...")
    create_single_rao_plot(data1, 'rao_plot_dataset1.png', ' - Dataset 1')
    
    # Generate individual subplots
    print("\n[3] Generating subplot figure...")
    create_separate_rao_plots(data1, 'rao_dataset1', ' - Dataset 1')
    
    # Process second dataset if available
    if DATA_STRING_2 is not None:
        print("\n[4] Processing secondary dataset...")
        data2 = parse_data(DATA_STRING_2)
        print("Comparison plot available if needed.")
    else:
        print("\n[!] Secondary dataset not defined.")
        print("    Assign data to DATA_STRING_2 for comparison plots.")
    
    print("\n" + "=" * 60)
    print("Processing complete!")
    print("=" * 60)
