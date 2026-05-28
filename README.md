# 🌍 Earthquake Pattern Visualizer – Disaster Data

This project analyzes **50 years of earthquake records from the USGS catalog**, focusing on the **India/Asia region**.  
The goal is to uncover patterns in earthquake magnitude, depth, timing, and geographic distribution, and present them through clear, scientific visualizations.

---

## 🔍 Project Overview
We are building a **data science pipeline**:
1. **Data ingestion** → Load CSV from USGS.
2. **Filtering** → Focus on India/Asia region.
3. **Feature engineering** → Create bins for magnitude, depth, and time of day.
4. **Visualization** → Generate plots using Seaborn and Matplotlib.

---

## 📊 Visualizations
- **Seaborn**
  - Jointplot: Magnitude vs Depth
  - Heatmap: Quakes by Month vs Year
  - Pairplot: Relationships between all variables
- **Matplotlib**
  - Scatter plot: Geographic hotspots (longitude vs latitude)
  - Timeline plot: Major quakes over time

---

## 🎯 Why It Matters
- **Scientific insight** → Understand earthquake behavior in Asia over decades.  
- **Disaster awareness** → Identify hotspots and trends useful for preparedness.  
- **Learning outcome** → Apply Python, Pandas, NumPy, Seaborn, and Matplotlib in a real-world data science project.  
- **Presentation impact** → Serious subject, naturally dramatic visuals that leave a strong impression.

---

## 🛠 Tech Stack
- **Python** (data analysis & visualization)  
- **Pandas / NumPy** (data cleaning, binning, feature engineering)  
- **Seaborn** (statistical plots)  
- **Matplotlib** (custom plots, geographic scatter, timelines)

---

## 📂 Project Structure
```plaintext
earthquake-pattern-visualizer/
├── data/                # raw CSV files
├── notebooks/           # Jupyter notebooks for experiments
├── src/                 # Python scripts (cleaning, plotting)
├── README.md            # project overview
├── requirements.txt     # libraries needed
```

---

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/Rising-Bihar-Students/earthquake-pattern-visualizer.git
   cd earthquake-pattern-visualizer
   ```
2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

3. Run the Jupyter notebook or Python scripts to generate visualizations.

---

---

## 👥 Team Collaboration
- **Ram Bhagat Thakur** → Data cleaning, feature engineering, Pandas/Numpy  
- **Naincy** → Visualization design, Seaborn/Matplotlib plots  

**Workflow**: Use branches (`ram-dev`, `naincy-dev`) and merge via pull requests after review.

---

## 📌 Deliverables
- Cleaned dataset (filtered for Asia)  
- Scripts/notebooks for analysis  
- Visualizations saved as PNGs  
- README explaining project purpose and workflow  
