"""SEABOUR"""


'''JOINTPLOT'''

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



'''HEATMAP'''

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