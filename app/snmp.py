# importer library
import json


# nom des fichier json
f_equipements = "equipements.json"
f_oid_high_level = "OID_high_level.json"
f_oid_low_level = "OID_low_level.json"




# fonction qui prendre en parametre le nom de fichier json qui nous retourne le contenu de fichier 
def open_json_file(nom_de_fichier_json):
    with open(nom_de_fichier_json) as f:
        data = json.load(f)

    return data





# chargement de contenu du fichier json
ficheir_equipements = open_json_file(f_equipements)
OID_low_level = open_json_file(f_oid_low_level)


# Tableau pour stocker le resultat de SNMP
res = []



# association d'un equipement avec une module de OID

length_equipements = len(ficheir_equipements['equipement'])


equipements = ficheir_equipements['equipement']



for index in range(0, length_equipements):

    constructeur = equipements[index]['constructeur']
    type_de_material

    print(equipements[index])





"""
pour ajouter un nouveau material il fault utilise le formati suivant:
my_data['Mikrotik']['nouveau_material_name'] = new_data

si le categorie de material existe déja utilse:
my_data['Mikrotik']['switch'].append(new_data)

"""


