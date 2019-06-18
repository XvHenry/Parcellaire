import sys
import argparse
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


    pass

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

