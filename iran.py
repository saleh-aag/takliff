
import geopandas as gpd  
import matplotlib.pyplot as plt  

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))  
asia = world[world['continent'] == 'Asia']  
iran = asia[asia['name'] == 'Iran']  

fig, ax = plt.subplots(figsize=(10, 10))  
asia.plot(ax=ax, color='lightgrey')  
iran.plot(ax=ax, color='orange')  

ax.set_title('Map of Asia with Highlighted Iran')  
ax.set_xlabel('Longitude')  
ax.set_ylabel('Latitude')  

plt.show()  
