import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib
import os


# Load the dataset
chunk_size = 500000  # Define the number of rows to read at a time
chunks = []

for chunk in pd.read_csv('US_Accidents_March23.csv', chunksize=chunk_size):
    # Process each chunk of data here
    # For example, let's print the first 5 rows of each chunk
    # 
    if True:
        print(chunk.head())
        print("Done")
        chunks.append(chunk)
        break

# Concatenate all chunks into one DataFrame
data = pd.concat(chunks, axis=0)

# Display the first few rows of the dataset
print(data.head())

# Analysis for city
import seaborn as sns

cities = data.City.unique()
len(cities)
cities_by_accident = data.City.value_counts()
top20_city = cities_by_accident.head(20)

'New York' in data.City
'NY' in data.State
barplot=sns.barplot(y=top20_city.keys(),x=top20_city.values)

# Add title and labels
plt.title('cities By accident')
plt.xlabel('Values')
plt.ylabel('Top 20 Cities')

# Show the plot
plt.show()


fig, axes = plt.subplots(1, 2, figsize=(15, 5))
datasever=data['Severity'][:10]
sns.lineplot(ax=axes[1],x=data['ID'][:10],y=datasever,data=data,marker='d')
datavis=data['Visibility(mi)'][:10]
sns.lineplot(ax=axes[0],x=data['ID'][:10],y=datavis,data=data,marker='d')
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(15, 5))
sns.histplot(data['Wind_Direction'],kde=False,color='blue',bins=10,ax=axes[0])
sns.histplot(data['Wind_Speed(mph)'],kde=False,color='pink',bins=10,ax=axes[1])
plt.show()


data['Timezone'].value_counts().plot.bar()
plt.show()

plt.figure(figsize=(5,5))
plt.pie(data['Amenity'].value_counts(),startangle=90,autopct='%.2f',labels=['TRUE','FALSE']);
plt.show()

import folium
import webbrowser

class Map:
    def __init__(self,center,zoom_start):
        self.center = center
        self.zoom_start = zoom_start
        
    def showMap(self):
        accident_map =  folium.Map(location= self.center , zoom_start= self.zoom_start)
        for index, row in data.sample(1000).iterrows():
            folium.Marker([row['Start_Lat'], row['Start_Lng']]).add_to(accident_map)


        accident_map.save("map.html")
        webbrowser.open("map.html")
        print(accident_map)
        # display(accident_map) 
coords = [data['Start_Lat'].mean(), data['Start_Lng'].mean()]
map = Map(center= coords , zoom_start=5)
map.showMap()






