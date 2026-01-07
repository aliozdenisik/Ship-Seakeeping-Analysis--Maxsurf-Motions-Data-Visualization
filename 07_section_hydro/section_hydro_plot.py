#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Section Hydrodynamic Coefficients Visualization

Generates publication-quality figures for sectional hydrodynamic coefficients
including added mass, damping, and wave excitation forces from strip theory analysis.

Data source: Maxsurf Motions Section Hydrodynamic Coefficients output
Methodology: Strip Theory (Salvesen, Tuck & Faltinsen, 1970)
Wave heading: Beam seas (90°)

Author: Ali Özden Işık
Institution: Istanbul Technical University - Naval Architecture and Marine Engineering
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import warnings
import os

warnings.filterwarnings('ignore')

# =============================================================================
# ACADEMIC STYLE SETTINGS
# =============================================================================

plt.rcParams['font.family'] = 'DejaVu Sans'

# Raw data from Maxsurf Motions (tab-separated, comma decimal)
raw_data = """0,240000	3,242285	0,240000	0,251572	0,240000	7,166431	0,240000	12,945210	0,240000	0,006836	0,240000	0,923290	0,240000	-157,335872
0,257778	3,291570	0,257778	0,290751	0,257778	7,166431	0,257778	12,741869	0,257778	0,007966	0,257778	1,093996	0,257778	-152,100481
0,275556	3,319676	0,275556	0,330887	0,275556	7,166431	0,275556	12,526819	0,275556	0,009202	0,275556	1,276823	0,275556	-146,391866
0,293333	3,326652	0,293333	0,369780	0,293333	7,166431	0,293333	12,300601	0,293333	0,010550	0,293333	1,467821	0,293333	-140,134480
0,311111	3,314520	0,311111	0,405016	0,311111	7,166431	0,311111	12,063780	0,311111	0,012017	0,311111	1,662480	0,311111	-133,253414
0,328889	3,286838	0,328889	0,434409	0,328889	7,166431	0,328889	11,816942	0,328889	0,013612	0,328889	1,856439	0,328889	-125,687386
0,346667	3,248034	0,346667	0,456425	0,346667	7,166431	0,346667	11,560694	0,346667	0,015342	0,346667	2,046157	0,346667	-117,398664
0,364444	3,202677	0,364444	0,470401	0,364444	7,166431	0,364444	11,295656	0,364444	0,017217	0,364444	2,229347	0,364444	-108,377036
0,382222	3,154883	0,382222	0,476525	0,382222	7,166431	0,382222	11,022464	0,382222	0,019248	0,382222	2,405043	0,382222	-98,637571
0,400000	3,107947	0,400000	0,475623	0,400000	7,166431	0,400000	10,741766	0,400000	0,021447	0,400000	2,573381	0,400000	-88,214102
0,419048	3,061259	0,419048	0,468195	0,419048	7,166431	0,419048	10,433435	0,419048	0,024005	0,419048	2,746568	0,419048	-76,337710
0,438095	3,020014	0,438095	0,455595	0,438095	7,166431	0,438095	10,118057	0,438095	0,026792	0,438095	2,913790	0,438095	-63,785817
0,457143	2,985062	0,457143	0,439241	0,457143	7,166431	0,457143	9,796456	0,457143	0,029827	0,457143	3,076564	0,457143	-50,613640
0,476190	2,956599	0,476190	0,420307	0,476190	7,166431	0,476190	9,469456	0,476190	0,033136	0,476190	3,236180	0,476190	-36,868629
0,495238	2,934409	0,495238	0,399692	0,495238	7,166431	0,495238	9,137881	0,495238	0,036746	0,495238	3,393592	0,495238	-22,588831
0,514286	2,918051	0,514286	0,378056	0,514286	7,166431	0,514286	8,802551	0,514286	0,040689	0,514286	3,549396	0,514286	-7,803115
0,533333	2,906981	0,533333	0,355861	0,533333	7,166431	0,533333	8,464279	0,533333	0,045002	0,533333	3,703874	0,533333	7,467608
0,552381	2,900631	0,552381	0,333430	0,552381	7,166431	0,552381	8,123868	0,552381	0,049727	0,552381	3,857053	0,552381	23,208799
0,571429	2,898455	0,571429	0,310988	0,571429	7,166431	0,571429	7,782109	0,571429	0,054913	0,571429	4,008770	0,571429	39,410731
0,590476	2,899947	0,590476	0,288695	0,590476	7,166431	0,590476	7,439774	0,590476	0,060615	0,590476	4,158734	0,590476	56,067164
0,609524	2,904649	0,609524	0,266676	0,609524	7,166431	0,609524	7,097621	0,609524	0,066899	0,609524	4,306571	0,609524	73,174301
0,628571	2,912147	0,628571	0,245036	0,628571	7,166431	0,628571	6,756383	0,628571	0,073841	0,628571	4,451872	0,628571	90,730028
0,647619	2,922068	0,647619	0,223868	0,647619	7,166431	0,647619	6,416773	0,647619	0,081531	0,647619	4,594218	0,647619	108,733392
0,666667	2,934072	0,666667	0,203263	0,666667	7,166431	0,666667	6,079477	0,666667	0,090076	0,666667	4,733208	0,666667	127,184258
0,685714	2,947848	0,685714	0,183312	0,685714	7,166431	0,685714	5,745156	0,685714	0,099601	0,685714	4,868473	0,685714	146,083100
0,704762	2,963106	0,704762	0,164102	0,704762	7,166431	0,704762	5,414440	0,704762	0,110256	0,704762	4,999690	0,704762	165,430878
0,723810	2,979578	0,723810	0,145722	0,723810	7,166431	0,723810	5,087928	0,723810	0,122224	0,723810	5,126585	0,723810	-174,771034
0,742857	2,997009	0,742857	0,128255	0,742857	7,166431	0,742857	4,766191	0,742857	0,135725	0,742857	5,248941	0,742857	-154,520893
0,761905	3,015164	0,761905	0,111776	0,761905	7,166431	0,761905	4,449762	0,761905	0,151028	0,761905	5,366598	0,761905	-133,816619
0,780952	3,033821	0,780952	0,096355	0,780952	7,166431	0,780952	4,139144	0,780952	0,168467	0,780952	5,479447	0,780952	-112,655831
0,800000	3,052774	0,800000	0,082049	0,800000	7,166431	0,800000	3,834803	0,800000	0,188460	0,800000	5,587433	0,800000	-91,035882
0,819048	3,071833	0,819048	0,068901	0,819048	7,166431	0,819048	3,537172	0,819048	0,211532	0,819048	5,690546	0,819048	-68,953906
0,838095	3,090825	0,838095	0,056945	0,838095	7,166431	0,838095	3,246645	0,838095	0,238362	0,838095	5,788818	0,838095	-46,406862
0,857143	3,109592	0,857143	0,046196	0,857143	7,166431	0,857143	2,963583	0,857143	0,269831	0,857143	5,882319	0,857143	-23,391588
0,876190	3,127996	0,876190	0,036659	0,876190	7,166431	0,876190	2,688311	0,876190	0,307109	0,876190	5,971149	0,876190	0,095151
0,895238	3,145915	0,895238	0,028323	0,895238	7,166431	0,895238	2,421115	0,895238	0,351781	0,895238	6,055433	0,895238	24,056613
0,914286	3,163244	0,914286	0,021165	0,914286	7,166431	0,914286	2,162250	0,914286	0,406046	0,914286	6,135319	0,914286	48,496035
0,933333	3,179896	0,933333	0,015151	0,933333	7,166431	0,933333	1,911932	0,933333	0,473047	0,933333	6,210968	0,933333	73,416593
0,952381	3,195798	0,952381	0,010234	0,952381	7,166431	0,952381	1,670346	0,952381	0,557428	0,952381	6,282550	0,952381	98,821369
0,971429	3,210896	0,971429	0,006362	0,971429	7,166431	0,971429	1,437642	0,971429	0,666361	0,971429	6,350244	0,971429	124,713328
0,990476	3,225146	0,990476	0,003473	0,990476	7,166431	0,990476	1,213938	0,990476	0,811512	0,990476	6,414226	0,990476	151,095288
1,009524	3,238521	1,009524	0,001498	1,009524	7,166431	1,009524	0,999321	1,009524	1,013219	1,009524	6,474660	1,009524	177,969913
1,028571	3,251002	1,028571	0,000366	1,028571	7,166431	1,028571	0,793853	1,028571	1,310368	1,028571	6,531647	1,028571	-154,660300
1,047619	3,261528	1,047619	0,000001	1,047619	7,166431	1,047619	0,597572	1,047619	1,787732	1,047619	6,558153	1,047619	-126,793048
1,066667	3,273320	1,066667	0,000325	1,066667	7,166431	1,066667	0,410512	1,066667	2,671846	1,066667	6,637145	1,066667	-98,426133
1,085714	3,283141	1,085714	0,001261	1,085714	7,166431	1,085714	0,232800	1,085714	4,838587	1,085714	6,685048	1,085714	-69,557639
1,104762	3,292113	1,104762	0,002732	1,104762	7,166431	1,104762	0,066080	1,104762	17,747911	1,104762	6,730308	1,104762	-40,185752
1,123810	3,300260	1,123810	0,004660	1,123810	7,166431	1,123810	0,099294	1,123810	167,992723	1,123810	6,772965	1,123810	-10,308847
1,142857	3,307614	1,142857	0,006971	1,142857	7,166431	1,142857	0,249204	1,142857	175,125071	1,142857	6,813106	1,142857	20,074538
1,161905	3,314215	1,161905	0,009596	1,161905	7,166431	1,161905	0,391336	1,161905	176,820345	1,161905	6,850811	1,161905	50,965710
1,180952	3,320101	1,180952	0,012465	1,180952	7,166431	1,180952	0,525032	1,180952	177,571933	1,180952	6,886147	1,180952	82,365826
1,200000	3,325316	1,200000	0,015515	1,200000	7,166431	1,200000	0,650346	1,200000	177,991925	1,200000	6,919169	1,200000	114,275904
1,219048	3,329907	1,219048	0,018687	1,219048	7,166431	1,219048	0,767426	1,219048	178,256983	1,219048	6,949916	1,219048	146,696829
1,238095	3,333918	1,238095	0,021926	1,238095	7,166431	1,238095	0,876454	1,238095	178,437015	1,238095	6,978415	1,238095	179,629362
1,257143	3,337395	1,257143	0,025183	1,257143	7,166431	1,257143	0,977633	1,257143	178,565211	1,257143	7,004680	1,257143	-146,925850
1,276190	3,340385	1,276190	0,028412	1,276190	7,166431	1,276190	1,071180	1,276190	178,659341	1,276190	7,028714	1,276190	-112,968264
1,295238	3,342933	1,295238	0,031573	1,295238	7,166431	1,295238	1,157321	1,295238	178,729767	1,295238	7,050512	1,295238	-78,497437
1,314286	3,345084	1,314286	0,034632	1,314286	7,166431	1,314286	1,236297	1,314286	178,782933	1,314286	7,070060	1,314286	-43,513013
1,333333	3,346878	1,333333	0,037559	1,333333	7,166431	1,333333	1,308352	1,333333	178,823048	1,333333	7,087338	1,333333	-8,014717
1,352381	3,348358	1,352381	0,040327	1,352381	7,166431	1,352381	1,373739	1,352381	178,852974	1,352381	7,102323	1,352381	27,997653
1,371429	3,349561	1,371429	0,042915	1,371429	7,166431	1,371429	1,432714	1,371429	178,874717	1,371429	7,114988	1,371429	64,524236
1,390476	3,350525	1,390476	0,045308	1,390476	7,166431	1,390476	1,485540	1,390476	178,889721	1,390476	7,125304	1,390476	101,565111
1,409524	3,351283	1,409524	0,047492	1,409524	7,166431	1,409524	1,532479	1,409524	178,899046	1,409524	7,133244	1,409524	139,120307
1,428571	3,351866	1,428571	0,049457	1,428571	7,166431	1,428571	1,573797	1,428571	178,903483	1,428571	7,138781	1,428571	177,189810
1,447619	3,352304	1,447619	0,051198	1,447619	7,166431	1,447619	1,609756	1,447619	178,903631	1,447619	7,141892	1,447619	-144,226433
1,466667	3,352624	1,466667	0,052712	1,466667	7,166431	1,466667	1,640623	1,466667	178,899947	1,466667	7,142556	1,466667	-105,128506
1,485714	3,352849	1,485714	0,053998	1,485714	7,166431	1,485714	1,666658	1,485714	178,892781	1,485714	7,140758	1,485714	-65,516520
1,504762	3,353002	1,504762	0,055060	1,504762	7,166431	1,504762	1,688122	1,504762	178,882401	1,504762	7,136489	1,504762	-25,390609
1,523810	3,353102	1,523810	0,055902	1,523810	7,166431	1,523810	1,705270	1,523810	178,869016	1,523810	7,129745	1,523810	15,249078
1,542857	3,353166	1,542857	0,056530	1,542857	7,166431	1,542857	1,718355	1,542857	178,852781	1,542857	7,120529	1,542857	56,402376
1,561905	3,353210	1,561905	0,056952	1,561905	7,166431	1,561905	1,727622	1,561905	178,833813	1,561905	7,108851	1,561905	98,069115
1,580952	3,353247	1,580952	0,057178	1,580952	7,166431	1,580952	1,733315	1,580952	178,812197	1,580952	7,094728	1,580952	140,249116
1,600000	3,353288	1,600000	0,057217	1,600000	7,166431	1,600000	1,735668	1,600000	178,787991	1,600000	7,078186	1,600000	-177,057803
1,677778	3,353672	1,677778	0,055687	1,677778	7,166431	1,677778	1,715327	1,677778	178,662764	1,677778	6,986309	1,677778	2,593487
1,755556	3,354657	1,755556	0,052063	1,755556	7,166431	1,755556	1,657310	1,755556	178,494460	1,755556	6,858112	1,755556	-169,214925
1,833333	3,356352	1,833333	0,047150	1,833333	7,166431	1,833333	1,573785	1,833333	178,279916	1,833333	6,698538	1,833333	27,507344
1,911111	3,358685	1,911111	0,041633	1,911111	7,166431	1,911111	1,474678	1,911111	178,014026	1,911111	6,513574	1,911111	-127,246721
1,988889	3,361504	1,988889	0,036031	1,988889	7,166431	1,988889	1,367764	1,988889	177,690300	1,988889	6,309649	1,988889	86,518378
2,066667	3,364630	2,066667	0,030699	2,066667	7,166431	2,066667	1,258876	2,066667	177,301210	2,066667	6,093083	2,066667	-51,199786
2,144444	3,367901	2,144444	0,025846	2,144444	7,166431	2,144444	1,152178	2,144444	176,838442	2,144444	5,869674	2,144444	179,597870
2,222222	3,371185	2,222222	0,021570	2,222222	7,166431	2,222222	1,050454	2,222222	176,293124	2,222222	5,644425	2,222222	58,911423
2,300000	3,374384	2,300000	0,017892	2,300000	7,166431	2,300000	0,955408	2,300000	175,656025	2,300000	5,421417	2,300000	-53,258480
2,377778	3,377432	2,377778	0,014785	2,377778	7,166431	2,377778	0,867920	2,377778	174,917756	2,377778	5,203783	2,377778	-156,910924
2,455556	3,380291	2,455556	0,012194	2,455556	7,166431	2,455556	0,788280	2,455556	174,068928	2,455556	4,993776	2,455556	107,955076
2,533333	3,382942	2,533333	0,010054	2,533333	7,166431	2,533333	0,716370	2,533333	173,100293	2,533333	4,792875	2,533333	21,340461
2,611111	3,385382	2,611111	0,008296	2,611111	7,166431	2,611111	0,651814	2,611111	172,002844	2,611111	4,601917	2,611111	-56,753937
2,688889	3,387615	2,688889	0,006859	2,688889	7,166431	2,688889	0,594087	2,688889	170,767896	2,688889	4,421236	2,688889	-126,327405
2,766667	3,389653	2,766667	0,005686	2,766667	7,166431	2,766667	0,542592	2,766667	169,387132	2,766667	4,250788	2,766667	172,620641
2,844444	3,391509	2,844444	0,004728	2,844444	7,166431	2,844444	0,496719	2,844444	167,852657	2,844444	4,090263	2,844444	120,090675
2,922222	3,393199	2,922222	0,003945	2,922222	7,166431	2,922222	0,455877	2,922222	166,157052	2,922222	3,939176	2,922222	76,083071
3,000000	3,394738	3,000000	0,003304	3,000000	7,166431	3,000000	0,419514	3,000000	164,293459	3,000000	3,796941	3,000000	40,598127"""

# =============================================================================
# DATA PROCESSING
# =============================================================================

lines = raw_data.strip().split('\n')
data = []
for line in lines:
    values = [float(v.replace(',', '.')) for v in line.split('\t')]
    data.append(values)

data = np.array(data)

# Extract columns
frequency = data[:, 0]              # Encounter Frequency (rad/s)
added_mass = data[:, 1]             # Added mass (t/m)
damping = data[:, 3]                # Damping (t/(m·s))
stiffness = data[:, 5]              # Stiffness (t/(m·s²)) - constant
froude_krylov_amp = data[:, 7]      # Froude-Krylov Amplitude (kN/m²)
froude_krylov_phase = data[:, 9]    # Froude-Krylov Phase (deg)
diffraction_amp = data[:, 11]       # Diffraction Amplitude (kN/m²)
diffraction_phase = data[:, 13]     # Diffraction Phase (deg)

# =============================================================================
# ACADEMIC STYLE SETTINGS
# =============================================================================

plt.style.use('seaborn-v0_8-whitegrid')

# Color palette
colors = {
    'added_mass': '#1f77b4',
    'damping': '#2ca02c',
    'stiffness': '#d62728',
    'froude_amp': '#9467bd',
    'froude_phase': '#8c564b',
    'diffraction_amp': '#e377c2',
    'diffraction_phase': '#ff7f0e'
}

# =============================================================================
# FIGURE 1: Added Mass and Damping Coefficients
# =============================================================================

fig1, ax1 = plt.subplots(figsize=(10, 6), dpi=150)

# Added Mass (left axis)
line1, = ax1.plot(frequency, added_mass, color=colors['added_mass'], 
                   linewidth=2, label='Added Mass ($a_{33}$)')
ax1.set_xlabel('Encounter Frequency (rad/s)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Added Mass, $a_{33}$ (t/m)', fontsize=12, fontweight='bold', 
               color=colors['added_mass'])
ax1.tick_params(axis='y', labelcolor=colors['added_mass'])
ax1.set_xlim([0, 3.2])

# Damping (right axis)
ax1_twin = ax1.twinx()
line2, = ax1_twin.plot(frequency, damping, color=colors['damping'], 
                        linewidth=2, linestyle='--', label='Damping ($b_{33}$)')
ax1_twin.set_ylabel('Damping, $b_{33}$ (t/(m·s))', fontsize=12, fontweight='bold',
                    color=colors['damping'])
ax1_twin.tick_params(axis='y', labelcolor=colors['damping'])

# Grid and legend
ax1.grid(True, linestyle='-', alpha=0.3)
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())
lines = [line1, line2]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right', fontsize=10, framealpha=0.9)

ax1.set_title('Section Hydrodynamic Coefficients: Added Mass and Damping', 
              fontsize=14, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('fig1_added_mass_damping.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('fig1_added_mass_damping.svg', format='svg', bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Figure 1 saved: fig1_added_mass_damping.png/svg")

# =============================================================================
# FIGURE 2: Wave Excitation Forces (Froude-Krylov and Diffraction)
# =============================================================================

fig2, (ax2a, ax2b) = plt.subplots(2, 1, figsize=(10, 8), dpi=150, sharex=True)

# Upper panel: Amplitudes
ax2a.plot(frequency, froude_krylov_amp, color=colors['froude_amp'], 
          linewidth=2, label='Froude-Krylov')
ax2a.plot(frequency, diffraction_amp, color=colors['diffraction_amp'], 
          linewidth=2, linestyle='--', label='Diffraction')
ax2a.set_ylabel('Wave Excitation Force\nAmplitude (kN/m²)', fontsize=11, fontweight='bold')
ax2a.legend(loc='upper right', fontsize=10, framealpha=0.9)
ax2a.grid(True, linestyle='-', alpha=0.3)
ax2a.xaxis.set_minor_locator(AutoMinorLocator())
ax2a.yaxis.set_minor_locator(AutoMinorLocator())
ax2a.set_title('Section Wave Excitation Forces (Heave)', fontsize=14, fontweight='bold', pad=10)

# Lower panel: Phases
ax2b.plot(frequency, froude_krylov_phase, color=colors['froude_phase'], 
          linewidth=2, label='Froude-Krylov Phase')
ax2b.plot(frequency, diffraction_phase, color=colors['diffraction_phase'], 
          linewidth=2, linestyle='--', label='Diffraction Phase')
ax2b.set_xlabel('Encounter Frequency (rad/s)', fontsize=12, fontweight='bold')
ax2b.set_ylabel('Phase (deg)', fontsize=11, fontweight='bold')
ax2b.set_ylim([-200, 200])
ax2b.set_yticks([-180, -90, 0, 90, 180])
ax2b.legend(loc='upper right', fontsize=10, framealpha=0.9)
ax2b.grid(True, linestyle='-', alpha=0.3)
ax2b.xaxis.set_minor_locator(AutoMinorLocator())
ax2b.set_xlim([0, 3.2])

plt.tight_layout()
plt.savefig('fig2_wave_excitation.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.savefig('fig2_wave_excitation.svg', format='svg', bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Figure 2 saved: fig2_wave_excitation.png/svg")

# =============================================================================
# FIGURE 3: All Coefficients - Combined View (4 Panel)
# =============================================================================

fig3, axes = plt.subplots(2, 2, figsize=(12, 9), dpi=150)

# Panel (a): Added Mass
ax_a = axes[0, 0]
ax_a.plot(frequency, added_mass, color=colors['added_mass'], linewidth=2)
ax_a.set_ylabel('$a_{33}$ (t/m)', fontsize=11, fontweight='bold')
ax_a.set_title('(a) Added Mass', fontsize=12, fontweight='bold')
ax_a.grid(True, linestyle='-', alpha=0.3)
ax_a.xaxis.set_minor_locator(AutoMinorLocator())
ax_a.yaxis.set_minor_locator(AutoMinorLocator())
ax_a.set_xlim([0, 3.2])

# Panel (b): Damping
ax_b = axes[0, 1]
ax_b.plot(frequency, damping, color=colors['damping'], linewidth=2)
ax_b.set_ylabel('$b_{33}$ (t/(m·s))', fontsize=11, fontweight='bold')
ax_b.set_title('(b) Damping', fontsize=12, fontweight='bold')
ax_b.grid(True, linestyle='-', alpha=0.3)
ax_b.xaxis.set_minor_locator(AutoMinorLocator())
ax_b.yaxis.set_minor_locator(AutoMinorLocator())
ax_b.set_xlim([0, 3.2])

# Panel (c): Froude-Krylov Excitation
ax_c = axes[1, 0]
ax_c.plot(frequency, froude_krylov_amp, color=colors['froude_amp'], linewidth=2, label='Amplitude')
ax_c_twin = ax_c.twinx()
ax_c_twin.plot(frequency, froude_krylov_phase, color=colors['froude_phase'], 
               linewidth=1.5, linestyle=':', label='Phase')
ax_c.set_xlabel('Encounter Frequency (rad/s)', fontsize=11, fontweight='bold')
ax_c.set_ylabel('Amplitude (kN/m²)', fontsize=10, fontweight='bold', color=colors['froude_amp'])
ax_c_twin.set_ylabel('Phase (deg)', fontsize=10, fontweight='bold', color=colors['froude_phase'])
ax_c.set_title('(c) Froude-Krylov Wave Excitation', fontsize=12, fontweight='bold')
ax_c.grid(True, linestyle='-', alpha=0.3)
ax_c.tick_params(axis='y', labelcolor=colors['froude_amp'])
ax_c_twin.tick_params(axis='y', labelcolor=colors['froude_phase'])
ax_c_twin.set_ylim([-200, 200])
ax_c.set_xlim([0, 3.2])

# Panel (d): Diffraction Excitation
ax_d = axes[1, 1]
ax_d.plot(frequency, diffraction_amp, color=colors['diffraction_amp'], linewidth=2, label='Amplitude')
ax_d_twin = ax_d.twinx()
ax_d_twin.plot(frequency, diffraction_phase, color=colors['diffraction_phase'], 
               linewidth=1.5, linestyle=':', label='Phase')
ax_d.set_xlabel('Encounter Frequency (rad/s)', fontsize=11, fontweight='bold')
ax_d.set_ylabel('Amplitude (kN/m²)', fontsize=10, fontweight='bold', color=colors['diffraction_amp'])
ax_d_twin.set_ylabel('Phase (deg)', fontsize=10, fontweight='bold', color=colors['diffraction_phase'])
ax_d.set_title('(d) Diffraction Wave Excitation', fontsize=12, fontweight='bold')
ax_d.grid(True, linestyle='-', alpha=0.3)
ax_d.tick_params(axis='y', labelcolor=colors['diffraction_amp'])
ax_d_twin.tick_params(axis='y', labelcolor=colors['diffraction_phase'])
ax_d_twin.set_ylim([-200, 200])
ax_d.set_xlim([0, 3.2])

fig3.suptitle('Section Hydrodynamic Coefficients (Heave Mode)', 
              fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('fig3_all_coefficients.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.savefig('fig3_all_coefficients.svg', format='svg', bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Figure 3 saved: fig3_all_coefficients.png/svg")

# =============================================================================
# FIGURE 4: Amplitude Comparison Only
# =============================================================================

fig4, ax4 = plt.subplots(figsize=(10, 6), dpi=150)

ax4.plot(frequency, froude_krylov_amp, color='#2E86AB', linewidth=2.5, 
         label='Froude-Krylov Wave Excitation', marker='o', markersize=3, markevery=5)
ax4.plot(frequency, diffraction_amp, color='#A23B72', linewidth=2.5, 
         label='Diffraction Wave Excitation', marker='s', markersize=3, markevery=5)

ax4.set_xlabel('Encounter Frequency (rad/s)', fontsize=12, fontweight='bold')
ax4.set_ylabel('Wave Excitation Force per Unit\nWave Amplitude (kN/m²)', fontsize=11, fontweight='bold')
ax4.set_title('Comparison of Wave Excitation Components (Heave)', 
              fontsize=14, fontweight='bold', pad=15)
ax4.legend(loc='upper right', fontsize=11, framealpha=0.95)
ax4.grid(True, linestyle='-', alpha=0.3)
ax4.xaxis.set_minor_locator(AutoMinorLocator())
ax4.yaxis.set_minor_locator(AutoMinorLocator())
ax4.set_xlim([0, 3.2])
ax4.set_ylim([0, 14])

plt.tight_layout()
plt.savefig('fig4_excitation_comparison.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.savefig('fig4_excitation_comparison.svg', format='svg', bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Figure 4 saved: fig4_excitation_comparison.png/svg")

plt.show()

print("\n" + "="*60)
print("All figures generated successfully!")
print("PNG format: High resolution images (300 DPI)")
print("SVG format: Vector graphics (ideal for academic publications)")
print("="*60)
