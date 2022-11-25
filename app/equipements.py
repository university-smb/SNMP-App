from high_level_OID import HighLevelOID



# class d'équipement pour CRUD l'équipement.
class Equipements:
    
    # Ajouter un "level" de supervision à cette class 
    level = ""

    # parametre d'initalisation de class
    def __init__(self, constructeur, type_de_material, IP, DNS, description, level):
        self.constructeur = constructeur
        self.type_de_material = type_de_material
        self.IP = IP
        self.DNS = DNS
        self.description = description
        self.level = level
        


    def get_oids(self):
        # Afficher les oid associer à une equipement
        pass


