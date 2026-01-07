# Ship Seakeeping Analysis: Maxsurf Motions Data Visualization

A Python-based visualization toolkit for analyzing ship seakeeping performance using Maxsurf Motions output data. This project generates publication-quality figures for Response Amplitude Operators (RAOs), motion spectra, hydrodynamic coefficients, and Motion Sickness Incidence (MSI) assessments.

## Author

**Ali Özden Işık**  
Istanbul Technical University (İTÜ)  
Department of Naval Architecture and Marine Engineering

## Course Information

| | |
|---|---|
| **Course Code** | DEN 411 |
| **Course Name** | Hydrodynamics of Ships & Offshore Structures |
| **Semester** | 2025-2026 Fall |
| **Instructor** | Dr. Deniz Bayraktar Bural |

> **Note**: Since the course is taught in Turkish, some figure outputs contain Turkish labels and annotations.

## Project Overview

This repository contains Python scripts developed for the **Ship and Marine Structures Hydrodynamics** course assignment. The analysis examines vessel seakeeping performance under irregular sea conditions using:

- **Wave Spectrum**: Single-parameter Bretschneider spectrum at Sea State 5
- **Wave Headings**: Head seas (180°) and beam seas (90°)
- **Motion Modes**: Heave (vertical displacement) and Pitch (rotational motion about transverse axis)

## Repository Structure

```
├── README.md                    # This documentation
├── requirements.txt             # Python dependencies
├── Rapor.pdf                    # Final report (Turkish)
│
├── 01_msi/                      # Motion Sickness Incidence
│   ├── README.md                # Module documentation
│   ├── msi_plot.py              # ISO 2631 comfort assessment
│   ├── MSI.xlsx                 # Input data
│   └── output/                  # Generated figures
│
├── 02_cg_rao/                   # CG Response Amplitude Operators
│   ├── README.md
│   ├── rao_plot.py              # Heave, Pitch, Roll RAOs
│   └── output/
│
├── 03_cg_spectra/               # CG Motion Response Spectra
│   ├── README.md
│   ├── cg_spectra_plot.py       # Spectral density plots
│   ├── spectra_data.csv         # Input data
│   └── output/
│
├── 04_remote_rao/               # Remote Location RAOs
│   ├── README.md
│   ├── rao_plot.py              # Officer cabin RAOs
│   └── output/
│
├── 05_remote_spectra/           # Remote Location Spectra
│   ├── README.md
│   ├── plot_spectra.py          # Multi-axis spectral plots
│   ├── data.txt                 # Input data
│   └── output/
│
├── 06_polar/                    # Polar Diagrams
│   ├── README.md
│   ├── polar_plot.py            # RMS vs wave heading
│   └── output/
│
├── 07_section_hydro/            # Section Hydrodynamic Coefficients
│   ├── README.md
│   ├── section_hydro_plot.py    # Multi-panel visualization
│   ├── section_hydro_academic.py # Publication format
│   ├── process_hydro_data.py    # Data processing
│   ├── Figure_Captions.md       # Academic captions
│   └── output/
│       ├── beam_seas/           # 90° heading results
│       └── head_seas/           # 180° heading results
│
└── 08_global_hydro/             # Global Hydrodynamic Coefficients
    ├── README.md
    ├── plot_hydro.py            # Wave excitation plots
    └── output/
```

## Theoretical Background

### Strip Theory Methodology

The seakeeping analysis is based on **Strip Theory** (Salvesen, Tuck & Faltinsen, 1970), which:

- Discretizes the hull into 2D cross-sections
- Computes hydrodynamic coefficients for each section
- Integrates sectional values to obtain global ship coefficients
- Solves coupled equations of motion in the frequency domain

### Key Equations

**Encounter Frequency:**

```
ωₑ = ω - (ω²V/g)cos(μ)
```

**Response Amplitude Operator:**

```
|H(ω)|² = |η(ω)/ζ(ω)|²
```

**Response Spectrum:**

```
Sᵣ(ωₑ) = |H(ωₑ)|² × Sᵥ(ωₑ)
```

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ship-seakeeping-analysis.git
cd ship-seakeeping-analysis

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage

Each module can be run independently:

```bash
# MSI Assessment
python 01_msi/msi_plot.py

# CG RAOs
python 02_cg_rao/rao_plot.py

# CG Spectra
python 03_cg_spectra/cg_spectra_plot.py

# Section Hydrodynamic Coefficients
python 07_section_hydro/section_hydro_academic.py
```

## Key Findings

The peak of the response spectrum does not always coincide with the wave spectrum peak because:

1. **RAO Resonance**: Vessel's natural frequency causes amplification at different frequencies
2. **Encounter Frequency Shift**: Forward speed causes Doppler-like frequency shift
3. **Transfer Function Shape**: RAO's frequency-dependent magnitude modifies spectral shape

## References

1. Salvesen, N., Tuck, E.O., & Faltinsen, O. (1970). "Ship Motions and Sea Loads." *SNAME Transactions*, Vol. 78.
2. St. Denis, M., & Pierson, W.J. (1953). "On the Motions of Ships in Confused Seas." *SNAME Transactions*, Vol. 61.
3. ISO 2631-1:1997. Mechanical vibration and shock evaluation.
4. Newman, J.N. (1977). *Marine Hydrodynamics*. MIT Press.

---
*Last updated: January 2026*
