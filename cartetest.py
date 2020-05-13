import folium
import os
import json

#créer une carte
m = folium.Map(location=[48.856614, 2.3522219], zoom_start=6)#pour créer la map

tooltip='Cliquez ici pour plus info'


chartAllemagne ={
 "description": "A simple bar chart with embedded data.",
 "autosize" : { "type" : "fit-x"},
 "data": {
 "values": [
 {"date": "2020-01-28", "infected": 4},
 {"date": "2020-02-08", "infected": 13},
 {"date": "2020-02-18", "infected": 16},
 {"date": "2020-02-28", "infected": 48},
 {"date": "2020-03-08", "infected": 1040},
 {"date": "2020-03-18", "infected": 12327},
 {"date": "2020-03-28", "infected": 57695},
 {"date": "2020-04-08", "infected": 113296},
 {"date": "2020-04-18", "infected": 143342},
 {"date": "2020-04-28", "infected": 159038}
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "date", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infected", "type": "quantitative"},
 "color":{"value":"red"}
 }
}


folium.Marker([50.74599, 9.766473],
              popup=folium.Popup().add_child(folium.VegaLite(chartAllemagne,width=600,height=200))
             ).add_to(m),



m.save('cart.html')#génerer la map sur carte.html
