import folium
import pandas as pd
import numpy as np

df=pd.read_csv('volcanos.csv')
coordinates=np.asarray(df[['Lat','Lon','Elv']])
def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<= elevation<3000:
        return 'orange'
    else:
        return 'red'

        
map=folium.Map(location=[23.178460, 88.451267],zoom_start=6,tiles="Stamen Terrain")#'Mapbox Bright'

fgp=folium.FeatureGroup(name='Populations')
fgp.add_child(
    folium.GeoJson(
        data=open('world.json','r',encoding='utf-8-sig').read(),
        style_function=lambda x:{'fillColor':'yellow' if x["properties"]["POP2005"] < 10000000 
        else 'green' if 10000000 <=x["properties"]["POP2005"]<20000000 else 'red'}
    )
)

fgv=folium.FeatureGroup(name='Volcanoes')
for coordinate in coordinates:
    fgv.add_child(
        folium.CircleMarker(
            location=[coordinate[0],coordinate[1]],
            radius=6,
            popup=f"{coordinate[2]} m",
            fill_color=color_producer(coordinate[2]),
            color='grey',fill=True,fill_opacity=0.7
            )
        )

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('demo.html')