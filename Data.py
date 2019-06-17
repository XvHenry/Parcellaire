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
        pass

    
    def culture_par_nom(inSelf, inNom):
        return inSelf._dictCultures[inNom]


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


    def read_exploitations(ioSelf, inNomFichierCsv): # return boolean
        """
        ROLE : lit le fichier CSV de nom spécifié dans Data ioSelf
        ENTREE inNomFichierCsv : str # nom du fichier CSV à traiter
        SORTIE False en cas d'erreur de l'opération, True sinon
        MAJ    ioSelf : Data
        """
        #1 Lecture du fichier dans la variable lstCultures
        fichCultures = open(inNomFichierCsv,'r')
        lstCultures = fichCultures.readlines() # ou lstPoints = list(fichPointsRando)
        fichCultures.close()
        #2 Ajout des différents points dans la trace ioSelf
        #  en sautant la ligne d'en-tête (avec le nom de colonnes)
        for LigneCulture in lstCultures[1:] : # traiter une ligne de culture
            lstDatas = LigneCulture.rstrip().split(";") # isoler chaque élément séparé par point-virgule
            # Culture;Nom;Irriguation;Récolte;Semence;Durée
            cultureType, nom, irriguation, recolte, semence, duree = lstDatas
            irriguation = True if irriguation == 'Oui' else False # conversion de str en booléen 
            #créer une culture en fonction de cultureType
            if cultureType == 'Annuelle':
                culture = Annuelle(nom, irriguation, recolte, semence)
            elif cultureType == 'Perenne':
                culture = Perenne(nom, irriguation, recolte, duree)
            else:
                print(cultureType, ': Culture ignorée')
                continue 

            ioSelf._lstCultures.append(culture)

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
        outSelf._width = inWidth.
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
        return areaHa.


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
    def __init__(self):
        self.irriguated = False
        self.orientation = Orientation.NORTH
        
        self.exploitation = None
        self.culture = None
        self.patch = []
        

class Cereales(Annuelle):
    pass


class Oleagineux(Annuelle):
    pass


if __name__ == '__main__': # Test unitaire du fichier Data.py 
    data = Data()
    data.read_cultures('Cultures.csv') 
