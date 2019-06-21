import sys
import matplotlib.pyplot as plt
import numpy as nup 
import pylab

import Data

def verifier_parcelles(inData):
    nombreErreurs = 0
    for culture in inData.cultures():
        for parcelle in culture.parcelles():
            if parcelle.irriguee() != culture.irriguee():
                print(parcelle.nom(), ": la culture", culture.nom(), "n'est pas adaptée" )
                nombreErreurs += 1 


    if nombreErreurs == 0:
        print('Les cultures sont adaptées aux parcelles')
    else:
        print(nombreErreurs, "problème(s) ont été rencontré(s)")


def dessiner_planning(inExploistation):
    dessiner_planing_culture(inExploistation)
    dessiner_planing_mois(inExploistation)

def dessiner_planing_mois(inExploitation):
    """
    ROLE dessiner le planing par mois
    """
    dictHaParMois = {}
    for mois in Data.LST_MOIS:
        dictHaParMois[mois] = 0    
    
    inExploitation.recuperer_infos_mois(dictHaParMois)    
    
    lstHaParMois = []
    for mois in Data.LST_MOIS:
        lstHaParMois.append(dictHaParMois[mois])        
    
    # tracer le diagramme en bâton

    fig = plt.figure()

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    width = 0.05
    BarName = ['a','b','c','d','e','f','g','h','i','j']

    plt.bar(x, lstHaParMois, width, color= 'r')
    #plt.scatter([i+width/2.0 for i in x],lstHaParMois,color='k',s=40)

    plt.xlim(0,13)
    plt.ylim(0,max(lstHaParMois) + 1)
    plt.grid()

    plt.ylabel('Ha à récolter')
    plt.title('Planning de récolte par mois')

    pylab.xticks(x, Data.LST_MOIS, rotation=40)

    #plt.savefig('SimpleBar.png')
    plt.show()


def dessiner_planing_culture(inExploitation):
    """
    ROLE dessiner le planing par culture
    """
    lstNomCultures = inExploitation.cultures()
    dictHaParCulture = {}
    
    for culture in lstNomCultures:
        dictHaParCulture[culture] = 0
    
    inExploitation.recuperer_infos_culture(dictHaParCulture)

    lstHaParCulture = []

    for culture in lstNomCultures:
        lstHaParCulture.append(dictHaParCulture[culture])
        #    lstCultures.append(dictHaParCulture.keys())
    
    
    # tracer le diagramme en bâton

    fig = plt.figure()

    x = []
    i = 1
    for culture in lstNomCultures:
        x.append(i)
        i = i + 1
    
    width = 0.05
    BarName = ['a','b','c','d','e','f','g','h','i','j']

    plt.bar(x, lstHaParCulture, width, color= 'r')
    #plt.scatter([i+width/2.0 for i in x],lstHaParCulture,color='k',s=40)

    plt.xlim(0,len(lstNomCultures) + 1)
    plt.ylim(0,max(lstHaParCulture) + 1)
    plt.grid()

    plt.ylabel('Ha à récolter')
    plt.title('Planning de récolte par culture')

    pylab.xticks(x, Data.LST_MOIS, rotation=40)

    #plt.savefig('SimpleBar.png')
    plt.show()  

# programme principal

data = Data.Data()
data.lire_fichier_cultures('Cultures.csv') 
data.lire_fichier_parcelles('Parcelles.csv')

# vérification automatique des cultures

verifier_parcelles(data)

# visualisation du planning d'un exploitant
# pour tester le programme possibilité d'utiliser 'Michel'

nom = input(" Rentrez le nom de l'exploitant : ")
nom = str(nom)

exploitation = data.recherche_exploitation(nom)
dessiner_planning(exploitation)
 

# ci dessous test unitaire utilisé pendant le devellopement de l'outil
"""
if  __name__ == "__main__":
    print(sys.argv)
    data = Data.Data()
    data.lire_fichier_cultures('Cultures.csv') 
    data.lire_fichier_parcelles('Parcelles.csv')
    
    if sys.argv[1] == 'check':
        verifier_parcelles(data)
    elif sys.argv[1] == 'plan':
        nom = sys.argv[2]
        exploitation = data.recherche_exploitation(nom)
        dessiner_planing_mois(exploitation)
    else:
        print(options.command, ': commande inconnue')
"""

