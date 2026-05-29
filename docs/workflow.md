# Earthquake Pattern Visualizer – Workflow

## Overview
This document outlines the end-to-end workflow for the Earthquake Pattern Visualizer project. It explains how raw data is ingested, cleaned, enriched, and then used for visualization. The workflow ensures reproducibility and clarity for all team members.

---

## Workflow Stages

### 1. Data Ingestion
- **Source**: USGS Earthquake Catalog (FDSN Event Web Service).
- **Process**:
  - Download earthquake data in CSV format by decade (1976–1985, 1986–1995, 1996–2005, 2006–2015, 2016–2026).
  - Minimum magnitude: 2.5
  - Region: Latitude 5–40, Longitude 60–100
- **Output**: Raw CSV files stored in `data/`.

---

### 2. Data Merging
- **Script**: `src/load_data.py`
- **Process**:
  - Read all decade CSVs using Pandas.
  - Concatenate into one DataFrame.
  - Save as `earthquakes_1976_2026.csv`.
- **Output**: Merged dataset with ~27,624 records and 22 columns.

---

### 3. Data Cleaning & Feature Engineering
- **Script**: `src/clean_data.py`
- **Process**:
  - Convert `time` column to datetime.
  - Extract `year`, `month`, `hour`.
  - Create bins:
    - `mag_bin` → Minor, Moderate, Strong, Major
    - `depth_bin` → Shallow, Intermediate, Deep
  - Drop unused metadata columns (IDs, error fields, catalog info).
- **Output**: `earthquakes_cleaned.csv` with 11 analysis-ready columns.

---

### 4. Documentation
- **Folder**: `docs/`
- Files:
  - `data_cleaning.md` → Cleaning process details.
  - `data_dictionary.md` → Column definitions.
  - `workflow.md` → This workflow overview.
  - `visualization.md` → To be created by Naincy (plots + insights).

---

### 5. Visualization
- **Script/Notebook**: `src/visualize.py` or Jupyter notebooks.
- **Process** (Naincy):
  - Scatter/jointplot → Magnitude vs Depth.
  - Heatmap → Frequency by Year/Month.
  - Histogram → Magnitude distribution.
  - Bar plots → Counts by `mag_bin` and `depth_bin`.
  - Geographic scatter → Latitude vs Longitude hotspots.
  - Timeline → Major quakes over 50 years.
- **Output**: Saved plots + documented insights in `docs/visualization.md`.

---

## Team Roles
- **Ram Bhagat Thakur** → Data ingestion, cleaning, feature engineering, documentation.
- **Naincy** → Visualization design, plotting, storytelling, visualization documentation.

---

## Final Deliverables
- Cleaned dataset: `earthquakes_cleaned.csv`
- Documentation: `docs/` folder with `.md` files
- Visualizations: Plots + insights for presentation/demo
