docs/visualization.md so she can fill it in as she builds plots:

markdown
# Earthquake Pattern Visualizer – Visualization Documentation

## Overview
This document records the visualizations created from the cleaned dataset (`earthquakes_cleaned.csv`). Each section explains the purpose of the plot, the method used, and the insights gained.

---

## 1. Magnitude vs Depth
- **Plot Type**: Scatter / Jointplot
- **Purpose**: To explore the relationship between earthquake magnitude and depth.
- **Code Example**:
  ```python
  sns.jointplot(data=df, x="depth", y="mag", kind="scatter", alpha=0.5)
Insights: (To be filled by Naincy)

2. Earthquake Frequency by Year and Month
Plot Type: Heatmap

Purpose: To identify seasonal or yearly patterns in earthquake occurrence.

Code Example:

python
pivot = df.pivot_table(index="year", columns="month", values="mag", aggfunc="count")
sns.heatmap(pivot, cmap="Reds", linewidths=0.5)
Insights: (To be filled by Naincy)

3. Magnitude Distribution
Plot Type: Histogram

Purpose: To show how earthquake magnitudes are distributed.

Code Example:

python
sns.histplot(df["mag"], bins=30, kde=True)
Insights: (To be filled by Naincy)

4. Counts by Magnitude and Depth Categories
Plot Type: Bar Plot

Purpose: To compare frequency of quakes across bins.

Code Example:

python
sns.countplot(data=df, x="mag_bin")
sns.countplot(data=df, x="depth_bin")
Insights: (To be filled by Naincy)

5. Geographic Hotspots
Plot Type: Scatter Map (Latitude vs Longitude)

Purpose: To visualize earthquake locations and identify clusters.

Code Example:

python
plt.scatter(df["longitude"], df["latitude"], c=df["mag"], cmap="Reds", alpha=0.5)
Insights: (To be filled by Naincy)

6. Timeline of Major Quakes
Plot Type: Line Plot / Timeline

Purpose: To highlight major earthquakes over 50 years.

Code Example:

python
major_quakes = df[df["mag"] >= 6.5]
plt.plot(major_quakes["time"], major_quakes["mag"], "o")
Insights: (To be filled by Naincy)

Notes
All plots should be saved as images (.png) in a figures/ folder.

Each plot must include a title, axis labels, and legend where appropriate.

Insights should connect visual patterns to real‑world interpretation.

Next Steps
Add plots to docs/visualization.md with screenshots or references.

Summarize findings in the final project report.

Code

---

### ✅ Commit Instructions
Run:
```bash
git add docs/visualization.md
git commit -m "Added visualization documentation template for Naincy"
git push origin ram-dev