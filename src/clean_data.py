import pandas as pd

# Load merged dataset
df = pd.read_csv("D:/earthquake-pattern-visualizer/data/earthquakes_1976_2026.csv")

# Convert time column to datetime
df['time'] = pd.to_datetime(df['time'])

# Extract useful features
df['year'] = df['time'].dt.year
df['month'] = df['time'].dt.month
df['hour'] = df['time'].dt.hour

# Create bins for magnitude and depth
df['mag_bin'] = pd.cut(df['mag'], bins=[0,3,5,7,10], labels=['Minor','Moderate','Strong','Major'])
df['depth_bin'] = pd.cut(df['depth'], bins=[0,70,300,700], labels=['Shallow','Intermediate','Deep'])

# Drop unused column
df = df.drop(columns=["horizontalError", "depthError", "magError"])
df = df.drop(columns=[
    "magType", "nst", "gap", "dmin", "rms",
    "net", "id", "updated", "type",
    "magNst", "status", "locationSource", "magSource"
])

# Save cleaned dataset
df.to_csv("D:/earthquake-pattern-visualizer/data/earthquakes_cleaned.csv", index=False)

print("Cleaned dataset saved as earthquakes_cleaned.csv")
print(df.head())
