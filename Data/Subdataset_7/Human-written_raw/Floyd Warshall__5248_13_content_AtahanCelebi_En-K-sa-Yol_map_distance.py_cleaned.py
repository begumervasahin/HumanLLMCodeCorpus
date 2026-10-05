import folium
import pandas as pd
def fonk1(path_v2):
    def fonk2(name,lat_list,long_list):
       b1 = [float(i) for i in lat_list ]
       b2 = [float(i) for i in long_list]
       b3 = pd.DataFrame({
           'lat': b2 ,
           'lon': b1,
           'name': name
       })
       b3
       b4 = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
       for i in range(0, len(b3)):
           folium.Marker([b3.iloc[i]['lon'], b3.iloc[i]['lat']], b5 = b3.iloc[i]['name']).add_to(b4)
       b4.save('unknown.html')
    b6 = open(path_v2,"r")
    b7 = list(b6)
    b3 = []
    for i in b7:
        b3.append(i.split(","))
    for i in range(len(b3)):
        b3[i][0] = str(i +1)
    b8 = list()
    b9 = list()
    b10 = list()
    b11 = list()
    for i in range(len(b3)):
        b8.append(b3[i][6])
        b9.append(b3[i][7])
        b10.append(b3[i][1])
        b11.append(b3[i][0])
    fonk2(b10,b8,b9)
    from geopy.geocoders import Nominatim
    from geopy.distance import great_circle
    b12 = Nominatim(user_agent="Hacettepe_Geomatik")
    b13 = []
    for j in range(len(b3)):
        b14 = b11[j]
        b15 = [b3[j][6],b3[j][7]]
        b16 = (float(b3[j][6]), float(b3[j][7]))
        for i in range(len(b8)):
            b17 = b11[i]
            b18 = (float(b3[i][6]), float(b3[i][7]))
            if b14 = = b17:
                continue
            b13.append([int(b14),int(b17),great_circle(b16, b18).km])
    return b13,len(b11)