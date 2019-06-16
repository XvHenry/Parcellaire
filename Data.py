from datetime import datetime

class Orientation:
    NORTH, SOUTH, EAST, WEST = range(4)



class Namable:
    def __init__(self):
        self.name = ""
        
        
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
        outSelf.lstCultures = []
        outSelf.lstExploitations = []
        

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
    def __init__(self):
        self.irriguated = False
        self.récolte = datetime()
        
        self.parcelle = []
        self.data = None
        

class Zone(Namable):
    def __init__(self):
        self.width = 0.
        self.height = 0.
        self.center = None
        
        
    def area(self):
        return 0.


    def perimeter(self):
        return 0.


class Region(Zone):
    pass


class Perenne(Culture):
    def __init__(self):
        self.durée = 0
        

class Annuelle(Culture):
    def __init__(self):
        self.semence = datetime()      


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
