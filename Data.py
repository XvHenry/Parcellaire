"""
ROLE : module mettant à disposition les classes : Nommable, Data, Exploitation, Zone, Culture, Parcelle, Annuelle et Perenne  
@authors : Vallée Guillaume, Henry Xavier

"""


# constante (liste) contenant les mois de l'année
LST_MOIS = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']


class Nommable:
    """
    ROLE : gérer le nom d'un objet
    """
    def __init__(outSelf, inNom):
        """
        PROCEDURE initialisant le nom de l'objet
        ENTREE inNom : str # nom à affecter à l'objet
        """
        outSelf._nom = inNom # initialisation de l'attribut _nom
        

    def nom(inSelf):
        """
        FONCTION retournant le nom de l'objet
        ENTREE inSelf : Nommable # l'objet dont on veut avoir le nom
        """
        return inSelf._nom


class Data:
    """
    ROLE : gestion des données provenant des fichers parcelles et cultures via des dictionnaires.
         cela permet de pouvoir accéder plus facilement aux informations qu'avec des listes
    """
    def __init__(outSelf):        
        """
        PROCEDURE initialisant l'objet Data outSelf
        ENTREE N/A
        SORTIE outSelf : Data
        """
        outSelf._dictCultures = {} # initialisation de l'atribut _dictCultures
        outSelf._dictParcellesNom = {} # initialisation de l'atribut _dictParcellesNom
        outSelf._dictExploitations = {} # initialisation de l'atribut _dicExploitation

    def ajouter_culture(ioSelf, inCulture):
        """
        PROCEDURE ajoute une Culture à l'attribut _dictCultures
        ENREE inCulture : Culture # la culture à ajouter
        MAJ ioSelf : _dictCultures 
        """
        ioSelf._dictCultures[inCulture.nom()] = inCulture 

    
    def culture_par_nom(inSelf, inNom):
        """
        FONCTION retournant une culture grâce à son nom
        ENTREE inNom : str # Nom de l'objet Culture que l'on souhaire récupérer
        SORTIE inSelf : Culture # Culture associée au nom entré
        """
        return inSelf._dictCultures[inNom]


    def cultures(inSelf):
        """
        FONCTION retournant la liste des cultures
        ENTREE inSelf : Data # l'objet Data qui contient la liste voulue
        SORTIE inSelf : list # liste des objets Culture que contient l'objet Data
        """
        return inSelf._dictCultures.values()


    def ajouter_parcelle(ioSelf, inParcelle):
        """
        PROCEDURE ajoutant une Parcelle à l'attribut _dictParcelles
        """
        ioSelf._dictParcellesNom[inParcelle.nom()] = inParcelle 

    
    def parcelle_par_nom(inSelf, inNom):
        """
        FONCTION retournant une culture grâce à son nom
        """
        return inSelf._dictParcellesNom[inNom]


    def recherche_exploitation(inSelf, inNom):
        """
        FONCTION retournant un objet exploitation grâce à son nom
        """
        # get permet également d'accéder à la valeur associée à la clé
        return inSelf._dictExploitations.get(inNom) 


    def creer_exploitation(ioSelf, inNom):
        """
        PROCEDURE créant un objet exploitation et le retourne directement. 
        ENTREE ioSelf : Data # objet Data qui va stocker l'objet Exploitation crée
                inNom : str # Nom du nouvel objet Exploitation
        MAJ ioSelf._dictExploitation  
        """
        exploitation = Exploitation(inNom) # création d'un objet de type Exploitation
        ioSelf._dictExploitations[inNom] = exploitation # justifie l'appellation PROCEDURE
        return exploitation # aurait pu justifier l'appellation FONCTION


    def lire_fichier_cultures(ioSelf, inNomFichierCsv ):
        """
        PROCEDURE lisant le fichier CSV de nom spécifié dans Data ioSelf
        ENTREE inNomFichierCsv : str # nom du fichier CSV à traiter
        MAJ    ioSelf : Data
        """
        #1 Lecture du fichier dans la variable fichCultures
        fichCultures = open(inNomFichierCsv,'r')
        lstCultures = fichCultures.readlines() # ou lstCultures = list(fichCultures)
        fichCultures.close()
        #2 Ajout des différentes cultures dans le data ioSelf
        #  en sautant la ligne d'en-tête (avec le nom de colonnes)
        if len(lstCultures[0].split(";")) != 6:
            print(inNomFichierCsv, ': Le fichier doit avoir 6 colonnes')
            return False # si le fichier n'est pas adapté, echec de la procédure

        for LigneCulture in lstCultures[1:] : # traiter une ligne de culture
            lstDatas = LigneCulture.rstrip().split(";") # isoler chaque élément séparé par point-virgule
            # Culture;Nom;Irriguation;Récolte;Semence;Durée
            cultureType, nom, irriguation, recolte, semence, duree = lstDatas
            irriguation = irriguation == 'Oui' # conversion de str en booléen 
            # créer une culture en fonction de cultureType
            # permet d'avoir deux types d'objets qui seront traités plus tard différemment
            if cultureType == 'Annuelle':
                culture = Annuelle(nom, irriguation, recolte, semence)
            elif cultureType == 'Perenne':
                culture = Perenne(nom, irriguation, recolte, duree)
            else:
                print(cultureType, ': Culture ignorée')
                continue 

            ioSelf.ajouter_culture(culture)

        return True # succès de la procédure


    def lire_fichier_parcelles(ioSelf, inNomFichierCsv): # return boolean
        """
        PROCEDURE lisant le fichier CSV de nom spécifié dans Data ioSelf
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
        if len(lstParcelles[0].split(";")) != 6:
            print(inNomFichierCsv, ': Le fichier doit avoir 6 colonnes')
            return False

        for LigneParcelle in lstParcelles[1:] : # traiter une ligne de parcelle
            lstDatas = LigneParcelle.rstrip().split(";") # isoler chaque élément séparé par point-virgule
            # Nom;Proprietaire;Largeur;Hauteur;Irriguee;Culture en cours
            name, proprietaire, strWidth, strHeight, strIrriguee, strActualCrop = lstDatas
            
            # conversion des données
            irriguee = strIrriguee == 'Oui' 
            actualCrop = ioSelf.culture_par_nom(strActualCrop) # Recherche de l'objet culture de même nom
            width = float(strWidth)
            height = float(strHeight)
            # création d'un objet Parcelle
            parcelle = Parcelle(name, width, height, center, irriguee, orientation, proprietaire, actualCrop)
            ioSelf.ajouter_parcelle(parcelle)

            # ajout de la parcelle à l'eploitation correspondante si celle ci existe déjà
            # création de l'exploitation puis ajout sinon
            exploitation = ioSelf.recherche_exploitation(proprietaire)
            if exploitation is None:
                exploitation = ioSelf.creer_exploitation(proprietaire) 
            exploitation.ajouter_parcelle(parcelle)


        return True


class Exploitation(Nommable):
    """
    ROLE : définit un ensemble de parcelles appartenant toutes à un même propriétaire.
    """    
    def __init__(outSelf, inProprietaire):
        """
        PROCEDURE créant une exploitation vide ne contenant aucune parcelle
        ENTREE inProprietaire : str # Nom de l'exploitation
        SORTIE outSelf : exploitation
        """
        super().__init__(inProprietaire) # initialise les attributs hérités de la classe supérieure, ici Nommable
        outSelf._lstParcelles = [] # initialise l'attribut _lsttParcelle


    def ajouter_parcelle(ioSelf, inParcelle):
        """
        PROCEDURE ajoute une Culture à l'attribut _lstParcelles
        ENREE inCulture : Culture # la culture à ajouter
        MAJ ioSelf : _lstParcelles 
        """
        ioSelf._lstParcelles.append(inParcelle)        

    
    def cultures(inSelf):
        """
        FONCTION retournant la liste des cultures sur l'exploitation
        """
        # la liste des cultures n'est pas un attribut il faut donc la créer d'abord
        # on aurait pu définir un attribut _lstCulture et créer une procédure pour remplir la liste
        lstCulture = []
        for parcelle in inSelf._lstParcelles:
            culture = parcelle.culture()
            existe = False 

            # plusieurs parcelles peuvent avoir la même culture il faut vérifier que la culture traitée n'est pas déjà présente
            for cultureClasse in lstCulture: 
                if culture == cultureClasse:
                    existe = True
            
            if existe == False:
                lstCulture.append(culture.nom())

        return lstCulture


    
    def recuperer_infos_culture(inSelf, ioDictHaParCulture):
        """
        PROCEDURE remplissant un dictionaire avec les hectares a récolter respectivement avec une clé culture 
        ENTREE inSelf : Exploitation
                ioDictHaParCulture : dict # dictionnaire que l'on souhaite remplir
        """

        for parcelle in inSelf._lstParcelles:
            culture = parcelle.culture()
            nomCulture = culture.nom()
            area = parcelle.area_ha()
            # sommer les surfaces dans le dictionnaire
            ioDictHaParCulture[nomCulture] = ioDictHaParCulture[nomCulture] + area


    def recuperer_infos_mois(inSelf, ioDictHaParMois):
        """
        ROLE remplit un dictionaire avec les hectares a récolter respectivement avec une clé mois
        ENTREE inSelf : Exploitation
                ioDictHaParMois : dict # dictionnaire que l'on souhaite remplir
        """

        for parcelle in inSelf._lstParcelles:
            culture = parcelle.culture()
            area = parcelle.area_ha()
            # sommer les surfaces dans le dictionnaire
            recolte = culture.recolte()
            ioDictHaParMois[recolte] = ioDictHaParMois[recolte] + area 


class Culture(Nommable):
    """
    ROLE : gérer les informations concernant un type de culture particulier
    """
    def __init__(outSelf, inNom, inIrriguee, inRecolte):
        """
        PROCEDURE initialisant l'objet Culture
        ENTREE inNom : str # le nom de la culture
                inIrriguee : bool # True si la culture à besoin d'eau
                inRecolte : str # mois de récolte
        """
        super().__init__(inNom)
        outSelf._irriguee = inIrriguee # initialise l'attribut _irriguee
        outSelf._recolte = inRecolte # initialise l'attribut _recolte
        # mise à jour de l'association bidirectionnelle culture-parcelle
        outSelf._lstParcelles = [] # initialise l'attribut _lstParcelles


    def irriguee(inSelf):
        """
        FONCTION retournant le besoin en irriguation de la culture
        """
        return inSelf._irriguee


    def parcelles(inSelf):
        """
        FONCTION retournant la liste des parcelles associées
        """
        return inSelf._lstParcelles


    def ajouter_parcelle(ioSelf, inParcelle):
        """
        PROCEDURE de mise à jour de l'association Culture-Parcelle lors de la lecture des fichiers
        ENTREE ioSelf : Culture
                inParcelle : Parcelle
        MAJ ioSelf : Culture
        """
        ioSelf._lstParcelles.append(inParcelle)


    def recolte(inSelf):
        """
        FONCTION retourne le mois de récolte de la culture
        """
        return inSelf._recolte


class Zone(Nommable):
    """
    ROLE gère les zones géographiques rectangles, calcule l'aire et le périmètre
    """
    def __init__(outSelf, inNom, inLongueur, inLargeur):
        """
        ROLE initialise l'objet Zone outself
        ENTREE  inLongueur : float # longueur de la zone en mètre
                inHeigth : float #hauteur de la parcelle en mètre
        MAJ ioself : Zone
        """
        super().__init__(inNom)
        outSelf._longueur = inLongueur # initialise l'attribut _longueur
        outSelf._largeur = inLargeur # initialise l'attribut _largeur
        
        
    def area_ha(inSelf):
        """
        ROLE renvoie l'aire de la zone en ha
        ENTREE inSelf : Zone
        """    
        L = inSelf._longueur
        l = inSelf._largeur
        areaMeter = L*l
        areaHa = areaMeter*0.001 # conversion en mètres
        return areaHa


class Perenne(Culture):
    """
    ROLE gérer les informations spécifiques à différentes caractéristiques d'objets Culture : le caractère perrin 
    NOTA le nouvel attibut ne sera pas utilisé, nous ne attarderons pas sur cette classe
    """
    def __init__(outSelf, inName, inIrriguated, inRecolte, inDuree):
        super().__init__(inName, inIrriguated, inRecolte)
        outSelf._duree = inDuree
        

class Annuelle(Culture):
    """
    ROLE : gérer les informations spécifiques à différentes caractéristiques d'objets Culture : le caractère annuel 
    NOTA le nouvel attibut ne sera pas utilisé, nous ne attarderons pas sur cette classe
    """
    def __init__(outSelf, inName, inIrriguated, inRecolte, inSemence):
        super().__init__(inName, inIrriguated, inRecolte)
        outSelf._semence = inSemence      


class Parcelle(Zone):
    """
    ROLE : gérer les informations spécifiques à une parcelle
    NOTA : la classe Zone est supperflue ici mais nous souhaitions à la base faire une classe Region qui en aurait aussi hérité
    """
    def __init__(outSelf, inName, inLongueur, inLargeur, inIrriguee, inProp, ioCultureActuelle):
        """
        ROLE initialise l'objet Zone outself
        ENTREE  inIrriguee : bool # la parcelle à accès à l'eau
                inProp : str # nom du propriétaire
                ioCultureActuelle : Culture #
        MAJ ioself : Zone
        """
        super().__init__(inName, inLongueur, inLargeur,)
        outSelf._irriguee = inIrriguee # initialisation de l'attribut _irriguee
        outSelf._prop = inProp # initialisation de l'attribut _prop
        # mise à jour de l'association Culture-Parcelle (bidirectionnelle)
        outSelf._actualCrop = ioCultureActuelle 
        ioCultureActuelle.ajouter_parcelle(outSelf)


    def prop(inSelf):
        """
        FONCTION retourne le nom du propriétaire
        """
        return inSelf._prop


    def recolte(inSelf):
        """
        FONCTION retourne le mois de récolte de la parcelle
        """
        return inSelf._actualCrop.recolte()

 
    def culture(inSelf):
        """
        FONCTION retourne la culture de la parcelle
        """
        return inSelf._actualCrop


if __name__ == '__main__': # Test unitaire du fichier Data.py 
    data = Data()
    data.lire_fichier_cultures('Cultures.csv') 
    data.lire_fichier_parcelles('Parcelles.csv')