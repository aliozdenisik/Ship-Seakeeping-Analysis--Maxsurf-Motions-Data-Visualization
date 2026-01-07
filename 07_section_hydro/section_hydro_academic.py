# -*- coding: utf-8 -*-
"""
Maxsurf Motion - Section Hydrodynamic Coefficients
Publication-Quality Academic Figures

Reference: Strip Theory methodology (Salvesen, Tuck & Faltinsen, 1970)
Standard presentation format for academic literature.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
import warnings
import os
warnings.filterwarnings('ignore')

# Create output directory for head seas (180 deg)
output_dir = 'output/head_seas'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# ============================================================================
# MATPLOTLIB SETTINGS FOR ACADEMIC PUBLICATIONS
# ============================================================================
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Georgia'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'axes.linewidth': 0.8,
    'lines.linewidth': 1.5,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'text.usetex': False,
    'mathtext.fontset': 'stix',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linewidth': 0.5,
    'grid.linestyle': '-'
})

# ============================================================================
# DATA LOADING AND PROCESSING
# ============================================================================
raw_data = """0,360002	3,214387	0,360002	0,467665	0,360002	7,166431	0,360002	12,226009	0,360002	62,993674	0,360002	0,326072	0,360002	-139,011893
0,364446	3,202671	0,364446	0,470402	0,364446	7,166431	0,364446	12,184185	0,364446	64,328750	0,364446	0,331310	0,364446	-137,621497
0,368891	3,190808	0,368891	0,472645	0,368891	7,166431	0,368891	12,142165	0,368891	65,673710	0,368891	0,336499	0,368891	-136,204094
0,373335	3,178853	0,373335	0,474405	0,373335	7,166431	0,373335	12,099954	0,373335	67,028464	0,373335	0,341642	0,373335	-134,760221
0,377779	3,166860	0,377779	0,475693	0,377779	7,166431	0,377779	12,057558	0,377779	68,392924	0,377779	0,346746	0,377779	-133,290481
0,382223	3,154880	0,382223	0,476525	0,382223	7,166431	0,382223	12,014980	0,382223	69,767004	0,382223	0,351813	0,382223	-131,795532
0,386668	3,142958	0,386668	0,476916	0,386668	7,166431	0,386668	11,972227	0,386668	71,150617	0,386668	0,356850	0,386668	-130,276080
0,391112	3,131137	0,391112	0,476884	0,391112	7,166431	0,391112	11,929301	0,391112	72,543680	0,391112	0,361861	0,391112	-128,732873
0,395556	3,119454	0,395556	0,476447	0,395556	7,166431	0,395556	11,886209	0,395556	73,946110	0,395556	0,366850	0,395556	-127,166688
0,400001	3,107945	0,400001	0,475623	0,400001	7,166431	0,400001	11,842955	0,400001	75,357824	0,400001	0,371822	0,400001	-125,578328
0,419048	3,061258	0,419048	0,468195	0,419048	7,166431	0,419048	11,655852	0,419048	81,511303	0,419048	0,393056	0,419048	-118,539508
0,438095	3,020014	0,438095	0,455594	0,438095	7,166431	0,438095	11,466199	0,438095	87,827754	0,438095	0,414415	0,438095	-111,173423
0,457143	2,985062	0,457143	0,439241	0,457143	7,166431	0,457143	11,274326	0,457143	94,301425	0,457143	0,436187	0,457143	-103,541043
0,476191	2,956599	0,476191	0,420307	0,476191	7,166431	0,476191	11,080541	0,476191	100,926893	0,476191	0,458592	0,476191	-95,695241
0,495238	2,934409	0,495238	0,399692	0,495238	7,166431	0,495238	10,885138	0,495238	107,699039	0,495238	0,481781	0,495238	-87,679184
0,514286	2,918051	0,514286	0,378056	0,514286	7,166431	0,514286	10,688392	0,514286	114,613028	0,514286	0,505853	0,514286	-79,526577
0,533333	2,906981	0,533333	0,355861	0,533333	7,166431	0,533333	10,490566	0,533333	121,664283	0,533333	0,530861	0,533333	-71,262909
0,552381	2,900631	0,552381	0,333430	0,552381	7,166431	0,552381	10,291904	0,552381	128,848467	0,552381	0,556822	0,552381	-62,907054
0,571429	2,898455	0,571429	0,310988	0,571429	7,166431	0,571429	10,092640	0,571429	136,161468	0,571429	0,583729	0,571429	-54,472852
0,590476	2,899947	0,590476	0,288695	0,590476	7,166431	0,590476	9,892993	0,590476	143,599383	0,590476	0,611553	0,590476	-45,970446
0,609524	2,904649	0,609524	0,266676	0,609524	7,166431	0,609524	9,693169	0,609524	151,158500	0,609524	0,640251	0,609524	-37,407346
0,628571	2,912147	0,628571	0,245036	0,628571	7,166431	0,628571	9,493364	0,628571	158,835289	0,628571	0,669766	0,628571	-28,789195
0,647619	2,922068	0,647619	0,223868	0,647619	7,166431	0,647619	9,293761	0,647619	166,626386	0,647619	0,700031	0,647619	-20,120310
0,666667	2,934072	0,666667	0,203263	0,666667	7,166431	0,666667	9,094533	0,666667	174,528586	0,666667	0,730967	0,666667	-11,404031
0,685714	2,947848	0,685714	0,183312	0,685714	7,166431	0,685714	8,895841	0,685714	-177,461169	0,685714	0,762490	0,685714	-2,642943
0,704762	2,963106	0,704762	0,164102	0,704762	7,166431	0,704762	8,697839	0,704762	-169,345800	0,704762	0,794505	0,704762	6,160995
0,723810	2,979578	0,723810	0,145722	0,723810	7,166431	0,723810	8,500670	0,723810	-161,128099	0,723810	0,826913	0,723810	15,006363
0,742857	2,997009	0,742857	0,128255	0,742857	7,166431	0,742857	8,304468	0,742857	-152,810734	0,742857	0,859608	0,742857	23,892237
0,761905	3,015164	0,761905	0,111776	0,761905	7,166431	0,761905	8,109358	0,761905	-144,396263	0,761905	0,892483	0,761905	32,818138
0,780952	3,033821	0,780952	0,096355	0,780952	7,166431	0,780952	7,915459	0,780952	-135,887134	0,780952	0,925425	0,780952	41,784001
0,800000	3,052774	0,800000	0,082049	0,800000	7,166431	0,800000	7,722881	0,800000	-127,285693	0,800000	0,958323	0,800000	50,790125
0,819048	3,071833	0,819048	0,068901	0,819048	7,166431	0,819048	7,531727	0,819048	-118,594194	0,819048	0,991068	0,819048	59,837124
0,838095	3,090825	0,838095	0,056945	0,838095	7,166431	0,838095	7,342091	0,838095	-109,814796	0,838095	1,023549	0,838095	68,925876
0,857143	3,109592	0,857143	0,046196	0,857143	7,166431	0,857143	7,154063	0,857143	-100,949578	0,857143	1,055664	0,857143	78,057469
0,876190	3,127996	0,876190	0,036659	0,876190	7,166431	0,876190	6,967726	0,876190	-92,000536	0,876190	1,087312	0,876190	87,233140
0,895238	3,145915	0,895238	0,028323	0,895238	7,166431	0,895238	6,783156	0,895238	-82,969588	0,895238	1,118399	0,895238	96,454228
0,914286	3,163244	0,914286	0,021165	0,914286	7,166431	0,914286	6,600424	0,914286	-73,858583	0,914286	1,148839	0,914286	105,722121
0,933333	3,179896	0,933333	0,015151	0,933333	7,166431	0,933333	6,419595	0,933333	-64,669300	0,933333	1,178551	0,933333	115,038218
0,952381	3,195798	0,952381	0,010234	0,952381	7,166431	0,952381	6,240729	0,952381	-55,403454	0,952381	1,207464	0,952381	124,403885
0,971429	3,210896	0,971429	0,006362	0,971429	7,166431	0,971429	6,063881	0,971429	-46,062697	0,971429	1,235513	0,971429	133,820433
0,990476	3,225146	0,990476	0,003473	0,990476	7,166431	0,990476	5,889101	0,990476	-36,648623	0,990476	1,262642	0,990476	143,289089
1,009524	3,238521	1,009524	0,001498	1,009524	7,166431	1,009524	5,716436	1,009524	-27,162770	1,009524	1,288803	1,009524	152,810978
1,028571	3,251002	1,028571	0,000366	1,028571	7,166431	1,028571	5,545926	1,028571	-17,606625	1,028571	1,313954	1,028571	162,387110
1,047619	3,261528	1,047619	0,000001	1,047619	7,166431	1,047619	5,377608	1,047619	-7,981620	1,047619	1,337604	1,047619	172,018355
1,066667	3,273320	1,066667	0,000325	1,066667	7,166431	1,066667	5,211517	1,066667	1,710856	1,066667	1,361124	1,066667	-178,294477
1,085714	3,283141	1,085714	0,001261	1,085714	7,166431	1,085714	5,047681	1,085714	11,469464	1,085714	1,383083	1,085714	-168,550809
1,104762	3,292113	1,104762	0,002732	1,104762	7,166431	1,104762	4,886126	1,104762	21,292906	1,104762	1,403949	1,104762	-158,750125
1,123810	3,300260	1,123810	0,004660	1,123810	7,166431	1,123810	4,726876	1,123810	31,179928	1,123810	1,423712	1,123810	-148,892056
1,142857	3,307614	1,142857	0,006971	1,142857	7,166431	1,142857	4,569950	1,142857	41,129314	1,142857	1,442373	1,142857	-138,976352
1,161905	3,314215	1,161905	0,009596	1,161905	7,166431	1,161905	4,415364	1,161905	51,139888	1,161905	1,459937	1,161905	-129,002885
1,180952	3,320101	1,180952	0,012465	1,180952	7,166431	1,180952	4,263132	1,180952	61,210509	1,180952	1,476412	1,180952	-118,971638
1,200000	3,325316	1,200000	0,015515	1,200000	7,166431	1,200000	4,113265	1,200000	71,340073	1,200000	1,491813	1,200000	-108,882698
1,219048	3,329907	1,219048	0,018687	1,219048	7,166431	1,219048	3,965770	1,219048	81,527506	1,219048	1,506155	1,219048	-98,736252
1,238095	3,333918	1,238095	0,021926	1,238095	7,166431	1,238095	3,820655	1,238095	91,771771	1,238095	1,519460	1,238095	-88,532579
1,257143	3,337395	1,257143	0,025183	1,257143	7,166431	1,257143	3,677922	1,257143	102,071857	1,257143	1,531749	1,257143	-78,272039
1,276190	3,340385	1,276190	0,028412	1,276190	7,166431	1,276190	3,537572	1,276190	112,426786	1,276190	1,543048	1,276190	-67,955071
1,295238	3,342933	1,295238	0,031573	1,295238	7,166431	1,295238	3,399606	1,295238	122,835606	1,295238	1,553384	1,295238	-57,582182
1,314286	3,345084	1,314286	0,034632	1,314286	7,166431	1,314286	3,264019	1,314286	133,297393	1,314286	1,562783	1,314286	-47,153940
1,333333	3,346878	1,333333	0,037559	1,333333	7,166431	1,333333	3,130808	1,333333	143,811250	1,333333	1,571276	1,333333	-36,670967
1,352381	3,348358	1,352381	0,040327	1,352381	7,166431	1,352381	2,999966	1,352381	154,376303	1,352381	1,578892	1,352381	-26,133934
1,371429	3,349561	1,371429	0,042915	1,371429	7,166431	1,371429	2,871486	1,371429	164,991705	1,371429	1,585660	1,371429	-15,543553
1,390476	3,350525	1,390476	0,045308	1,390476	7,166431	1,390476	2,745357	1,390476	175,656629	1,390476	1,591612	1,390476	-4,900568
1,409524	3,351283	1,409524	0,047492	1,409524	7,166431	1,409524	2,621568	1,409524	-173,629727	1,409524	1,596777	1,409524	5,794247
1,428571	3,351866	1,428571	0,049457	1,428571	7,166431	1,428571	2,500108	1,428571	-162,868146	1,428571	1,601184	1,428571	16,540096
1,447619	3,352304	1,447619	0,051198	1,447619	7,166431	1,447619	2,380962	1,447619	-152,059387	1,447619	1,604864	1,447619	27,336164
1,466667	3,352624	1,466667	0,052712	1,466667	7,166431	1,466667	2,264116	1,466667	-141,204193	1,466667	1,607844	1,466667	38,181627
1,485714	3,352849	1,485714	0,053998	1,485714	7,166431	1,485714	2,149554	1,485714	-130,303285	1,485714	1,610152	1,485714	49,075650
1,504762	3,353002	1,504762	0,055060	1,504762	7,166431	1,504762	2,037258	1,504762	-119,357366	1,504762	1,611815	1,504762	60,017399
1,523810	3,353102	1,523810	0,055902	1,523810	7,166431	1,523810	1,927211	1,523810	-108,367122	1,523810	1,612859	1,523810	71,006038
1,542857	3,353166	1,542857	0,056530	1,542857	7,166431	1,542857	1,819394	1,542857	-97,333221	1,542857	1,613309	1,542857	82,040734
1,561905	3,353210	1,561905	0,056952	1,561905	7,166431	1,561905	1,713786	1,561905	-86,256315	1,561905	1,613188	1,561905	93,120664
1,580952	3,353247	1,580952	0,057178	1,580952	7,166431	1,580952	1,610368	1,580952	-75,137039	1,580952	1,612520	1,580952	104,245014
1,600000	3,353288	1,600000	0,057217	1,600000	7,166431	1,600000	1,509117	1,600000	-63,976014	1,600000	1,611326	1,600000	115,412983
1,677778	3,353672	1,677778	0,055687	1,677778	7,166431	1,677778	1,117705	1,677778	-17,981034	1,677778	1,601411	1,677778	161,451934
1,755556	3,354657	1,755556	0,052063	1,755556	7,166431	1,755556	0,760468	1,755556	28,661471	1,755556	1,584292	1,755556	-151,845027
1,833333	3,356352	1,833333	0,047150	1,833333	7,166431	1,833333	0,435697	1,833333	75,916212	1,833333	1,560973	1,833333	-104,522810
1,911111	3,358685	1,911111	0,041633	1,911111	7,166431	1,911111	0,141608	1,911111	123,750992	1,911111	1,532281	1,911111	-56,620626
1,988889	3,361504	1,988889	0,036031	1,988889	7,166431	1,988889	0,123617	1,988889	-7,863659	1,988889	1,498924	1,988889	-8,172445
2,066667	3,364630	2,066667	0,030699	2,066667	7,166431	2,066667	0,361806	2,066667	41,045203	2,066667	1,461530	2,066667	40,792249
2,144444	3,367901	2,144444	0,025846	2,144444	7,166431	2,144444	0,574768	2,144444	90,452670	2,144444	1,420681	2,144444	90,247630
2,222222	3,371185	2,222222	0,021570	2,222222	7,166431	2,222222	0,764274	2,222222	140,335745	2,222222	1,376924	2,222222	140,170780
2,300000	3,374384	2,300000	0,017892	2,300000	7,166431	2,300000	0,932048	2,300000	-169,326851	2,300000	1,330785	2,300000	-169,458935
2,377778	3,377432	2,377778	0,014785	2,377778	7,166431	2,377778	1,079749	2,377778	-118,554857	2,377778	1,282763	2,377778	-118,660337
2,455556	3,380291	2,455556	0,012194	2,455556	7,166431	2,455556	1,208967	2,455556	-67,366622	2,455556	1,233332	2,455556	-67,450792
2,533333	3,382942	2,533333	0,010054	2,533333	7,166431	2,533333	1,321215	2,533333	-15,779241	2,533333	1,182935	2,533333	-15,846454
2,611111	3,385382	2,611111	0,008296	2,611111	7,166431	2,611111	1,417928	2,611111	36,191333	2,611111	1,131984	2,611111	36,137558
2,688889	3,387615	2,688889	0,006859	2,688889	7,166431	2,688889	1,500461	2,688889	88,530179	2,688889	1,080855	2,688889	88,487035
2,766667	3,389653	2,766667	0,005686	2,766667	7,166431	2,766667	1,570083	2,766667	141,223323	2,766667	1,029886	2,766667	141,188586
2,844444	3,391509	2,844444	0,004728	2,844444	7,166431	2,844444	1,627986	2,844444	-165,742350	2,844444	0,979378	2,844444	-165,770429
2,922222	3,393199	2,922222	0,003945	2,922222	7,166431	2,922222	1,675280	2,922222	-112,379163	2,922222	0,929597	2,922222	-112,401959
3,000000	3,394738	3,000000	0,003304	3,000000	7,166431	3,000000	1,712999	3,000000	-58,698715	3,000000	0,880771	3,000000	-58,717305"""

# Process data
lines = raw_data.strip().split('\n')
data = []
for line in lines:
    values = [float(v.replace(',', '.')) for v in line.split('\t')]
    data.append(values)

data = np.array(data)

# Extract columns
omega = data[:, 0]  # Encounter Frequency (rad/s)
added_mass = data[:, 1]  # Added mass a33 (t/m)
damping = data[:, 3]  # Damping b33 (t/(m·s))
stiffness = data[:, 5]  # Stiffness c33 (t/(m·s²))
froude_krylov_amp = data[:, 7]  # Froude-Krylov Amplitude (kN/m²)
froude_krylov_phase = data[:, 9]  # Froude-Krylov Phase (deg)
diffraction_amp = data[:, 11]  # Diffraction Amplitude (kN/m²)
diffraction_phase = data[:, 13]  # Diffraction Phase (deg)

# ============================================================================
# FIGURE 1: Added Mass and Damping - Classic Academic Format
# (Most commonly used format in literature)
# ============================================================================
fig1, (ax1a, ax1b) = plt.subplots(1, 2, figsize=(10, 4))

# Left panel: Added Mass
ax1a.plot(omega, added_mass, 'k-', linewidth=1.8, label=r'$a_{33}$')
ax1a.set_xlabel(r'$\omega$ (rad/s)')
ax1a.set_ylabel(r'$a_{33}$ (t/m)')
ax1a.set_xlim([0, 3.2])
ax1a.set_ylim([2.8, 3.5])
ax1a.xaxis.set_minor_locator(AutoMinorLocator(2))
ax1a.yaxis.set_minor_locator(AutoMinorLocator(2))
ax1a.text(0.05, 0.95, '(a)', transform=ax1a.transAxes, fontsize=12, 
          fontweight='bold', va='top')

# Right panel: Damping
ax1b.plot(omega, damping, 'k-', linewidth=1.8, label=r'$b_{33}$')
ax1b.set_xlabel(r'$\omega$ (rad/s)')
ax1b.set_ylabel(r'$b_{33}$ (t/(m$\cdot$s))')
ax1b.set_xlim([0, 3.2])
ax1b.set_ylim([0, 0.5])
ax1b.xaxis.set_minor_locator(AutoMinorLocator(2))
ax1b.yaxis.set_minor_locator(AutoMinorLocator(2))
ax1b.text(0.05, 0.95, '(b)', transform=ax1b.transAxes, fontsize=12, 
          fontweight='bold', va='top')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Fig1_AddedMass_Damping.png'), dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig(os.path.join(output_dir, 'Fig1_AddedMass_Damping.pdf'), format='pdf', bbox_inches='tight')
print("Figure 1 saved: output/head_seas/Fig1_AddedMass_Damping.png/pdf")

# ============================================================================
# FIGURE 2: Wave Excitation Forces - Amplitude & Phase (4 Panel)
# Standard presentation in academic papers
# ============================================================================
fig2, axes = plt.subplots(2, 2, figsize=(10, 8))

# Top left: Froude-Krylov Amplitude
ax2a = axes[0, 0]
ax2a.plot(omega, froude_krylov_amp, 'k-', linewidth=1.8)
ax2a.set_ylabel(r'$|F_{FK}|$ (kN/m$^2$)')
ax2a.set_xlim([0, 3.2])
ax2a.set_ylim([0, 14])
ax2a.xaxis.set_minor_locator(AutoMinorLocator(2))
ax2a.yaxis.set_minor_locator(AutoMinorLocator(2))
ax2a.text(0.05, 0.95, '(a) Froude-Krylov', transform=ax2a.transAxes, 
          fontsize=11, fontweight='bold', va='top')
ax2a.set_xticklabels([])

# Top right: Diffraction Amplitude
ax2b = axes[0, 1]
ax2b.plot(omega, diffraction_amp, 'k-', linewidth=1.8)
ax2b.set_ylabel(r'$|F_D|$ (kN/m$^2$)')
ax2b.set_xlim([0, 3.2])
ax2b.set_ylim([0, 8])
ax2b.xaxis.set_minor_locator(AutoMinorLocator(2))
ax2b.yaxis.set_minor_locator(AutoMinorLocator(2))
ax2b.text(0.05, 0.95, '(b) Diffraction', transform=ax2b.transAxes, 
          fontsize=11, fontweight='bold', va='top')
ax2b.set_xticklabels([])

# Bottom left: Froude-Krylov Phase
ax2c = axes[1, 0]
ax2c.plot(omega, froude_krylov_phase, 'k-', linewidth=1.8)
ax2c.set_xlabel(r'$\omega$ (rad/s)')
ax2c.set_ylabel(r'$\phi_{FK}$ (deg)')
ax2c.set_xlim([0, 3.2])
ax2c.set_ylim([-200, 200])
ax2c.set_yticks([-180, -90, 0, 90, 180])
ax2c.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
ax2c.xaxis.set_minor_locator(AutoMinorLocator(2))
ax2c.text(0.05, 0.95, '(c)', transform=ax2c.transAxes, fontsize=11, 
          fontweight='bold', va='top')

# Bottom right: Diffraction Phase
ax2d = axes[1, 1]
ax2d.plot(omega, diffraction_phase, 'k-', linewidth=1.8)
ax2d.set_xlabel(r'$\omega$ (rad/s)')
ax2d.set_ylabel(r'$\phi_D$ (deg)')
ax2d.set_xlim([0, 3.2])
ax2d.set_ylim([-200, 200])
ax2d.set_yticks([-180, -90, 0, 90, 180])
ax2d.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
ax2d.xaxis.set_minor_locator(AutoMinorLocator(2))
ax2d.text(0.05, 0.95, '(d)', transform=ax2d.transAxes, fontsize=11, 
          fontweight='bold', va='top')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Fig2_WaveExcitation.png'), dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.savefig(os.path.join(output_dir, 'Fig2_WaveExcitation.pdf'), format='pdf', bbox_inches='tight')
print("Figure 2 saved: output/head_seas/Fig2_WaveExcitation.png/pdf")

# ============================================================================
# FIGURE 3: Comparative Wave Excitation (Overlay)
# Froude-Krylov vs Diffraction - on same plot
# ============================================================================
fig3, (ax3a, ax3b) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

# Top panel: Amplitude comparison
ax3a.plot(omega, froude_krylov_amp, 'k-', linewidth=1.8, 
          label='Froude-Krylov')
ax3a.plot(omega, diffraction_amp, 'k--', linewidth=1.8, 
          label='Diffraction')
ax3a.set_ylabel(r'Wave Excitation Force (kN/m$^2$)')
ax3a.set_xlim([0, 3.2])
ax3a.set_ylim([0, 14])
ax3a.legend(loc='upper right', framealpha=0.95, edgecolor='black')
ax3a.xaxis.set_minor_locator(AutoMinorLocator(2))
ax3a.yaxis.set_minor_locator(AutoMinorLocator(2))
ax3a.text(0.02, 0.95, '(a) Amplitude', transform=ax3a.transAxes, 
          fontsize=11, fontweight='bold', va='top')

# Bottom panel: Phase comparison
ax3b.plot(omega, froude_krylov_phase, 'k-', linewidth=1.8, 
          label='Froude-Krylov')
ax3b.plot(omega, diffraction_phase, 'k--', linewidth=1.8, 
          label='Diffraction')
ax3b.set_xlabel(r'$\omega$ (rad/s)')
ax3b.set_ylabel(r'Phase (deg)')
ax3b.set_xlim([0, 3.2])
ax3b.set_ylim([-200, 200])
ax3b.set_yticks([-180, -90, 0, 90, 180])
ax3b.axhline(y=0, color='gray', linestyle=':', linewidth=0.8)
ax3b.legend(loc='upper right', framealpha=0.95, edgecolor='black')
ax3b.xaxis.set_minor_locator(AutoMinorLocator(2))
ax3b.text(0.02, 0.95, '(b) Phase', transform=ax3b.transAxes, 
          fontsize=11, fontweight='bold', va='top')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Fig3_WaveExcitation_Comparison.png'), dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.savefig(os.path.join(output_dir, 'Fig3_WaveExcitation_Comparison.pdf'), format='pdf', bbox_inches='tight')
print("Figure 3 saved: output/head_seas/Fig3_WaveExcitation_Comparison.png/pdf")

# ============================================================================
# FIGURE 4: All Hydrodynamic Coefficients - Single Figure (6 Panel)
# Comprehensive academic presentation format
# ============================================================================
fig4, axes = plt.subplots(3, 2, figsize=(10, 10))

# (a) Added Mass
ax4a = axes[0, 0]
ax4a.plot(omega, added_mass, 'k-', linewidth=1.8)
ax4a.set_ylabel(r'$a_{33}$ (t/m)')
ax4a.set_xlim([0, 3.2])
ax4a.xaxis.set_minor_locator(AutoMinorLocator(2))
ax4a.yaxis.set_minor_locator(AutoMinorLocator(2))
ax4a.text(0.05, 0.95, '(a) Added Mass', transform=ax4a.transAxes, 
          fontsize=10, fontweight='bold', va='top')
ax4a.set_xticklabels([])

# (b) Damping
ax4b = axes[0, 1]
ax4b.plot(omega, damping, 'k-', linewidth=1.8)
ax4b.set_ylabel(r'$b_{33}$ (t/(m$\cdot$s))')
ax4b.set_xlim([0, 3.2])
ax4b.xaxis.set_minor_locator(AutoMinorLocator(2))
ax4b.yaxis.set_minor_locator(AutoMinorLocator(2))
ax4b.text(0.05, 0.95, '(b) Damping', transform=ax4b.transAxes, 
          fontsize=10, fontweight='bold', va='top')
ax4b.set_xticklabels([])

# (c) Froude-Krylov Amplitude
ax4c = axes[1, 0]
ax4c.plot(omega, froude_krylov_amp, 'k-', linewidth=1.8)
ax4c.set_ylabel(r'$|F_{FK}|$ (kN/m$^2$)')
ax4c.set_xlim([0, 3.2])
ax4c.xaxis.set_minor_locator(AutoMinorLocator(2))
ax4c.yaxis.set_minor_locator(AutoMinorLocator(2))
ax4c.text(0.05, 0.95, '(c) Froude-Krylov Force', transform=ax4c.transAxes, 
          fontsize=10, fontweight='bold', va='top')
ax4c.set_xticklabels([])

# (d) Froude-Krylov Phase
ax4d = axes[1, 1]
ax4d.plot(omega, froude_krylov_phase, 'k-', linewidth=1.8)
ax4d.set_ylabel(r'$\phi_{FK}$ (deg)')
ax4d.set_xlim([0, 3.2])
ax4d.set_ylim([-200, 200])
ax4d.set_yticks([-180, -90, 0, 90, 180])
ax4d.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
ax4d.xaxis.set_minor_locator(AutoMinorLocator(2))
ax4d.text(0.05, 0.95, '(d) Froude-Krylov Phase', transform=ax4d.transAxes, 
          fontsize=10, fontweight='bold', va='top')
ax4d.set_xticklabels([])

# (e) Diffraction Amplitude
ax4e = axes[2, 0]
ax4e.plot(omega, diffraction_amp, 'k-', linewidth=1.8)
ax4e.set_xlabel(r'$\omega$ (rad/s)')
ax4e.set_ylabel(r'$|F_D|$ (kN/m$^2$)')
ax4e.set_xlim([0, 3.2])
ax4e.xaxis.set_minor_locator(AutoMinorLocator(2))
ax4e.yaxis.set_minor_locator(AutoMinorLocator(2))
ax4e.text(0.05, 0.95, '(e) Diffraction Force', transform=ax4e.transAxes, 
          fontsize=10, fontweight='bold', va='top')

# (f) Diffraction Phase
ax4f = axes[2, 1]
ax4f.plot(omega, diffraction_phase, 'k-', linewidth=1.8)
ax4f.set_xlabel(r'$\omega$ (rad/s)')
ax4f.set_ylabel(r'$\phi_D$ (deg)')
ax4f.set_xlim([0, 3.2])
ax4f.set_ylim([-200, 200])
ax4f.set_yticks([-180, -90, 0, 90, 180])
ax4f.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
ax4f.xaxis.set_minor_locator(AutoMinorLocator(2))
ax4f.text(0.05, 0.95, '(f) Diffraction Phase', transform=ax4f.transAxes, 
          fontsize=10, fontweight='bold', va='top')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Fig4_AllCoefficients.png'), dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.savefig(os.path.join(output_dir, 'Fig4_AllCoefficients.pdf'), format='pdf', bbox_inches='tight')
print("Figure 4 saved: output/head_seas/Fig4_AllCoefficients.png/pdf")

# ============================================================================
# FIGURE 5: Added Mass & Damping (Single Panel - Dual Axis)
# Compact format preferred by some journals
# ============================================================================
fig5, ax5 = plt.subplots(figsize=(8, 5))

# Added Mass (left axis)
color1 = 'black'
ln1 = ax5.plot(omega, added_mass, 'k-', linewidth=2, label=r'$a_{33}$')
ax5.set_xlabel(r'$\omega$ (rad/s)')
ax5.set_ylabel(r'Added Mass, $a_{33}$ (t/m)')
ax5.tick_params(axis='y')
ax5.set_xlim([0, 3.2])
ax5.set_ylim([2.8, 3.5])

# Damping (right axis)
ax5_twin = ax5.twinx()
ln2 = ax5_twin.plot(omega, damping, 'k--', linewidth=2, label=r'$b_{33}$')
ax5_twin.set_ylabel(r'Damping, $b_{33}$ (t/(m$\cdot$s))')
ax5_twin.tick_params(axis='y')
ax5_twin.set_ylim([0, 0.6])

# Combined legend
lns = ln1 + ln2
labs = [l.get_label() for l in lns]
ax5.legend(lns, labs, loc='upper right', framealpha=0.95, edgecolor='black')

ax5.xaxis.set_minor_locator(AutoMinorLocator(2))
ax5.yaxis.set_minor_locator(AutoMinorLocator(2))
ax5_twin.yaxis.set_minor_locator(AutoMinorLocator(2))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Fig5_AddedMass_Damping_Combined.png'), dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.savefig(os.path.join(output_dir, 'Fig5_AddedMass_Damping_Combined.pdf'), format='pdf', bbox_inches='tight')
print("Figure 5 saved: output/head_seas/Fig5_AddedMass_Damping_Combined.png/pdf")

# ============================================================================
# FIGURE 6: Wave Excitation Amplitudes Only - Comparison
# Academic presentation with markers (ideal for experimental/numerical comparison)
# ============================================================================
fig6, ax6 = plt.subplots(figsize=(8, 5))

# Show marker every 5th point (cleaner appearance)
markevery = 4

ax6.plot(omega, froude_krylov_amp, 'k-', linewidth=1.8, 
         marker='o', markersize=5, markevery=markevery, markerfacecolor='white',
         markeredgewidth=1.2, label='Froude-Krylov')
ax6.plot(omega, diffraction_amp, 'k--', linewidth=1.8,
         marker='s', markersize=5, markevery=markevery, markerfacecolor='white',
         markeredgewidth=1.2, label='Diffraction')

ax6.set_xlabel(r'$\omega$ (rad/s)')
ax6.set_ylabel(r'Wave Excitation Force per Unit Wave Amplitude (kN/m$^2$)')
ax6.set_xlim([0, 3.2])
ax6.set_ylim([0, 14])
ax6.legend(loc='upper right', framealpha=0.95, edgecolor='black')
ax6.xaxis.set_minor_locator(AutoMinorLocator(2))
ax6.yaxis.set_minor_locator(AutoMinorLocator(2))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Fig6_WaveExcitation_Markers.png'), dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.savefig(os.path.join(output_dir, 'Fig6_WaveExcitation_Markers.pdf'), format='pdf', bbox_inches='tight')
print("Figure 6 saved: output/head_seas/Fig6_WaveExcitation_Markers.png/pdf")

plt.show()

print("\n" + "="*70)
print("ACADEMIC FIGURES GENERATED SUCCESSFULLY!")
print("="*70)
print("""
Generated Figures:
------------------
Fig1: Added Mass and Damping (side-by-side panels)
Fig2: Wave Excitation Forces - 4 panel (FK amp, D amp, FK phase, D phase)
Fig3: Froude-Krylov vs Diffraction comparison (overlay)
Fig4: All coefficients - 6 panel comprehensive view
Fig5: Added Mass & Damping - dual-axis compact format
Fig6: Wave Excitation Amplitudes - comparison with markers

Format:
-------
- PNG: High resolution (300 DPI) - for presentations
- PDF: Vector format - ideal for academic publications

Academic Standards:
-------------------
- Serif font family (Times New Roman style)
- Grayscale compatible (for B&W printing)
- Mathematical notation (LaTeX style)
- Minor grid lines
- Panel labels (a), (b), (c)...
""")
print("="*70)

