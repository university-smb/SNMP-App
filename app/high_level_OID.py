


# class d'équipement pour CRUD l'équipement.
class HighLevelOID:


    # parametre d'initalisation de class
    def __init__(self, oid_list):
        self.oid_list = oid_list


    # Fonction pour afficher notre list des OIDs
    def __str__(self):
        return f'{self.oid_list}'

    
    # Fonction pour ajouter un nouveau oid 
    # nouveau OID doit etre sur le forme d'un dictionaire
    def add_oid(self, oid):

        new_oid_list_key = list(oid.keys())[0]
        new_oid_list_value = list(oid.values())[0]

        if self.oid_existe(new_oid_list_key):
            print("oid already existe")
        else:
            self.oid_list[new_oid_list_key] = new_oid_list_value



    # Fonction pour supprimer un OID 
    # Fonction prendre le clé "KEY" de OID pour supprimer
    def del_oid(self, oid_key):

        if self.oid_existe(oid_key):
            del self.oid_list[oid_key]



    # Checker si l'OID existe déja
    def oid_existe(self, oid):

        if oid in self.oid_list.keys():
            return True
        else:
            return False

        
 
