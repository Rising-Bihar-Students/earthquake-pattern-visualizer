import pandas as pd

'''
# Load CSVs from data folder
files = [
    "D:/earthquake-pattern-visualizer/data/eq_1976_1985.csv",
    "D:/earthquake-pattern-visualizer/data/eq_1986_1995.csv", 
    "D:/earthquake-pattern-visualizer/data/eq_1996_2005.csv", 
    "D:/earthquake-pattern-visualizer/data/eq_2006_2015.csv", 
    "D:/earthquake-pattern-visualizer/data/eq_2016_2026.csv"
]

# Read and merge
dfs = [pd.read_csv(f) for f in files]
df = pd.concat(dfs, ignore_index=True)

# Save merged file
df.to_csv("D:/earthquake-pattern-visualizer/data/earthquakes_1976_2026.csv", index=False)

print("Merged dataset saved as earthquakes_1976_2026.csv")
print(df.shape)
'''

df = pd.read_csv("D:/earthquake-pattern-visualizer/data/earthquakes_1976_2026.csv")

print("Before:", df.shape)
df = df.drop_duplicates()
print("After:", df.shape)
