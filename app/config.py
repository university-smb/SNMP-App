
# importer library
import json
import time
import calendar
import logging


from snmp import Snmp_server




# Logging

# Gets or creates a logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.DEBUG)

# define file handler and set formatter
file_handler = logging.FileHandler('log/std.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)







# nom des fichier json
f_equipements = "BDD/equipements.json"
f_oid_high_level = "OID/OID_high_level.json"
f_oid_low_level = "OID/OID_low_level.json"



# fonction qui prend comme parametre le nom de fichier json qui nous retourne le contenu de fichier 
def open_json_file(nom_de_fichier_json):
    with open(nom_de_fichier_json) as f:
        data = json.load(f)

    return data



# chargement de contenu du fichier json
ficheir_equipements = open_json_file(f_equipements)
OID_low_level = open_json_file(f_oid_low_level)
OID_high_level = open_json_file(f_oid_high_level)




# Tableau pour stocker le resultat de SNMP
res = []



# association d'un equipement avec une module de OID

length_equipements = len(ficheir_equipements['equipement'])


equipements = ficheir_equipements['equipement']


server = Snmp_server()
current_GMT = time.gmtime()

time_stamp = calendar.timegm(current_GMT)






for index in range(0, length_equipements):

    constructeur = equipements[index]['constructeur']
    material = equipements[index]['type_de_material']
    level = equipements[index]['level']

    #print(equipements[index])
    #print(equipements[index]['IP'])

    
    
    oids = OID_high_level[constructeur][material]
    oid_list = list(oids.values())

    oid_key_list = list(oids.keys())


    result = server.get(equipements[index]['IP'], oid_list)

    list_result = list(result)

    

    data = {}
    for i in range(0, len(list_result)):
        data[oid_key_list[i]] = result[list_result[i]]


    print(data)



    #print(server.get(equipements[index]['IP'],["1.3.6.1.2.1.31.1.1.1.10.1"]))
    #result = server.get(equipements[index]['IP'],["1.3.6.1.2.1.2.2.1.16.1"])
    #logger.info(f'OID result is:{result.get("1.3.6.1.2.1.2.2.1.16.1")}')



