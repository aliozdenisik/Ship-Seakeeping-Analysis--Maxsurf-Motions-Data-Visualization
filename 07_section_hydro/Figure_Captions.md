# Figure Captions for Academic Publication

## Data Validation Summary

| Parameter | Range | Unit | Academic Validity |
|-----------|-------|------|-------------------|
| Added Mass (a₃₃) | 2.90 - 3.39 | t/m | ✅ Typical 2D section values |
| Damping (b₃₃) | 0.00 - 0.48 | t/(m·s) | ✅ Expected frequency behavior |
| Stiffness (c₃₃) | 7.17 (constant) | t/(m·s²) | ✅ Hydrostatic restoring (frequency independent) |
| Froude-Krylov | 0.07 - 12.95 | kN/m² | ✅ High at low ω, typical behavior |
| Diffraction | 0.92 - 7.14 | kN/m² | ✅ Dominant at high ω, as expected |
| Frequency Range | 0.24 - 3.00 | rad/s | ✅ Standard seakeeping analysis range |

---

## Figure Captions

### **Figure 1: Added Mass and Damping Coefficients**

> **Figure 1.** Two-dimensional section hydrodynamic coefficients for heave motion as functions of encounter frequency: (a) sectional added mass coefficient a₃₃, and (b) sectional damping coefficient b₃₃. The added mass exhibits a characteristic minimum at ω ≈ 0.57 rad/s before increasing monotonically at higher frequencies. The damping coefficient shows typical behavior with a peak at low frequencies (ω ≈ 0.38 rad/s) and asymptotic decay toward zero at high frequencies. Results obtained using strip theory methodology (Maxsurf Motion).

---

### **Figure 2: Wave Excitation Forces - Four Panel View**

> **Figure 2.** Sectional wave excitation force components for heave motion: (a) Froude-Krylov force amplitude |F_FK|, (b) diffraction force amplitude |F_D|, (c) Froude-Krylov force phase φ_FK, and (d) diffraction force phase φ_D. The Froude-Krylov component, representing the pressure integration over the undisturbed wave field, dominates at low frequencies and decays with increasing frequency. The diffraction component, accounting for wave scattering effects, shows relatively stable amplitude across the frequency range. Phase angles exhibit characteristic wrap-around behavior at ±180°.

---

### **Figure 3: Comparative Wave Excitation Analysis**

> **Figure 3.** Comparison of sectional wave excitation force components: (a) amplitude comparison showing the dominance of Froude-Krylov forces at low frequencies (ω < 1.0 rad/s) and the convergence of both components at higher frequencies, and (b) phase angle comparison illustrating the distinct phase characteristics of each component. Solid line: Froude-Krylov component; dashed line: diffraction component. The crossover region near ω ≈ 1.1 rad/s indicates the transition from Froude-Krylov dominated to diffraction-influenced response.

---

### **Figure 4: Complete Hydrodynamic Coefficient Summary**

> **Figure 4.** Comprehensive presentation of two-dimensional section hydrodynamic coefficients for heave motion: (a) added mass coefficient a₃₃, (b) damping coefficient b₃₃, (c) Froude-Krylov wave excitation force amplitude, (d) Froude-Krylov phase, (e) diffraction wave excitation force amplitude, and (f) diffraction phase. All quantities are presented as functions of encounter frequency ω (rad/s). These coefficients form the basis for strip theory seakeeping analysis following the methodology of Salvesen, Tuck, and Faltinsen (1970).

---

### **Figure 5: Combined Added Mass and Damping Plot**

> **Figure 5.** Sectional added mass (a₃₃, solid line, left axis) and damping (b₃₃, dashed line, right axis) coefficients for heave motion plotted on dual vertical axes. This compact representation facilitates direct comparison of the frequency-dependent behavior of both coefficients. The added mass shows a characteristic "U-shaped" profile with minimum near ω = 0.57 rad/s, while damping peaks at lower frequency (ω ≈ 0.38 rad/s) before monotonically decreasing.

---

### **Figure 6: Wave Excitation Force Comparison with Markers**

> **Figure 6.** Sectional wave excitation force amplitudes per unit wave amplitude for heave motion. Circle markers: Froude-Krylov component; square markers: diffraction component. The Froude-Krylov force, which represents the undisturbed incident wave pressure integrated over the body surface, decreases from approximately 13 kN/m² at low frequencies to less than 1 kN/m² at high frequencies. The diffraction force, arising from wave scattering by the body, increases monotonically from 1 kN/m² to approximately 7 kN/m² over the frequency range studied.

---

## Usage Notes

### Recommended Format for Publications

```
Figure X. [Short title]. [Detailed caption with physical description]
```

### LaTeX Example

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{Fig1_AddedMass_Damping.pdf}
    \caption{Two-dimensional section hydrodynamic coefficients for heave motion...}
    \label{fig:hydro_coefficients}
\end{figure}
```

### Reference Format

```
Salvesen, N., Tuck, E.O., & Faltinsen, O. (1970). Ship motions and sea loads. 
Transactions SNAME, 78, 250-287.
```

---

## Academic Validation Checklist

- [x] Added mass minimum value (~0.57 rad/s) - Consistent with strip theory
- [x] Damping approaching zero at high frequency - Physically correct
- [x] Stiffness constant - Hydrostatic restoring is frequency independent
- [x] Froude-Krylov dominant at low frequency - Consistent with long wave theory
- [x] Diffraction increasing at high frequency - Expected short wave scattering behavior
- [x] Phase wrap-around behavior (±180°) - Mathematically correct
- [x] Units consistent (t/m, t/(m·s), kN/m², rad/s, deg)
- [x] Frequency range (0.24-3.0 rad/s) - Typical seakeeping analysis range

---

*Generated from Maxsurf Motion Section Hydrodynamic Coefficients Analysis*
