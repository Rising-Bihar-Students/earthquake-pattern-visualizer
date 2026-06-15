### SEABOUR ###


'''JOINTPLOT- magnitude vs depth'''

#import os 
# print("Current Folder:",os.getcwd())

# import pandas as pd
# df=pd.read_csv(r"C:\Users\Deepak Kumar\Desktop\earthquake-pattern-visualizer\data\earthquakes_cleaned.csv")
# print(df.head())
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.jointplot(
#     data= pd.read_csv(r"C:\Users\Deepak Kumar\Desktop\earthquake-pattern-visualizer\data\earthquakes_cleaned.csv"),
#     x='mag',
#     y='depth',
#     kind='scatter'
# )

# plt.show()



'''HEATMAP '''

#import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# df = pd.read_csv(r"C:\Users\Deepak Kumar\Desktop\earthquake-pattern-visualizer\data\earthquakes_cleaned.csv")

# corr = df.corr(numeric_only=True)

# plt.figure(figsize=(10,8))
# sns.heatmap(corr, annot=True, cmap="coolwarm")

# plt.title("Earthquake Data Heatmap")
# plt.show()



'''PAIRPLOT'''

# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv(r"C:\Users\Deepak Kumar\Desktop\earthquake-pattern-visualizer\data\earthquakes_cleaned.csv")

# sns.pairplot(
#    df[["mag","depth","latitude","longitude"]]
# )
# plt.title("Earthquake Data Pairplot")
# plt.show()


"""MATPLOTLIB"""

'''scatter plot'''
# import matplotlib.pyplot as plt
# import pandas as pd

# df=df=pd.read_csv(r"C:\Users\Deepak Kumar\Desktop\earthquake-pattern-visualizer\data\earthquakes_cleaned.csv")
# plt.figure(figsize=(10,6))


# plt.scatter(
#     df["longitude"],
#     df["latitude"]
# )

# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.title("Earthquake Hotspots")

# plt.show()


'''TIMELINE PLOT'''

# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv(r"C:\Users\Deepak Kumar\Desktop\earthquake-pattern-visualizer\data\earthquakes_cleaned.csv")

# df_major = df[df["mag"] >= 6]

# plt.figure(figsize=(12,6))

# plt.plot(
#     df_major["time"],
#     df_major["mag"]
# )

# plt.xlabel("Time")
# plt.ylabel("Magnitude")
# plt.title("Major Earthquakes Over Time (Magnitude ≥ 6)")

# plt.xticks(rotation=45)

# plt.show()


"""BARPLOT"""

# import pandas as pd
# import matplotlib.pyplot as plt

# # CSV file load karo
# df=pd.read_csv(r"C:\Users\Deepak Kumar\Desktop\earthquake-pattern-visualizer\data\earthquakes_cleaned.csv")

# # Pehle 20 rows lo taki graph readable rahe
# plt.figure(figsize=(10,5))
# plt.bar(df['mag'][:20], df['depth'][:20])

# plt.title("Mag vs Depth")
# plt.xlabel("Mag")
# plt.ylabel("Depth")
# plt.savefig("C:/Users/Deepak Kumar/Desktop/earthquake-pattern-visualizer/images/barplot.jpg")

# plt.show()


"""HISTOGRAM"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
plt.figure(figsize=(8,5))
df=pd.read_csv(r"C:\Users\Deepak Kumar\Desktop\earthquake-pattern-visualizer\data\earthquakes_cleaned.csv")

sns.histplot(df['mag'], bins=10, kde=True)

plt.title("Distribution of Earthquake Magnitude")
plt.xlabel("Magnitude")
plt.ylabel("Count")
plt.savefig("C:/Users/Deepak Kumar/Desktop/earthquake-pattern-visualizer/images/histogram.jpg")

plt.show()