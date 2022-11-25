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


    def add_level(self, level):
        self.level = level





        

    def start_monitoring(self):
        # start monitoring using snmp
        pass
    #def demarer_surveillance(self):
        ###

    #def arreter_surveillance(self):
        #
    




#equipement = Equipements("Mikrotik","routeur","192.168.56.210", "", "Routeur Mikrotik à surveiller")






# creating list       
#list = [] 

# appending instances to list 
#list.append(Equipements("Mikrotik","routeur","192.168.56.210", "", "Routeur Mikrotik à surveiller"))
#list.append(Equipements("Mikrotik2","routeur","192.168.56.210", "", "Routeur Mikrotik à surveiller"))



"""
10112022
lo = LowLevelOID("1.3.6.1.4.1.14988.1.1.3.6", "1.3.6.1.2.1.25.2.3.1.5.65536")

eq = Equipements("Mikrotik","routeur","192.168.56.210", "", "Routeur Mikrotik à surveiller")

eq.add_level(lo)

print(eq.level.cpu)
"""

#oid = HighLevelOID("1.3.6.1.4.1.14988.1.1.3.6", "1.3.6.1.2.1.25.2.3.1.5.65536", "1.3.6.1.2.1.31.1.1.1.6.1", "1.3.6.1.2.1.31.1.1.1.10.1")


"""
for obj in list:
    print( obj.constructeur, sep =' ')

"""


"""
dic = {}

equipement = Equipements(dic)
equipement.add_device("Mikrotik","routeur","192.168.56.210", "", "Routeur Mikrotik à surveiller")

equipement.add_device("Mikrotik2","routeur","192.168.56.210", "", "Routeur Mikrotik à surveiller")

print(equipement)

"""


"""
f_equipements = "equipements.json"
with open(f_equipements) as f:
    data = json.load(f)

print(data)
"""

