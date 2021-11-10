import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import wkt
import mplleaflet



# importo las bases de datos de viajes y estaciones
viajes = pd.read_csv(".\Desktop\Tembici\BBDD\Septiembre.csv", encoding="utf8", sep=",")
estaciones = pd.read_csv(".\Desktop\Tembici\BBDD\estaciones.csv", encoding="utf8", sep=",")



# chequeo la cantidad de estaciones que tiene cada base a través de su id
len(viajes['Id de estación de inicio'].unique())  #251
len(estaciones['id'].unique())  #229
# hay menos estaciones en la base de estaciones



# realizamos un join de las bases matcheando por id de estación de origen en viajes
viajes_origen = pd.merge(viajes, estaciones, left_on='Id de estación de inicio', right_on='id', how='left')
viajes_origen[['Id de estación de inicio',"id"]].head(n=50)
# luego de hacer el join cuantifiquemos cuantas lograron matchear y cuantas no
len(viajes_origen)  #218137 misma cantidad que en viajes, es decir, no se perdió información
viajes_origen.isna().sum() #92583 registros de viajes corresponden a estaciones de origen sin matchear
viajes_origen = viajes_origen.dropna()  #eliminamos valores nulos 
len(viajes_origen)  #125552
col_ori = ['ID','Duración','Id de estación de inicio','Fecha de inicio','WKT','ubicacion'] #eliminamos las columnas que no son útiles
viajes_origen = viajes_origen[col_ori]



# realizamos un join de las bases matcheando por id de estación de destino en viajes
viajes_destino = pd.merge(viajes, estaciones, left_on='Id de estación de fin de viaje', right_on='id', how='left')
viajes_destino[['Id de estación de fin de viaje',"id"]].head(n=50)
# luego de hacer el join cuantifiquemos cuantas lograron matchear y cuantas no
len(viajes_destino)  #218137 misma cantidad que en viajes, es decir, no se perdió información
viajes_destino.isna().sum() #93071 registros de viajes corresponden a estaciones de origen sin matchear
viajes_destino = viajes_destino.dropna()  #eliminamos valores nulos 
len(viajes_destino)  #125066
col_dest = ['ID','Duración','Fecha de inicio','Id de estación de fin de viaje','WKT','ubicacion'] #eliminamos las columnas que no son útiles
viajes_destino = viajes_destino[col_dest]


#  tomamos una muestra
viajes_origen_muestra = viajes_origen.sample(500)
list(viajes_origen_muestra)
len(viajes_origen_muestra)


#  mapeamos la muestra
viajes_origen_muestra['geometry'] = viajes_origen_muestra.WKT.apply(wkt.loads)
viajes_origen_muestra.drop('WKT', axis=1, inplace=True) #Drop WKT column
gdf = gpd.GeoDataFrame(viajes_origen_muestra, geometry='geometry')
world = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
ax = world[world.name == 'Buenos Aires'].plot(
    color='white', edgecolor='black')
gdf.plot(ax=ax, color='red')
mplleaflet.show()

#  represetarlo en OSM




# Mostrar el mapa finalizado
viajes_origen_muestra.plot()


