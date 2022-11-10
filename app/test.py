



# class d'équipement pour CRUD l'équipement.
class HighLevelOID:
    

    # parametre d'initalisation de class
    def __init__(self, **kwargs):
        self.kwargs = kwargs

   

    
    # Fonction pour ajouter un nouveau oid 
    # nouveau OID doit etre sur le forme d'un dictionaire
    def add_oid(self, **kwargs):

        new_oid_list_key = list(kwargs.keys())[0]
        new_oid_list_value = list(kwargs.values())[0]

        if self.oid_existe(new_oid_list_key):
            print("oid already existe")
        else:
            self.kwargs[new_oid_list_key] = new_oid_list_value



    # Fonction pour supprimer un OID 
    # Fonction prendre le clé "KEY" de OID pour supprimer
    def del_oid(self, oid_key):

        if self.oid_existe(oid_key):
            del self.kwargs[oid_key]



    # Checker si l'OID existe déja
    def oid_existe(self, oid):

        if oid in self.kwargs.keys():
            return True
        else:
            return False

        
 

oid = {"cpu" : "1.3.6.1.4.1.14988.1.1.3.6"}
oid_list = { "cpus" : "1.3.6.1.4.1.14988.1.1.3.6", "ram": "1.3.6.1.2.1.25.2.3.1.5.65536"}



lo = HighLevelOID(cpus="1.3.6.1.4.1.14988.1.1.3.6", ram="1.3.6.1.2.1.25.2.3.1.5.65536")

print(lo.__dict__)


lo.add_oid(cpu="1.3.6.1.4.1.14988.1.1.3.6")
print(lo.__dict__)
