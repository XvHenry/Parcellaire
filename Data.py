from datetime import datetime

class Orientation:
    NORTH, SOUTH, EAST, WEST = range(4)



class Namable:
    def __init__(outSelf, inName):
        outSelf._name = inName
        
        
class Data:
    """
    Gestion des données provenant des fichers exploitants et culutures
    """
    def __init__(outSelf):        
        """
        ROLE initialise l'objet Data outSelf
        ENTREE N/A
        SORTIE outSelf : Data
        """
        outSelf._lstCultures = []
        outSelf._lstExploitations = []
        

    def read_cultures(ioSelf, inNomFichierCsv ):
        """
        ROLE : lit le fichier CSV de nom spécifié dans Data ioSelf
        ENTREE inNomFichierCsv : str # nom du fichier CSV à traiter
        MAJ    ioSelf : Data
        """
        return False


    def read_exploitations(ioSelf, inNomFichierCsv): # return boolean
        """
        ROLE : lit le fichier CSV de nom spécifié dans Data ioSelf
        ENTREE inNomFichierCsv : str # nom du fichier CSV à traiter
        SORTIE False en cas d'erreur de l'opération, True sinon
        MAJ    ioSelf : Data
        """
        return True


class Patch:
    def __init__(self):
        
        self.parcelle = []
        

class Exploitation(Namable):
    def __init__(self):
        
        self.parcelle = []
        self.data = None


class Culture(Namable):
    def __init__(outSelf, inName, inIrriguated, inRecolte):
        super().__init__(inName)
        outSelf._irriguated = inIrriguated
        outSelf._recolte = inRecolte 
        
        outSelf._lstParcelles = []
        

class Zone(Namable):
    def __init__(self):
        self._width = 0.
        self._height = 0.
        self._center = None
        
        
    def area(self):
        return 0.


    def perimeter(self):
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
