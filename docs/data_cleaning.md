# Data Cleaning Documentation

## Overview
This document explains the steps taken to clean and prepare the earthquake dataset (1976–2026) for analysis and visualization. The goal was to transform raw USGS earthquake data into a lean, structured dataset that highlights the most relevant features for pattern analysis.

---

## Raw Data
- Source: [[USGS Earthquake Catalog](https://earthquake.usgs.gov/earthquakes/search/)] (CSV downloads by decade).
- Initial columns: 22 fields including technical metadata (errors, catalog IDs, etc.).
- Total records: ~27,624 earthquakes (Magnitude ≥ 2.5, Asia region).

---

## Cleaning Steps
1. **Merge Decade Files**
   - Combined five CSVs (1976–1985, 1986–1995, 1996–2005, 2006–2015, 2016–2026).
   - Saved as `earthquakes_1976_2026.csv`.

2. **Datetime Conversion**
   - Converted `time` column to proper datetime format.
   - Extracted `year`, `month`, and `hour` for temporal analysis.

3. **Feature Engineering**
   - Created `mag_bin` (Minor, Moderate, Strong, Major).
   - Created `depth_bin` (Shallow, Intermediate, Deep).

4. **Column Reduction**
   - Dropped unused metadata: `magType`, `nst`, `gap`, `dmin`, `rms`, `net`, `id`, `updated`, `type`, `magNst`, `status`, `locationSource`, `magSource`, and error columns.
   - Retained only analysis-relevant fields.

---

## Final Dataset
**File:** `earthquakes_cleaned.csv`  
**Columns:**
- `time` → UTC timestamp
- `latitude`, `longitude` → geographic coordinates
- `depth` → depth in km
- `mag` → magnitude
- `place` → human-readable location
- `year`, `month`, `hour` → derived temporal features
- `mag_bin` → categorized magnitude
- `depth_bin` → categorized depth

---

## Purpose
This cleaned dataset is now ready for:
- Trend analysis (yearly, monthly, hourly).
- Magnitude vs depth relationships.
- Geographic hotspot mapping.
- Storytelling with human-readable locations.

---