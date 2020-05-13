import csv
import csvReader2
from operator import itemgetter, attrgetter




def exportCSV(tableau : list, fichier : str):   # definition de ma fonction
    if len(tableau) != 0:            # on gère un tableau vide
        header = tableau[0].keys()   # on recupére les catégories/descripteurs
        # On ouvre un fichier en écriture ('w') et on dit qu'on va le "formatter"
        # au format csv avec DictWriter. Les catégories du fichier csv sont données par 
        # header.
        fichierCSV = csv.DictWriter(open(fichier, 'w'), fieldnames = header) 
        fichierCSV.writeheader()     # on écrit les catégories/descripteurs
        for ligne in tableau:        # on lit la liste de dictionnaires (ligne est un dictionnaire)
            #print( ligne )
            fichierCSV.writerow(ligne) # on écrit les valeurs correspondant aux catégories dans la ligne ('row')
    return None                      # on met un return pour le plaisir

# print('')

#table = importCSV('exemple.csv')

#print(table[0])
#print(table[0:1])
#exportCSV(table,'test.csv')
# print('')

def filtrerLigne(tableau : list, critere : str, valeur : str):
    filtrerTableau = []
    for indice in range(len(tableau)):
        if tableau[indice][critere] == valeur:
            # on ajoute l'enregistrement numéro indice à tableauFiltrer
            filtrerTableau.append( tableau[indice] )
        #print(indice, tableau[indice][critere], valeur, tableau[indice][critere] == valeur)
    return filtrerTableau

#tableFiltree = filtrerLigne(table, 'Francais', '14')
#exportCSV(tableFiltree, 'maTableFiltree.csv')

def filtrerColonne(tableau : list, listeCriteres : str):
    filtrerTableau = []
    for enregistrement in tableau:
        dicoFiltrer = {}
        #print(enregistrement[listeCriteres])
        # on va parcourir toutes les clés qui sont dans la liste de Critères
        for critere in listeCriteres:
            # on ajoute les valeurs des enregistrements dans le dicoFiltrer.
            # on sélectionne les valeur qui correspondent au critere demandé.
            dicoFiltrer[critere] = enregistrement[critere]

        filtrerTableau.append(dicoFiltrer)
    return filtrerTableau

# print('debut')
# tableColonne = filtrerColonne( table, ['Nom', 'Francais'] )
# exportCSV(tableColonne, 'tableColonne.csv')
# print('fin')
'''
[
{'Nom': 'Erwann', 'Francais': '16', 'Science': '12', 'Histoire': '15'},
{'Nom': 'Celine', 'Francais': '14', 'Science': '16', 'Histoire': '13'},
{'Nom': 'Julien', 'Francais': '14', 'Science': '17', 'Histoire': '15'}
]
'''
#devient si on appelle filtrerColonne( table, 'Nom' )
'''
[
{'Nom': 'Erwann'}, 
{'Nom': 'Celine'}, 
{'Nom': 'Julien'}
]
'''

def triTable(tableau: list, critere: str, decroissant = False ):
    return sorted(tableau, key = lambda k: k[critere], reverse=decroissant)





table1 = csvReader2.importCSV('coronapays.csv')

def filtrer(tableau : list):
    filtrerTableau = []
    for dico in tableau:
        if dico == 'Autriche' or 'Belgique'or'Bulgarie':
            filtrerTableau.append(dico)
    return filtrerTableau
print(filtrer(table1))
exportCSV(filtrer,'exemplecoro.csv')
