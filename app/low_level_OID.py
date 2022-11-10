

# class d'équipement pour CRUD l'équipement.
class LowLevelOID:


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

        
 
 


   




"""

oid = {"cpu" : "1.3.6.1.4.1.14988.1.1.3.6"}
oid_list = { "cpus" : "1.3.6.1.4.1.14988.1.1.3.6", "ram": "1.3.6.1.2.1.25.2.3.1.5.65536"}


lo = LowLevelOID(oid_list)
print(lo)
lo.add_oid(oid)
print(lo)
lo.del_oid('ram')
print(lo)

#print(lo.oid_existe(list(oid.keys())[0]))
"""






