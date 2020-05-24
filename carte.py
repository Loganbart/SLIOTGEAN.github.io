import folium
import os
import json

#créer une carte
m = folium.Map(location=[48.856614, 12.432786], zoom_start=8)#pour créer la map

tooltip='Cliquez ici pour plus info'

#création de logo pour pays

logoFrance= folium.features.CustomIcon('france.png',icon_size=(70,70))
logoAllemagne= folium.features.CustomIcon('allemagne.png',icon_size=(70,70))
logoAutriche= folium.features.CustomIcon('autriche.png',icon_size=(50,50))
logoBelgique= folium.features.CustomIcon('belgique.png',icon_size=(50,50))
logoBulgarie= folium.features.CustomIcon('Bulgarie.png',icon_size=(50,50))
logoChypre= folium.features.CustomIcon('chypre.png',icon_size=(50,50))
logoCroatie= folium.features.CustomIcon('croatie.png',icon_size=(50,50))
logoDanemark= folium.features.CustomIcon('Danemark.png',icon_size=(50,50))
logoEspagne= folium.features.CustomIcon('espagne.png',icon_size=(80,80))
logoEstionie= folium.features.CustomIcon('estonie.png',icon_size=(50,50))
logoFinlande= folium.features.CustomIcon('finlande.png',icon_size=(50,50))
logoGrece= folium.features.CustomIcon('grece.png',icon_size=(50,50))
logoHongrie= folium.features.CustomIcon('hongrie.png',icon_size=(50,50))
logoIrlande= folium.features.CustomIcon('irland.png',icon_size=(50,50))
logoItalie= folium.features.CustomIcon('italie.png',icon_size=(70,70))
logoLettonie= folium.features.CustomIcon('Lettonie.png',icon_size=(50,50))
logoLituanie= folium.features.CustomIcon('Lituanie.png',icon_size=(50,50))
logoLuxembourg= folium.features.CustomIcon('Luxembourg.png',icon_size=(50,50))
logoMalte= folium.features.CustomIcon('Malte.png',icon_size=(50,50))
logoPaysBas= folium.features.CustomIcon('Pays-Bas.png',icon_size=(50,50))
logoPologne= folium.features.CustomIcon('Pologne.png',icon_size=(50,50))
logoPortugal= folium.features.CustomIcon('Portugal.png',icon_size=(50,50))
logoRepubliqueTcheque = folium.features.CustomIcon('Republiquetcheque.png',icon_size=(50,50))
logoRoumanie= folium.features.CustomIcon('Roumanie.png',icon_size=(50,50))
logoSlovaquie= folium.features.CustomIcon('Slovaquie.png',icon_size=(50,50))
logoSlovenie= folium.features.CustomIcon('Slovenie.png',icon_size=(50,50))
logoSuede= folium.features.CustomIcon('Suede.png',icon_size=(50,50))

chartFrance ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-01-28", "infecté": 4},
 {"2020": "2020-02-08", "infecté": 11},
 {"2020": "2020-02-18", "infecté": 12},
 {"2020": "2020-02-28", "infecté": 57},
 {"2020": "2020-03-08", "infecté": 1126},
 {"2020": "2020-03-18", "infecté": 9134},
 {"2020": "2020-03-28", "infecté": 37575},
 {"2020": "2020-04-08", "infecté": 103302},
 {"2020": "2020-04-18", "infecté": 151393},
 {"2020": "2020-04-28", "infecté": 165842},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}


chartAllemagne ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-01-28", "infecté": 4},
 {"2020": "2020-02-08", "infecté": 13},
 {"2020": "2020-02-18", "infecté": 16},
 {"2020": "2020-02-28", "infecté": 48},
 {"2020": "2020-03-08", "infecté": 1040},
 {"2020": "2020-03-18", "infecté": 12327},
 {"2020": "2020-03-28", "infecté": 57695},
 {"2020": "2020-04-08", "infecté": 113296},
 {"2020": "2020-04-18", "infecté": 143342},
 {"2020": "2020-04-28", "infecté": 159038},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartAutriche ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-02-28", "infecté": 3},
 {"2020": "2020-03-08", "infecté": 104},
 {"2020": "2020-03-18", "infecté": 1646},
 {"2020": "2020-03-28", "infecté": 8271},
 {"2020": "2020-04-08", "infecté": 12942},
 {"2020": "2020-04-18", "infecté": 14771},
 {"2020": "2020-04-28", "infecté": 15357},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartBelgique ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-02-08", "infecté": 1},
 {"2020": "2020-02-18", "infecté": 1},
 {"2020": "2020-02-28", "infecté": 1},
 {"2020": "2020-03-08", "infecté": 200},
 {"2020": "2020-03-18", "infecté": 1486},
 {"2020": "2020-03-28", "infecté": 9134},
 {"2020": "2020-04-08", "infecté": 23403},
 {"2020": "2020-04-18", "infecté": 37183},
 {"2020": "2020-04-28", "infecté": 47334},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartBulgarie ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-03-08", "infecté": 4},
 {"2020": "2020-03-18", "infecté": 92},
 {"2020": "2020-03-28", "infecté": 331},
 {"2020": "2020-04-08", "infecté": 593},
 {"2020": "2020-04-18", "infecté": 878},
 {"2020": "2020-04-28", "infecté": 1399},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}
chartChypre ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-03-08", "infecté": 2},
 {"2020": "2020-03-18", "infecté": 49},
 {"2020": "2020-03-28", "infecté": 179},
 {"2020": "2020-04-08", "infecté": 526},
 {"2020": "2020-04-18", "infecté": 761},
 {"2020": "2020-04-28", "infecté": 837},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartCroatie ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-02-28", "infecté": 5},
 {"2020": "2020-03-08", "infecté": 12},
 {"2020": "2020-03-18", "infecté": 81},
 {"2020": "2020-03-28", "infecté": 657},
 {"2020": "2020-04-08", "infecté": 1343},
 {"2020": "2020-04-18", "infecté": 1832},
 {"2020": "2020-04-28", "infecté": 2047},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartDanemark ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-02-28", "infecté": 1},
 {"2020": "2020-03-08", "infecté": 35},
 {"2020": "2020-03-18", "infecté": 1057},
 {"2020": "2020-03-28", "infecté": 2211},
 {"2020": "2020-04-08", "infecté": 5413},
 {"2020": "2020-04-18", "infecté": 7253},
 {"2020": "2020-04-28", "infecté": 8862},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartEspagne ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-02-08", "infecté": 1},
 {"2020": "2020-02-18", "infecté": 2},
 {"2020": "2020-02-28", "infecté": 32},
 {"2020": "2020-03-08", "infecté": 673},
 {"2020": "2020-03-18", "infecté": 13910},
 {"2020": "2020-03-28", "infecté": 73235},
 {"2020": "2020-04-08", "infecté": 113296},
 {"2020": "2020-04-18", "infecté": 191726},
 {"2020": "2020-04-28", "infecté": 232128},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartFinlande ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-01-28", "infecté": 1},
 {"2020": "2020-02-08", "infecté": 1},
 {"2020": "2020-02-18", "infecté": 1},
 {"2020": "2020-02-28", "infecté": 2},
 {"2020": "2020-03-08", "infecté": 23},
 {"2020": "2020-03-18", "infecté": 336},
 {"2020": "2020-03-28", "infecté": 1167},
 {"2020": "2020-04-08", "infecté": 2487},
 {"2020": "2020-04-18", "infecté": 3681},
 {"2020": "2020-04-28", "infecté": 4740},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartEstonie ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-02-28", "infecté": 1},
 {"2020": "2020-03-08", "infecté": 10},
 {"2020": "2020-03-18", "infecté": 258},
 {"2020": "2020-03-28", "infecté": 645},
 {"2020": "2020-04-08", "infecté": 1185},
 {"2020": "2020-04-18", "infecté": 1512},
 {"2020": "2020-04-28", "infecté": 1660},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartGrece ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-02-28", "infecté": 4},
 {"2020": "2020-03-08", "infecté": 73},
 {"2020": "2020-03-18", "infecté": 418},
 {"2020": "2020-03-28", "infecté": 1061},
 {"2020": "2020-04-08", "infecté": 1884},
 {"2020": "2020-04-18", "infecté": 2235},
 {"2020": "2020-04-28", "infecté": 2534},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartHongrie ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-03-08", "infecté": 7},
 {"2020": "2020-03-18", "infecté": 58},
 {"2020": "2020-03-28", "infecté": 343},
 {"2020": "2020-04-08", "infecté": 895},
 {"2020": "2020-04-18", "infecté": 1834},
 {"2020": "2020-04-28", "infecté": 2649},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartIrlande ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-02-28", "infecté": 1},
 {"2020": "2020-03-08", "infecté": 19},
 {"2020": "2020-03-18", "infecté": 292},
 {"2020": "2020-03-28", "infecté": 2415},
 {"2020": "2020-04-08", "infecté": 6074},
 {"2020": "2020-04-18", "infecté": 14758},
 {"2020": "2020-04-28", "infecté": 19648},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartItalie ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-01-28", "infecté": 2},
 {"2020": "2020-02-08", "infecté": 3},
 {"2020": "2020-02-18", "infecté": 3},
 {"2020": "2020-02-28", "infecté": 888},
 {"2020": "2020-03-08", "infecté": 7375},
 {"2020": "2020-03-18", "infecté": 35713},
 {"2020": "2020-03-28", "infecté": 92472},
 {"2020": "2020-04-08", "infecté": 139422},
 {"2020": "2020-04-18", "infecté": 175925},
 {"2020": "2020-04-28", "infecté": 199414},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}
chartLettonie ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-03-08", "infecté": 2},
 {"2020": "2020-03-18", "infecté": 71},
 {"2020": "2020-03-28", "infecté": 305},
 {"2020": "2020-04-08", "infecté": 577},
 {"2020": "2020-04-18", "infecté": 712},
 {"2020": "2020-04-28", "infecté": 838},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}
chartLituanie ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-03-08", "infecté": 1},
 {"2020": "2020-03-18", "infecté": 27},
 {"2020": "2020-03-28", "infecté": 394},
 {"2020": "2020-04-08", "infecté": 912},
 {"2020": "2020-04-18", "infecté": 1239},
 {"2020": "2020-04-28", "infecté": 1344},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartLuxembourg ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-02-28", "infecté": 1},
 {"2020": "2020-03-08", "infecté": 3},
 {"2020": "2020-03-18", "infecté": 203},
 {"2020": "2020-03-28", "infecté": 1831},
 {"2020": "2020-04-08", "infecté": 3034},
 {"2020": "2020-04-18", "infecté": 3537},
 {"2020": "2020-04-28", "infecté": 3729},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartMalte ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-03-08", "infecté": 3},
 {"2020": "2020-03-18", "infecté": 38},
 {"2020": "2020-03-28", "infecté": 149},
 {"2020": "2020-04-08", "infecté": 299},
 {"2020": "2020-04-18", "infecté": 426},
 {"2020": "2020-04-28", "infecté": 458},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartPaysBas ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-02-28", "infecté": 1},
 {"2020": "2020-03-08", "infecté": 265},
 {"2020": "2020-03-18", "infecté": 2056},
 {"2020": "2020-03-28", "infecté": 9819},
 {"2020": "2020-04-08", "infecté": 20682},
 {"2020": "2020-04-18", "infecté": 31766},
 {"2020": "2020-04-28", "infecté": 38612},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartPologne ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-03-08", "infecté": 11},
 {"2020": "2020-03-18", "infecté": 251},
 {"2020": "2020-03-28", "infecté": 1638},
 {"2020": "2020-04-08", "infecté": 5205},
 {"2020": "2020-04-18", "infecté": 8742},
 {"2020": "2020-04-28", "infecté": 12089},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartPortugal ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-03-08", "infecté": 30},
 {"2020": "2020-03-18", "infecté": 448},
 {"2020": "2020-03-28", "infecté": 5170},
 {"2020": "2020-04-08", "infecté": 13141},
 {"2020": "2020-04-18", "infecté": 19685},
 {"2020": "2020-04-28", "infecté": 24322},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartRepubliqueTcheque ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-03-08", "infecté": 31},
 {"2020": "2020-03-18", "infecté": 464},
 {"2020": "2020-03-28", "infecté": 2631},
 {"2020": "2020-04-08", "infecté": 5312},
 {"2020": "2020-04-18", "infecté": 6606},
 {"2020": "2020-04-28", "infecté": 7449},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartRoumanie ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-02-28", "infecté": 3},
 {"2020": "2020-03-08", "infecté": 15},
 {"2020": "2020-03-18", "infecté": 260},
 {"2020": "2020-03-28", "infecté": 1452},
 {"2020": "2020-04-08", "infecté": 4761},
 {"2020": "2020-04-18", "infecté": 8418},
 {"2020": "2020-04-28", "infecté": 11616},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartSlovaquie ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-03-08", "infecté": 3},
 {"2020": "2020-03-18", "infecté": 105},
 {"2020": "2020-03-28", "infecté": 292},
 {"2020": "2020-04-08", "infecté": 682},
 {"2020": "2020-04-18", "infecté": 1089},
 {"2020": "2020-04-28", "infecté": 1384},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartSlovenie ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-03-08", "infecté": 16},
 {"2020": "2020-03-18", "infecté": 275},
 {"2020": "2020-03-28", "infecté": 684},
 {"2020": "2020-04-08", "infecté": 1091},
 {"2020": "2020-04-18", "infecté": 1317},
 {"2020": "2020-04-28", "infecté": 1408},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}

chartSuede ={
 "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
 "description": "A simple bar chart with embedded data.",
 "width":450,
 "height":250,
 "data": {
 "values": [
 {"2020": "2020-01-28", "infecté": 1},
 {"2020": "2020-02-08", "infecté": 1},
 {"2020": "2020-02-18", "infecté": 1},
 {"2020": "2020-02-28", "infecté": 7},
 {"2020": "2020-03-08", "infecté": 203},
 {"2020": "2020-03-18", "infecté": 1279},
 {"2020": "2020-03-28", "infecté": 3447},
 {"2020": "2020-04-08", "infecté": 8419},
 {"2020": "2020-04-18", "infecté": 13822},
 {"2020": "2020-04-28", "infecté": 19621},
 ]
 },
 "mark": "line",
 "encoding": {
 "x": {"field": "2020", "type": "temporal", "axis": {"labelAngle": 200}},
 "y": {"field": "infecté", "type": "quantitative"},
 "color":{
     "value":"red"}
 }
}
#création des pop'up


folium.Marker([46.954994, 2.396425],
              popup=folium.Popup().add_child(folium.VegaLite(chartFrance,width=600,height=200)),
              tooltip=tooltip,
              icon=logoFrance).add_to(m),
folium.Marker([50.74599, 9.766473],
              popup=folium.Popup().add_child(folium.VegaLite(chartAllemagne,width=600,height=200)),
              tooltip=tooltip,
              icon=logoAllemagne).add_to(m),
folium.Marker([47.200033,13.199959],
              popup=folium.Popup().add_child(folium.VegaLite(chartAutriche,width=600,height=200)),
              tooltip=tooltip,
              icon=logoAutriche).add_to(m),
folium.Marker([50.728141,4.511679],
              popup=folium.Popup().add_child(folium.VegaLite(chartBelgique,width=600,height=200)),
              tooltip=tooltip,
              icon=logoBelgique).add_to(m),
folium.Marker([42.583782,25.357713],
              popup=folium.Popup().add_child(folium.VegaLite(chartBulgarie,width=600,height=200)),
              tooltip=tooltip,
              icon=logoBulgarie).add_to(m),
folium.Marker([34.982301,33.145128],
              popup=folium.Popup().add_child(folium.VegaLite(chartChypre,width=600,height=200)),
              tooltip=tooltip,
              icon=logoChypre).add_to(m),
folium.Marker([45.673257,16.483329],
              popup=folium.Popup().add_child(folium.VegaLite(chartCroatie,width=600,height=200)),
              tooltip=tooltip,
              icon=logoCroatie).add_to(m),
folium.Marker([56.131198,9.116544],
              popup=folium.Popup().add_child(folium.VegaLite(chartDanemark,width=600,height=200)),
              tooltip=tooltip,
              icon=logoDanemark).add_to(m),
folium.Marker([40.340856,-3.082582],
              popup=folium.Popup().add_child(folium.VegaLite(chartEspagne,width=600,height=200)),
              tooltip=tooltip,
              icon=logoEspagne).add_to(m),
folium.Marker([58.752377,25.331907],
              popup=folium.Popup().add_child(folium.VegaLite(chartEstonie,width=600,height=200)),
              tooltip=tooltip,
              icon=logoEstionie).add_to(m),
folium.Marker([63.763860,26.078146],
              popup=folium.Popup().add_child(folium.VegaLite(chartFinlande,width=600,height=200)),
              tooltip=tooltip,
              icon=logoFinlande).add_to(m),
folium.Marker([39.091474,21.932379],
              popup=folium.Popup().add_child(folium.VegaLite(chartGrece,width=600,height=200)),
              tooltip=tooltip,
              icon=logoGrece).add_to(m),
folium.Marker([47.181758,19.506093],
              popup=folium.Popup().add_child(folium.VegaLite(chartHongrie,width=600,height=200)),
              tooltip=tooltip,
              icon=logoHongrie).add_to(m),
folium.Marker([52.865196,-7.979459],
              popup=folium.Popup().add_child(folium.VegaLite(chartIrlande,width=600,height=200)),
              tooltip=tooltip,
              icon=logoIrlande).add_to(m),
folium.Marker([42.099006,13.518622],
              popup=folium.Popup().add_child(folium.VegaLite(chartItalie,width=600,height=200)),
              tooltip=tooltip,
              icon=logoItalie).add_to(m),
folium.Marker([56.840649,24.753764],
              popup=folium.Popup().add_child(folium.VegaLite(chartLettonie,width=600,height=200)),
              tooltip=tooltip,
              icon=logoLettonie).add_to(m),
folium.Marker([55.350000,23.749999],
              popup=folium.Popup().add_child(folium.VegaLite(chartLituanie,width=600,height=200)),
              tooltip=tooltip,
              icon=logoLituanie).add_to(m),
folium.Marker([49.754361,6.117630],
              popup=folium.Popup().add_child(folium.VegaLite(chartLuxembourg,width=600,height=200)),
              tooltip=tooltip,
              icon=logoLuxembourg).add_to(m),
folium.Marker([35.888599,14.447691],
              popup=folium.Popup().add_child(folium.VegaLite(chartMalte,width=600,height=200)),
              tooltip=tooltip,
              icon=logoMalte).add_to(m),
folium.Marker([52.247649,5.541246],
              popup=folium.Popup().add_child(folium.VegaLite(chartPaysBas,width=600,height=200)),
              tooltip=tooltip,
              icon=logoPaysBas).add_to(m),
folium.Marker([52.215933,19.134422],
              popup=folium.Popup().add_child(folium.VegaLite(chartPologne,width=600,height=200)),
              tooltip=tooltip,
              icon=logoPologne).add_to(m),
folium.Marker([39.824872,-8.408225],
              popup=folium.Popup().add_child(folium.VegaLite(chartPortugal,width=600,height=200)),
              tooltip=tooltip,
              icon=logoPortugal).add_to(m),
folium.Marker([49.816700,15.474954],
              popup=folium.Popup().add_child(folium.VegaLite(chartRepubliqueTcheque,width=600,height=200)),
              tooltip=tooltip,
              icon=logoRepubliqueTcheque).add_to(m),
folium.Marker([45.985212,24.685922],
              popup=folium.Popup().add_child(folium.VegaLite(chartRoumanie,width=600,height=200)),
              tooltip=tooltip,
              icon=logoRoumanie).add_to(m),
folium.Marker([48.741152,19.452864],
              popup=folium.Popup().add_child(folium.VegaLite(chartSlovaquie,width=600,height=200)),
              tooltip=tooltip,
              icon=logoSlovaquie).add_to(m),
folium.Marker([45.813311,14.480836],
              popup=folium.Popup().add_child(folium.VegaLite(chartSlovenie,width=600,height=200)),
              tooltip=tooltip,
              icon=logoSlovenie).add_to(m),
folium.Marker([59.674971,14.520858],
              popup=folium.Popup().add_child(folium.VegaLite(chartSuede,width=600,height=200)),
              tooltip=tooltip,
              icon=logoSuede).add_to(m),


m.save('cart.html')#génerer la map sur carte.html
