# -*- coding: utf-8 -*-
"""
RAO Comparison Plots - Maxsurf Motion CG RAOs
90° vs 180° Wave Heading Comparison
Academic Standard Visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# Akademik Standart Grafik Ayarları
# ============================================================================
rcParams['figure.figsize'] = (10, 7)
rcParams['axes.labelsize'] = 14
rcParams['axes.titlesize'] = 16
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['legend.fontsize'] = 12
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif', 'STIX']
rcParams['mathtext.fontset'] = 'stix'
rcParams['axes.grid'] = True
rcParams['grid.alpha'] = 0.3
rcParams['grid.linestyle'] = '--'
rcParams['savefig.dpi'] = 300
rcParams['savefig.bbox'] = 'tight'
rcParams['axes.linewidth'] = 1.2
rcParams['lines.linewidth'] = 1.8

# ============================================================================
# Akademik Standart Renk Paleti (ColorBrewer + Nature/Science standartları)
# Renk körlüğü dostu ve basılı yayınlarda da net görünen renkler
# ============================================================================
COLOR_90 = '#0072B2'    # Koyu mavi (90 derece için)
COLOR_180 = '#D55E00'   # Koyu turuncu-kırmızı (180 derece için)
LINESTYLE_90 = '-'      # Solid line
LINESTYLE_180 = '--'    # Dashed line
MARKER_90 = 'o'         # Circle marker
MARKER_180 = 's'        # Square marker
MARKERSIZE = 4
MARKEVERY = 5

# ============================================================================
# Veri Tanımlamaları
# ============================================================================

# 90 Derece Dalga Açısı Verileri
data_90_raw = """0,240000	0,997714	0,240000	0,229022	0,240000	189,693385
0,257778	1,001060	0,257778	0,262857	0,257778	213,669824
0,275556	1,005062	0,275556	0,295099	0,275556	237,060904
0,293333	1,009688	0,293333	0,325430	0,293333	258,969566
0,311111	1,014917	0,311111	0,353477	0,311111	278,347829
0,328889	1,020756	0,328889	0,378822	0,328889	294,025284
0,346667	1,027257	0,346667	0,401009	0,346667	304,769243
0,364444	1,034538	0,364444	0,419567	0,364444	309,382356
0,382222	1,042804	0,382222	0,434028	0,382222	306,840025
0,400000	1,052375	0,400000	0,443946	0,400000	296,475959
0,419048	1,064563	0,419048	0,449066	0,419048	276,632175
0,438095	1,079512	0,438095	0,448222	0,438095	249,039536
0,457143	1,098623	0,457143	0,441873	0,457143	218,448303
0,476190	1,122514	0,476190	0,429114	0,476190	200,365232
0,495238	1,152209	0,495238	0,409879	0,495238	222,562144
0,514286	1,188659	0,514286	0,384271	0,514286	275,176947
0,533333	1,232571	0,533333	0,352606	0,533333	335,415157
0,552381	1,284182	0,552381	0,315464	0,552381	394,187849
0,571429	1,342963	0,571429	0,273783	0,571429	447,551180
0,590476	1,407227	0,590476	0,229019	0,590476	493,163373
0,609524	1,473628	0,609524	0,183495	0,609524	528,957382
0,628571	1,536588	0,628571	0,141167	0,628571	552,350775
0,647619	1,587866	0,647619	0,109044	0,647619	560,137943
0,666667	1,616814	0,666667	0,096493	0,666667	549,514346
0,685714	1,612112	0,685714	0,104306	0,685714	520,232129
0,704762	1,565331	0,704762	0,120038	0,704762	476,781384
0,723810	1,475007	0,723810	0,132257	0,723810	428,305184
0,742857	1,348356	0,742857	0,135677	0,742857	384,743927
0,761905	1,198924	0,761905	0,129235	0,761905	352,338882
0,780952	1,041825	0,780952	0,114289	0,780952	334,355617
0,800000	0,889673	0,800000	0,093367	0,800000	332,484442
0,819048	0,750749	0,819048	0,069330	0,819048	340,387175
0,838095	0,629004	0,838095	0,044883	0,838095	343,716250
0,857143	0,524996	0,857143	0,022390	0,857143	331,051402
0,876190	0,437167	0,876190	0,005675	0,876190	301,219497
0,895238	0,363178	0,895238	0,013533	0,895238	266,498801
0,914286	0,301045	0,914286	0,023078	0,914286	255,507414
0,933333	0,249820	0,933333	0,028050	0,933333	273,264833
0,952381	0,209603	0,952381	0,028686	0,952381	287,681955
0,971429	0,180511	0,971429	0,025808	0,971429	287,060346
0,990476	0,161364	0,990476	0,020506	0,990476	275,086023
1,009524	0,148849	1,009524	0,014083	1,009524	260,871263
1,028571	0,138413	1,028571	0,008326	1,028571	252,504089
1,047619	0,126128	1,047619	0,006591	1,047619	252,958210
1,066667	0,109823	1,066667	0,009185	1,066667	259,611564
1,085714	0,089218	1,085714	0,011799	1,085714	266,449538
1,104762	0,065545	1,104762	0,012945	1,104762	267,931648
1,123810	0,041076	1,123810	0,012505	1,123810	262,539150
1,142857	0,019012	1,142857	0,010840	1,142857	253,440990
1,161905	0,009427	1,161905	0,008580	1,161905	246,144282
1,180952	0,018837	1,180952	0,006548	1,180952	245,162432
1,200000	0,025471	1,200000	0,005567	1,200000	250,827723
1,219048	0,026314	1,219048	0,005722	1,219048	259,021461
1,238095	0,022240	1,238095	0,006236	1,238095	265,543228
1,257143	0,015649	1,257143	0,006520	1,257143	268,686517
1,276190	0,012183	1,276190	0,006410	1,276190	269,509309
1,295238	0,017558	1,295238	0,005945	1,295238	270,276811
1,314286	0,026351	1,314286	0,005232	1,314286	272,596347
1,333333	0,034304	1,333333	0,004449	1,333333	276,900880
1,352381	0,039823	1,352381	0,003896	1,352381	282,748063
1,371429	0,042203	1,371429	0,003850	1,371429	289,058004
1,390476	0,041366	1,390476	0,004197	1,390476	294,952722
1,409524	0,037888	1,409524	0,004521	1,409524	300,223611
1,428571	0,032883	1,428571	0,004541	1,428571	304,221098
1,447619	0,027543	1,447619	0,004260	1,447619	305,844874
1,466667	0,022460	1,466667	0,003929	1,466667	305,669813
1,485714	0,017498	1,485714	0,003839	1,485714	306,174040
1,504762	0,013091	1,504762	0,003998	1,504762	309,156701
1,523810	0,012580	1,523810	0,004139	1,523810	314,339803
1,542857	0,018029	1,542857	0,004056	1,542857	320,075684
1,561905	0,025515	1,561905	0,003746	1,561905	324,911869
1,580952	0,031894	1,580952	0,003347	1,580952	328,720855
1,600000	0,035629	1,600000	0,003014	1,600000	332,209575
1,677778	0,024349	1,677778	0,002650	1,677778	341,544110
1,755556	0,017524	1,755556	0,002441	1,755556	348,463988
1,833333	0,023117	1,833333	0,001803	1,833333	350,936827
1,911111	0,019918	1,911111	0,001446	1,911111	346,747834
1,988889	0,015447	1,988889	0,001483	1,988889	348,792330
2,066667	0,015750	2,066667	0,001263	2,066667	342,618661
2,144444	0,015161	2,144444	0,001198	2,144444	339,366441
2,222222	0,016041	2,222222	0,001163	2,222222	337,208653
2,300000	0,018015	2,300000	0,000978	2,300000	324,002878
2,377778	0,019151	2,377778	0,000948	2,377778	318,457726
2,455556	0,019761	2,455556	0,000776	2,455556	295,725526
2,533333	0,019016	2,533333	0,000868	2,533333	293,620208
2,611111	0,019767	2,611111	0,000717	2,611111	268,919328
2,688889	0,029158	2,688889	0,000518	2,688889	254,037228
2,766667	0,027269	2,766667	0,001001	2,766667	274,083819
2,844444	0,016539	2,844444	0,001447	2,844444	315,466088
2,922222	0,016312	2,922222	0,000764	2,922222	223,320155
3,000000	0,021122	3,000000	0,000439	3,000000	186,355929"""

# 180 Derece Dalga Açısı Verileri
data_180_raw = """0,360002	0,919803	0,360002	1,022664	0,360002	240,174207
0,364446	0,915559	0,364446	1,022286	0,364446	242,074148
0,368891	0,911167	0,368891	1,021823	0,368891	243,829176
0,373335	0,906625	0,373335	1,021272	0,373335	245,437261
0,377779	0,901929	0,377779	1,020632	0,377779	246,896803
0,382223	0,897077	0,382223	1,019899	0,382223	248,206663
0,386668	0,892068	0,386668	1,019071	0,386668	249,366228
0,391112	0,886900	0,391112	1,018144	0,391112	250,375566
0,395556	0,881569	0,395556	1,017116	0,395556	251,234934
0,400001	0,876072	0,400001	1,015984	0,400001	251,945376
0,419048	0,850576	0,419048	1,009884	0,419048	253,356590
0,438095	0,821763	0,438095	1,001642	0,438095	252,344845
0,457143	0,789292	0,457143	0,991311	0,457143	249,358745
0,476191	0,753103	0,476191	0,978264	0,476191	245,418653
0,495238	0,712975	0,495238	0,962195	0,495238	241,769115
0,514286	0,668708	0,514286	0,942759	0,514286	239,875509
0,533333	0,620125	0,533333	0,919564	0,533333	241,099846
0,552381	0,567102	0,552381	0,892175	0,552381	246,202623
0,571429	0,509635	0,571429	0,860109	0,571429	254,920362
0,590476	0,447970	0,590476	0,822860	0,590476	265,922846
0,609524	0,382857	0,609524	0,779944	0,609524	277,148333
0,628571	0,316046	0,628571	0,730981	0,628571	286,246172
0,647619	0,251307	0,647619	0,675831	0,647619	290,938295
0,666667	0,196343	0,666667	0,614775	0,666667	289,307940
0,685714	0,164368	0,685714	0,548693	0,685714	280,091827
0,704762	0,165763	0,704762	0,479138	0,704762	262,983625
0,723810	0,191534	0,723810	0,408195	0,723810	238,831801
0,742857	0,223957	0,742857	0,338166	0,742857	209,575249
0,761905	0,252328	0,761905	0,271209	0,761905	177,935754
0,780952	0,272616	0,780952	0,209103	0,780952	147,254906
0,800000	0,284110	0,800000	0,153134	0,800000	123,037664
0,819048	0,287488	0,819048	0,104073	0,819048	119,079635
0,838095	0,283919	0,838095	0,062201	0,838095	132,889590
0,857143	0,274682	0,857143	0,027392	0,857143	146,984723
0,876190	0,261004	0,876190	0,000905	0,876190	157,041412
0,895238	0,244001	0,895238	0,022945	0,895238	162,658278
0,914286	0,224648	0,914286	0,039785	0,914286	164,404362
0,933333	0,203778	0,933333	0,052042	0,933333	163,247248
0,952381	0,182079	0,952381	0,060391	0,952381	160,320228
0,971429	0,160143	0,971429	0,065494	0,971429	156,816313
0,990476	0,138442	0,990476	0,067952	0,990476	153,775163
1,009524	0,117349	1,009524	0,068281	1,009524	151,845523
1,028571	0,097157	1,028571	0,066926	1,028571	151,135051
1,047619	0,078094	1,047619	0,064269	1,047619	151,253259
1,066667	0,060333	1,066667	0,060635	1,066667	151,553569
1,085714	0,044005	1,085714	0,056297	1,085714	151,401232
1,104762	0,029215	1,104762	0,051483	1,104762	150,333254
1,123810	0,016112	1,123810	0,046385	1,123810	148,106545
1,142857	0,005636	1,142857	0,041157	1,142857	144,683864
1,161905	0,007767	1,161905	0,035930	1,161905	140,196872
1,180952	0,015854	1,180952	0,030806	1,180952	134,905596
1,200000	0,022970	1,200000	0,025871	1,200000	129,163048
1,219048	0,028788	1,219048	0,021194	1,219048	123,391596
1,238095	0,033319	1,238095	0,016831	1,238095	118,080692
1,257143	0,036628	1,257143	0,012837	1,257143	113,813835
1,276190	0,038797	1,276190	0,009277	1,276190	111,259127
1,295238	0,039922	1,295238	0,006274	1,295238	110,806215
1,314286	0,040103	1,314286	0,004156	1,314286	111,950529
1,333333	0,039443	1,333333	0,003605	1,333333	113,720720
1,352381	0,038049	1,352381	0,004538	1,352381	115,506118
1,371429	0,036032	1,371429	0,005920	1,371429	117,134028
1,390476	0,033502	1,390476	0,007236	1,390476	118,671191
1,409524	0,030573	1,409524	0,008332	1,409524	120,259384
1,428571	0,027361	1,428571	0,009171	1,428571	121,999027
1,447619	0,023993	1,447619	0,009747	1,447619	123,885904
1,466667	0,020605	1,466667	0,010072	1,466667	125,811535
1,485714	0,017364	1,485714	0,010164	1,485714	127,608713
1,504762	0,014482	1,504762	0,010046	1,504762	129,106373
1,523810	0,012240	1,523810	0,009744	1,523810	130,170658
1,542857	0,010953	1,542857	0,009286	1,542857	130,727731
1,561905	0,010793	1,561905	0,008700	1,561905	130,772169
1,580952	0,011587	1,580952	0,008018	1,580952	130,365375
1,600000	0,012934	1,600000	0,007273	1,600000	129,626843
1,677778	0,018276	1,677778	0,004360	1,677778	126,764830
1,755556	0,018899	1,755556	0,003623	1,755556	129,133184
1,833333	0,015483	1,833333	0,004379	1,833333	135,221475
1,911111	0,012271	1,911111	0,004404	1,911111	141,218347
1,988889	0,012616	1,988889	0,003634	1,988889	143,376128
2,066667	0,013798	2,066667	0,002900	2,066667	144,619720
2,144444	0,013299	2,144444	0,002735	2,144444	148,284158
2,222222	0,011842	2,222222	0,002698	2,222222	153,546344
2,300000	0,010998	2,300000	0,002430	2,300000	157,153763
2,377778	0,010715	2,377778	0,002093	2,377778	159,281921
2,455556	0,010144	2,455556	0,001891	2,455556	162,370380
2,533333	0,009383	2,533333	0,001740	2,533333	166,574675
2,611111	0,008855	2,611111	0,001537	2,611111	169,816780
2,688889	0,008325	2,688889	0,001349	2,688889	171,942078
2,766667	0,007518	2,766667	0,001228	2,766667	174,615657
2,844444	0,006786	2,844444	0,001106	2,844444	178,209762
2,922222	0,006418	2,922222	0,000944	2,922222	181,030237
3,000000	0,006021	3,000000	0,000805	3,000000	182,693805"""


def parse_data(raw_data):
    """
    Türkçe ondalık formatındaki (virgüllü) veriyi parse eder.
    Sütunlar: Heave_X, Heave_Y, Pitch_X, Pitch_Y, AddedRes_X, AddedRes_Y
    """
    lines = raw_data.strip().split('\n')
    heave_x, heave_y = [], []
    pitch_x, pitch_y = [], []
    added_res_x, added_res_y = [], []
    
    for line in lines:
        # Tab ile ayrılmış sütunları al
        parts = line.split('\t')
        if len(parts) >= 6:
            # Türkçe ondalık formatını (virgül) noktaya çevir
            heave_x.append(float(parts[0].replace(',', '.')))
            heave_y.append(float(parts[1].replace(',', '.')))
            pitch_x.append(float(parts[2].replace(',', '.')))
            pitch_y.append(float(parts[3].replace(',', '.')))
            added_res_x.append(float(parts[4].replace(',', '.')))
            added_res_y.append(float(parts[5].replace(',', '.')))
    
    return {
        'heave_x': np.array(heave_x),
        'heave_y': np.array(heave_y),
        'pitch_x': np.array(pitch_x),
        'pitch_y': np.array(pitch_y),
        'added_res_x': np.array(added_res_x),
        'added_res_y': np.array(added_res_y)
    }


# ============================================================================
# Veri İşleme
# ============================================================================
data_90 = parse_data(data_90_raw)
data_180 = parse_data(data_180_raw)

# ============================================================================
# Grafik 1: Heave RAO Karşılaştırması
# ============================================================================
fig1, ax1 = plt.subplots(figsize=(10, 7))

ax1.plot(data_90['heave_x'], data_90['heave_y'], 
         color=COLOR_90, linestyle=LINESTYLE_90, linewidth=2, 
         marker=MARKER_90, markersize=MARKERSIZE, markevery=MARKEVERY,
         label=r'Beam Sea ($\beta = 90°$)')
ax1.plot(data_180['heave_x'], data_180['heave_y'], 
         color=COLOR_180, linestyle=LINESTYLE_180, linewidth=2, 
         marker=MARKER_180, markersize=MARKERSIZE, markevery=MARKEVERY,
         label=r'Head Sea ($\beta = 180°$)')

ax1.set_xlabel(r'Wave Frequency, $\omega$ (rad/s)', fontsize=14, fontweight='bold')
ax1.set_ylabel(r'Heave RAO, $\eta_3/\zeta_a$ (m/m)', fontsize=14, fontweight='bold')
ax1.set_title('Heave Response Amplitude Operator (RAO)\nComparison at Different Wave Headings', 
              fontsize=14, fontweight='bold', pad=15)
ax1.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
ax1.set_xlim([0, 1.5])
ax1.set_ylim([0, max(max(data_90['heave_y']), max(data_180['heave_y'])) * 1.1])
ax1.grid(True, linestyle='--', alpha=0.6)

# Minor grid ekleme
ax1.minorticks_on()
ax1.grid(which='minor', linestyle=':', alpha=0.3)

plt.tight_layout()
fig1.savefig('Heave_RAO_Comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
fig1.savefig('Heave_RAO_Comparison.pdf', dpi=300, bbox_inches='tight', facecolor='white')
print("Heave RAO grafiği kaydedildi: Heave_RAO_Comparison.png/pdf")

# ============================================================================
# Grafik 2: Pitch RAO Karşılaştırması
# ============================================================================
fig2, ax2 = plt.subplots(figsize=(10, 7))

ax2.plot(data_90['pitch_x'], data_90['pitch_y'], 
         color=COLOR_90, linestyle=LINESTYLE_90, linewidth=2, 
         marker=MARKER_90, markersize=MARKERSIZE, markevery=MARKEVERY,
         label=r'Beam Sea ($\beta = 90°$)')
ax2.plot(data_180['pitch_x'], data_180['pitch_y'], 
         color=COLOR_180, linestyle=LINESTYLE_180, linewidth=2, 
         marker=MARKER_180, markersize=MARKERSIZE, markevery=MARKEVERY,
         label=r'Head Sea ($\beta = 180°$)')

ax2.set_xlabel(r'Wave Frequency, $\omega$ (rad/s)', fontsize=14, fontweight='bold')
ax2.set_ylabel(r'Pitch RAO, $\eta_5/k\zeta_a$ (rad/rad)', fontsize=14, fontweight='bold')
ax2.set_title('Pitch Response Amplitude Operator (RAO)\nComparison at Different Wave Headings', 
              fontsize=14, fontweight='bold', pad=15)
ax2.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
ax2.set_xlim([0, 2.0])
ax2.set_ylim([0, max(max(data_90['pitch_y']), max(data_180['pitch_y'])) * 1.1])
ax2.grid(True, linestyle='--', alpha=0.6)

ax2.minorticks_on()
ax2.grid(which='minor', linestyle=':', alpha=0.3)

plt.tight_layout()
fig2.savefig('Pitch_RAO_Comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
fig2.savefig('Pitch_RAO_Comparison.pdf', dpi=300, bbox_inches='tight', facecolor='white')
print("Pitch RAO grafiği kaydedildi: Pitch_RAO_Comparison.png/pdf")

# ============================================================================
# Grafik 3: Added Resistance Karşılaştırması
# ============================================================================
fig3, ax3 = plt.subplots(figsize=(10, 7))

ax3.plot(data_90['added_res_x'], data_90['added_res_y'], 
         color=COLOR_90, linestyle=LINESTYLE_90, linewidth=2, 
         marker=MARKER_90, markersize=MARKERSIZE, markevery=MARKEVERY,
         label=r'Beam Sea ($\beta = 90°$)')
ax3.plot(data_180['added_res_x'], data_180['added_res_y'], 
         color=COLOR_180, linestyle=LINESTYLE_180, linewidth=2, 
         marker=MARKER_180, markersize=MARKERSIZE, markevery=MARKEVERY,
         label=r'Head Sea ($\beta = 180°$)')

ax3.set_xlabel(r'Wave Frequency, $\omega$ (rad/s)', fontsize=14, fontweight='bold')
ax3.set_ylabel(r'Added Resistance, $R_{AW}$ (kN/m²)', fontsize=14, fontweight='bold')
ax3.set_title('Added Resistance in Waves\nComparison at Different Wave Headings', 
              fontsize=14, fontweight='bold', pad=15)
ax3.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
ax3.set_xlim([0, 2.0])
ax3.set_ylim([0, max(max(data_90['added_res_y']), max(data_180['added_res_y'])) * 1.1])
ax3.grid(True, linestyle='--', alpha=0.6)

ax3.minorticks_on()
ax3.grid(which='minor', linestyle=':', alpha=0.3)

plt.tight_layout()
fig3.savefig('Added_Resistance_Comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
fig3.savefig('Added_Resistance_Comparison.pdf', dpi=300, bbox_inches='tight', facecolor='white')
print("Added Resistance grafiği kaydedildi: Added_Resistance_Comparison.png/pdf")

# ============================================================================
# Grafik 4: Tüm RAO'lar Tek Figürde (3 subplot)
# ============================================================================
fig4, axes = plt.subplots(3, 1, figsize=(10, 14))

# Heave RAO
axes[0].plot(data_90['heave_x'], data_90['heave_y'], 
             color=COLOR_90, linestyle=LINESTYLE_90, linewidth=2, 
             marker=MARKER_90, markersize=MARKERSIZE, markevery=MARKEVERY,
             label=r'Beam Sea ($\beta = 90°$)')
axes[0].plot(data_180['heave_x'], data_180['heave_y'], 
             color=COLOR_180, linestyle=LINESTYLE_180, linewidth=2, 
             marker=MARKER_180, markersize=MARKERSIZE, markevery=MARKEVERY,
             label=r'Head Sea ($\beta = 180°$)')
axes[0].set_xlabel(r'Wave Frequency, $\omega$ (rad/s)', fontsize=12)
axes[0].set_ylabel(r'Heave RAO (m/m)', fontsize=12)
axes[0].set_title('(a) Heave RAO', fontsize=13, fontweight='bold')
axes[0].legend(loc='upper right', frameon=True)
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].set_xlim([0, 2.0])
axes[0].minorticks_on()
axes[0].grid(which='minor', linestyle=':', alpha=0.3)

# Pitch RAO
axes[1].plot(data_90['pitch_x'], data_90['pitch_y'], 
             color=COLOR_90, linestyle=LINESTYLE_90, linewidth=2, 
             marker=MARKER_90, markersize=MARKERSIZE, markevery=MARKEVERY,
             label=r'Beam Sea ($\beta = 90°$)')
axes[1].plot(data_180['pitch_x'], data_180['pitch_y'], 
             color=COLOR_180, linestyle=LINESTYLE_180, linewidth=2, 
             marker=MARKER_180, markersize=MARKERSIZE, markevery=MARKEVERY,
             label=r'Head Sea ($\beta = 180°$)')
axes[1].set_xlabel(r'Wave Frequency, $\omega$ (rad/s)', fontsize=12)
axes[1].set_ylabel(r'Pitch RAO (rad/rad)', fontsize=12)
axes[1].set_title('(b) Pitch RAO', fontsize=13, fontweight='bold')
axes[1].legend(loc='upper right', frameon=True)
axes[1].grid(True, linestyle='--', alpha=0.6)
axes[1].set_xlim([0, 2.0])
axes[1].minorticks_on()
axes[1].grid(which='minor', linestyle=':', alpha=0.3)

# Added Resistance
axes[2].plot(data_90['added_res_x'], data_90['added_res_y'], 
             color=COLOR_90, linestyle=LINESTYLE_90, linewidth=2, 
             marker=MARKER_90, markersize=MARKERSIZE, markevery=MARKEVERY,
             label=r'Beam Sea ($\beta = 90°$)')
axes[2].plot(data_180['added_res_x'], data_180['added_res_y'], 
             color=COLOR_180, linestyle=LINESTYLE_180, linewidth=2, 
             marker=MARKER_180, markersize=MARKERSIZE, markevery=MARKEVERY,
             label=r'Head Sea ($\beta = 180°$)')
axes[2].set_xlabel(r'Wave Frequency, $\omega$ (rad/s)', fontsize=12)
axes[2].set_ylabel(r'Added Resistance (kN/m²)', fontsize=12)
axes[2].set_title('(c) Added Resistance in Waves', fontsize=13, fontweight='bold')
axes[2].legend(loc='upper right', frameon=True)
axes[2].grid(True, linestyle='--', alpha=0.6)
axes[2].set_xlim([0, 2.0])
axes[2].minorticks_on()
axes[2].grid(which='minor', linestyle=':', alpha=0.3)

plt.tight_layout()
fig4.savefig('All_RAO_Comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
fig4.savefig('All_RAO_Comparison.pdf', dpi=300, bbox_inches='tight', facecolor='white')
print("Tüm RAO grafikleri kaydedildi: All_RAO_Comparison.png/pdf")

# ============================================================================
# Grafikleri Göster
# ============================================================================
plt.show()

print("\n" + "="*60)
print("Tüm grafikler başarıyla oluşturuldu ve kaydedildi!")
print("="*60)
print("\nKaydedilen dosyalar:")
print("  - Heave_RAO_Comparison.png/pdf")
print("  - Pitch_RAO_Comparison.png/pdf")
print("  - Added_Resistance_Comparison.png/pdf")
print("  - All_RAO_Comparison.png/pdf")
print("\nAkademik Özellikler:")
print("  - Times New Roman / STIX fontları")
print("  - 300 DPI çözünürlük")
print("  - LaTeX formatında etiketler")
print("  - Profesyonel grid ve legend")

