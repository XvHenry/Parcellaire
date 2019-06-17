from datetime import datetime

class Orientation:
    NORTH, SOUTH, EAST, WEST = range(4)



class Nommable:
    def __init__(outSelf, inNom):
        outSelf._nom = inNom
        
        
    def nom(inSelf):
        """
        FONCTION retourne le nom
        """
        return inSelf._nom


class Data:
    """
    Gestion des données provenant des fichers parcelles et cultures
    """
    def __init__(outSelf):        
        """
        ROLE initialise l'objet Data outSelf
        ENTREE N/A
        SORTIE outSelf : Data
        """
        outSelf._dictCultures = {}
        outSelf._dictParcelles = {}
        

    def ajouter_culture(ioSelf, inCulture):
        ioSelf._dictCultures[inCulture.nom()] = inCulture 

    
    def culture_par_nom(inSelf, inNom):
        return inSelf._dictCultures[inNom]


    def ajouter_parcelle(ioSelf, inParcelle):
        ioSelf._dictParcelles[inParcelle.nom()] = inParcelle 

    
    def parcelle_par_nom(inSelf, inNom):
        return inSelf._dictParcelles[inNom]


    def lire_fichier_cultures(ioSelf, inNomFichierCsv ):
        """
        ROLE : lit le fichier CSV de nom spécifié dans Data ioSelf
        ENTREE inNomFichierCsv : str # nom du fichier CSV à traiter
        MAJ    ioSelf : Data
        """
        #1 Lecture du fichier dans la variable lstCultures
        fichCultures = open(inNomFichierCsv,'r')
        lstCultures = fichCultures.readlines() # ou lstCultures = list(ficjCultures)
        fichCultures.close()
        #2 Ajout des différents points dans la trace ioSelf
        #  en sautant la ligne d'en-tête (avec le nom de colonnes)
        if len(lstCultures[0].split(";")) != 6:
            print(inNomFichierCsv, ': Le fichier doit avoir 6 colonnes')
            return False

        for LigneCulture in lstCultures[1:] : # traiter une ligne de culture
            lstDatas = LigneCulture.rstrip().split(";") # isoler chaque élément séparé par point-virgule
            # Culture;Nom;Irriguation;Récolte;Semence;Durée
            cultureType, nom, irriguation, recolte, semence, duree = lstDatas
            irriguation = irriguation == 'Oui' # conversion de str en booléen 
            #créer une culture en fonction de cultureType
            if cultureType == 'Annuelle':
                culture = Annuelle(nom, irriguation, recolte, semence)
            elif cultureType == 'Perenne':
                culture = Perenne(nom, irriguation, recolte, duree)
            else:
                print(cultureType, ': Culture ignorée')
                continue 

            ioSelf.ajouter_culture(culture)

        return True


    def lire_fichier_parcelles(ioSelf, inNomFichierCsv): # return boolean
        """
        ROLE : lit le fichier CSV de nom spécifié dans Data ioSelf
        ENTREE inNomFichierCsv : str # nom du fichier CSV à traiter
        SORTIE False en cas d'erreur de l'opération, True sinon
        MAJ    ioSelf : Data
        """
        #1 Lecture du fichier dans la variable lstParcelles
        fichParcelles = open(inNomFichierCsv,'r')
        lstParcelles = fichParcelles.readlines() # ou lstParcelles = list(fichParcelles)
        fichParcelles.close()
        #2 Ajout des différentes parcelles dans la Data ioself
        #  en sautant la ligne d'en-tête (avec le nom de colonnes)
        if len(lstParcelles[0].split(";")) != 8:
            print(inNomFichierCsv, ': Le fichier doit avoir 8 colonnes')
            return False

        for LigneParcelle in lstParcelles[1:] : # traiter une ligne de parcelle
            lstDatas = LigneParcelle.rstrip().split(";") # isoler chaque élément séparé par point-virgule
            # Nom;Proprietaire;Largeur;Hauteur;Centre;Irriguee;Orientation;Culture en cours
            name, owner, width, height, center, irriguee, orientation, actualCrop = lstDatas
            irriguee = irriguee == 'Oui' # conversion de str en booléen 
            actualCrop = ioSelf.culture_par_nom(actualCrop) # Recherche de l'objet culture de même nom
            parcelle = Parcelle(name, width, height, center, irriguee, orientation, owner, actualCrop)
            ioSelf.ajouter_parcelle(parcelle)

        return True





class Patch(Nommable):
    """
        
        self.parcelle = []
        

class Exploitation(Namable):
    def __init__(outSelf, inIrriguated, inOrientation):
        
        outSelf.parcelle = []
        outSelf.data = None


class Culture(Nommable):
    def __init__(outSelf, inName, inIrriguated, inRecolte):
        super().__init__(inName)
        outSelf._irriguated = inIrriguated
        outSelf._recolte = inRecolte 
        
        outSelf._lstParcelles = []
        

    def ajouter_parcelle(ioSelf, inParcelle):
        """
        ROLE mise à jour de l'association Culture-Parcelle
        """
        ioSelf._lstParcelles.append(inParcelle)
        

class Zone(Nommable):
    """
    ROLE gère les zones géographiques rectangles, calcule l'aire et le périmètre
    """
    def __init__(outSelf, inName, inWidth, inHeight, inCenter):
        """
        ROLE initialise l'objet Zone outself
        ENTREE  inWidth : float # largeur de la zone en mètre
                inHeigth : float #hauteur de la parcelle en mètre
                inCenter : lst #couple contenant les coordonnées du centre
        MAJ ioself : Zone
        """
        super().__init__(inName)
        outSelf._width = inWidth
        outSelf._height = inHeight
        outSelf._center = inCenter
        
        
    def area_ha(inSelf):
        """
        ROLE renvoie l'aire de la zone en ha
        ENTREE inSelf : Zone
        """    
        L = inSelf._width
        l = inSelf._height
        areaMeter = L*l
        areaHa = areaMeter*0.001 # conversion en mètres
        return areaHa


    def perimeter(inSelf):    
        return 0.


class Region(Zone):
    pass


class Perenne(Culture):
    def __init__(outSelf, inName, inIrriguated, inRecolte, inDuree):
        super().__init__(inName, inIrriguated, inRecolte)
        outSelf._duree = inDuree
        

class Annuelle(Culture):
    def __init__(outSelf, inName, inIrriguated, inRecolte, inSemence):
        super().__init__(inName, inIrriguated, inRecolte)
        outSelf._semence = inSemence      


class Fruitier(Perenne):
    pass


class Prairie(Perenne):
    pass
    

class Parcelle(Zone):
    def __init__(outSelf, inName, inWidth, inHeight, inCenter, inIrriguated, inOrientation, inOwner, ioActualCrop):
        super().__init__(inName, inWidth, inHeight, inCenter)
        outSelf._irriguated = inIrriguated
        outSelf._orientation = inOrientation
        outSelf._owner = inOwner
        # mise à jour de l'association Culture-Parcelle (bidirectionnelle)
        outSelf._actualCrop = ioActualCrop
        ioActualCrop.ajouter_parcelle(outSelf)
        pass


class Exploitation(Nommable):
    """
    ROLE définit un ensemble de parcelles appartenant toutes à un même propriétaire.
    """
    def __init__(outSelf, inName, inOwner):
        """
        PROCEDURE créant une exploitation vide ne contenant aucune parcelle
        ENTREE inName : str # Nom de l'exploitation
               inOwner :str # Nom du propriétaire
        SORTIE outSelf : exploitation
        """
        super().__init__(inName) # Nom de l'exploitation
        outSelf._Owner =str(inOwner) # Nom du propriétaire
        outSelf._lstParcelles = list() # Liste des exploitations 

    
    def ajouter_parcelles(ioSelf):
        pass

        
        

class Cereales(Annuelle):
    pass


class Oleagineux(Annuelle):
    pass


if __name__ == '__main__': # Test unitaire du fichier Data.py 
    data = Data()
    data.lire_fichier_cultures('Cultures.csv') 
    data.lire_fichier_parcelles('Parcelles.csv')