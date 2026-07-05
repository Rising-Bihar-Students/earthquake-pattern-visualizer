import pandas as pd
from pathlib import Path
# Project root (two levels up)
# If running as script
try:
    project_root = Path(__file__).resolve().parent.parent
except NameError:
# If in Jupyter/interactive mode
    project_root = Path.cwd().parent

# Paths
data_path = project_root / "data"

# Load CSVs from data folder
files = [
    f"{data_path}/eq_1976_1985.csv",
    f"{data_path}/eq_1986_1995.csv", 
    f"{data_path}/eq_1996_2005.csv", 
    f"{data_path}/eq_2006_2015.csv", 
    f"{data_path}/eq_2016_2026.csv"
]

# Read and merge
dfs = [pd.read_csv(f) for f in files]
df = pd.concat(dfs, ignore_index=True)

# Save merged file
df.to_csv(f"{data_path}/earthquakes_1976_2026.csv", index=False)

print("Merged dataset saved as earthquakes_1976_2026.csv")
print(df.shape)

df = pd.read_csv(f"{data_path}/earthquakes_1976_2026.csv")

print("Before:", df.shape)
df = df.drop_duplicates()
print("After:", df.shape)