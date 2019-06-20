
class Orientation:
    NORTH, SOUTH, EAST, WEST = range(4)


LST_MOIS = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']


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
        outSelf._dictParcellesNom = {}
        #outSelf._dictParcellesProp = {}
        outSelf._dictExploitations = {}
        
    def ajouter_culture(ioSelf, inCulture):
        ioSelf._dictCultures[inCulture.nom()] = inCulture 

    
    def culture_par_nom(inSelf, inNom):
        return inSelf._dictCultures[inNom]


    def cultures(inSelf):
        """
        FONCTION qui retourne la list des cultures
        """
        return inSelf._dictCultures.values()


    def ajouter_parcelle(ioSelf, inParcelle):
        ioSelf._dictParcellesNom[inParcelle.nom()] = inParcelle 
        #ioSelf._dictParcellesProp[inParcelle.prop()] = inParcelle

    
    def parcelle_par_nom(inSelf, inNom):
        return inSelf._dictParcellesNom[inNom]


    def recherche_exploitation(inSelf, inNom):
        return inSelf._dictExploitations.get(inNom)


    def creer_exploitation(ioSelf, inNom):
            exploitation = Exploitation(inNom)
            ioSelf._dictExploitations[inNom] = exploitation
        return exploitation


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
            name, proprietaire, strWidth, strHeight, center, strIrriguee, orientation, strActualCrop = lstDatas
            
            # conversion des données
            irriguee = strIrriguee == 'Oui' 
            actualCrop = ioSelf.culture_par_nom(strActualCrop) # Recherche de l'objet culture de même nom
            width = float(strWidth)
            height = float(strHeight)

            parcelle = Parcelle(name, width, height, center, irriguee, orientation, proprietaire, actualCrop)
            ioSelf.ajouter_parcelle(parcelle)

            exploitation = ioSelf.recherche_exploitation(proprietaire)
            if exploitation is None:
                exploitation = ioSelf.creer_exploitation(proprietaire) 
            exploitation.ajouter_parcelle(parcelle)


        return True


class Exploitation(Nommable):
    """
    ROLE définit un ensemble de parcelles appartenant toutes à un même propriétaire.
    """    
    def __init__(outSelf, inProprietaire):
        """
        PROCEDURE créant une exploitation vide ne contenant aucune parcelle
        ENTREE inProprietaire : str # Nom de l'exploitation
        SORTIE outSelf : exploitation
        """
        super().__init__(inProprietaire)
        outSelf._lstParcelles = []


    def ajouter_parcelle(ioSelf, inParcelle):
        ioSelf._lstParcelles.append(inParcelle)        

    
    def cultures(inSelf):
        """
        FONCTION retournant la liste des cultures sur l'exploitation
        """
        lstCulture = []
        for parcelle in inSelf._lstParcelles:
            culture = parcelle.culture()
            existe = False


            for cultureClasse in lstCulture:
                if culture == cultureClasse:
                    existe = True
            
            if existe == False:
                NOM = culture.nom()
                lstCulture.append(culture.nom())


        return lstCulture


    
    def recupérer_infos_culture(inSelf, ioDictHaParCulture):
        """
        ROLE remplit un dictionaire avec les hectares a récolter respectivement avec une clé culture 
        """

        for parcelle in inSelf._lstParcelles:
            culture = parcelle.culture()
            nomCulture = culture.nom()
            area = parcelle.area_ha()
            # sommer les surfaces dans le dictionnaire
            ioDictHaParCulture[nomCulture] = ioDictHaParCulture[nomCulture] + area


    def recupérer_infos_mois(inSelf, ioDictHaParMois):
    """
        ROLE remplit un dictionaire avec les hectares a récolter respectivement avec une clé mois
        """

        for parcelle in inSelf._lstParcelles:
            culture = parcelle.culture()
            area = parcelle.area_ha()
            # sommer les surfaces dans les deux dictionnaires
            recolte = culture.recolte()
            ioDictHaParMois[recolte] = ioDictHaParMois[recolte] + area
        
        


        
        

        




class Culture(Nommable):
    def __init__(outSelf, inName, inIrriguated, inRecolte):
        super().__init__(inName)
        outSelf._irriguated = inIrriguated
        outSelf._recolte = inRecolte 
        
        outSelf._lstParcelles = []
        
    def irriguee(inSelf):
        """
        FONCTION retourne le besoin en irriguation de la culture
        """
        return inSelf._irriguated

    def parcelles(inSelf):
        """
        FONCTION retourne la liste des parcelles associées
        """
        return inSelf._lstParcelles
    
    def ajouter_parcelle(ioSelf, inParcelle):
        """
        ROLE mise à jour de l'association Culture-Parcelle
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


class Perenne(Culture):
    def __init__(outSelf, inName, inIrriguated, inRecolte, inDuree):
        super().__init__(inName, inIrriguated, inRecolte)
        outSelf._duree = inDuree
        

class Annuelle(Culture):
    def __init__(outSelf, inName, inIrriguated, inRecolte, inSemence):
        super().__init__(inName, inIrriguated, inRecolte)
        outSelf._semence = inSemence      


class Parcelle(Zone):
    def __init__(outSelf, inName, inWidth, inHeight, inCenter, inIrriguated, inOrientation, inProp, ioActualCrop):
        super().__init__(inName, inWidth, inHeight, inCenter)
        outSelf._irriguated = inIrriguated
        outSelf._orientation = inOrientation
        outSelf._prop = inProp
        # mise à jour de l'association Culture-Parcelle (bidirectionnelle)
        outSelf._actualCrop = ioActualCrop
        ioActualCrop.ajouter_parcelle(outSelf)


    def irriguee(inSelf):
        """
        FONCTION retourne l'accès à l'eau pour la parcelle
        """
    
    
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

class Cereales(Annuelle):
    pass


class Oleagineux(Annuelle):
    pass


if __name__ == '__main__': # Test unitaire du fichier Data.py 
    data = Data()
    data.lire_fichier_cultures('Cultures.csv') 
    data.lire_fichier_parcelles('Parcelles.csv')