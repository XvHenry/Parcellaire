import sys
import argparse
import Data

def verifier_parcelles(inData):
    pass

if  __name__ == "__main__":
    print(sys.argv)
    data = Data.Data()
    data.read_cultures('Cultures.csv') 
    
    parser = argparse.ArgumentParser(description = 'Projet parcellaire')
    parser.add_argument('-c', '--command', metavar = '<cmd>', help = 'commande', required = True)
    parser.add_argument('-p', '--parametre', metavar = '<param>', help = 'paramètre de la commande', required = False)
    options = parser.parse_args()
    if options.command == 'check':
        verifier_parcelles(data)
    else:
        print(options.command, ': commande inconnue')
