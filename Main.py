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


def dessiner_planning():
    pass

def dessiner_planing_mois(inExploitation):
    """
    ROLE dessiner le planing par mois
    """
    dictHaParMois = {}
    lstHaParMois = []
    for mois in Data.LST_MOIS:
        dictHaParMois[mois] = 0
        lstHaParMois.append(0)
    
    i = 0
    
    inExploitation.recupérer_infos_mois(dictHaParMois)    
    
    for mois in Data.LST_MOIS:
        lstHaParMois[i] = dictHaParMois[mois]
        i = i + 1
    
    # tracer le diagramme en bâton

    fig = plt.figure()

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    width = 0.05
    BarName = ['a','b','c','d','e','f','g','h','i','j']

    plt.bar(x, lstHaParMois, width, color= 'r')
    plt.scatter([i+width/2.0 for i in x],lstHaParMois,color='k',s=40)

    plt.xlim(0,13)
    plt.ylim(0,max(lstHaParMois) + 1)
    plt.grid()

    plt.ylabel('Ha à récolter')
    plt.title('Planning de récolte')

    pylab.xticks(x, Data.LST_MOIS, rotation=40)

    #plt.savefig('SimpleBar.png')
    plt.show()

if  __name__ == "__main__":
    print(sys.argv)
    data = Data.Data()
    data.lire_fichier_cultures('Cultures.csv') 
    data.lire_fichier_parcelles('Parcelles.csv')
    
    if sys.argv[1] == 'check':
        verifier_parcelles(data)
    elif sys.argv[1] == 'plan':
        nom = sys.argv[2]
        exploitation = data.rechercher_exploitation(nom)
        dessiner_planing_mois(exploitation)
    else:
        print(options.command, ': commande inconnue')

