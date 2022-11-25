
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
    #type_de_material

    

    #print(equipements[index])
    #print(equipements[index]['IP'])

    
    if (level == '1'):
        oids = OID_high_level[constructeur][material]
        oid_list = list(oids.values())

        oid_key_list = list(oids.keys())


        result = server.get(equipements[index]['IP'], oid_list)


        print(result)


    

    #print(server.get(equipements[index]['IP'],["1.3.6.1.2.1.31.1.1.1.10.1"]))
    #result = server.get(equipements[index]['IP'],["1.3.6.1.2.1.2.2.1.16.1"])
    #logger.info(f'OID result is:{result.get("1.3.6.1.2.1.2.2.1.16.1")}')







"""
    log_data = {
        "message": "les données snmp est sauvegardé avec success!",
        "log": {
            "constructeur": equipements[index]['constructeur'],
            "material": equipements[index]['type_de_material'],
            "IP": equipements[index]['IP'],
            "OID": "NONE",
        },
        "user": {
            "name": "default",
            "id": 1
        },
        "event": {
            "success": True
        }
    }
"""









"""
pour ajouter un nouveau material il fault utilise le formati suivant:
my_data['Mikrotik']['nouveau_material_name'] = new_data

si le categorie de material existe déja utilse:
my_data['Mikrotik']['switch'].append(new_data)

"""







"""
from pysnmp import hlapi
import argparse

def construct_object_types(list_of_oids):
    object_types = []
    for oid in list_of_oids:
        object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
    return object_types

def construct_value_pairs(list_of_pairs):
    pairs = []
    for key, value in list_of_pairs.items():
        pairs.append(hlapi.ObjectType(hlapi.ObjectIdentity(key), value))
    return pairs

def cast(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            try:
                return str(value)
            except (ValueError, TypeError):
                pass
    return value

def fetch(handler, count):
    result = []
    for i in range(count):
        try:
            error_indication, error_status, error_index, var_binds = next(handler)
            if not error_indication and not error_status:
                items = {}
                for var_bind in var_binds:
                    items[str(var_bind[0])] = cast(var_bind[1])
                result.append(items)
            else:
                raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
        except StopIteration:
            break
    return result

def get(target, oids, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.nextCmd(
        engine,
        hlapi.CommunityData('public'),
        hlapi.UdpTransportTarget((target, port)),
        context,
        *construct_object_types(oids)
    )
    return fetch(handler, 1)[0]

def walk(target, oids, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData(), debug = False):
    output = []
    for (errorIndication,errorStatus,errorIndex,varBinds) in hlapi.nextCmd(
        engine,
        hlapi.CommunityData('public'),
        hlapi.UdpTransportTarget((target, port)),
        context,
        *construct_object_types(oids),
        lexicographicMode = False
    ):

        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            break
        else:
            output.append(varBinds)
            if debug:
                for varBind in varBinds:
                    print(' = '.join([x.prettyPrint() for x in varBind]))
    return output

def get_bulk(target, oids, count, start_from=0, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.bulkCmd(
        engine,
        hlapi.CommunityData('public'),
        hlapi.UdpTransportTarget((target, port)),
        context,
        start_from, count,
        *construct_object_types(oids)
    )
    return fetch(handler, count)

def get_bulk_auto(target, oids, count_oid, start_from=0, port=161,
                  engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    count = get(target, [count_oid], port, engine, context)[count_oid]
    return get_bulk(target, oids, count, start_from, port, engine, context)



def get_args():
    parser = argparse.ArgumentParser(description="Tool to perform SNMP-Walk requests")
    parser.add_argument('--host', required=True, help='SNMP server IP Address', default="127.0.0.1")
    parser.add_argument('--oid', required=False, help='SNMP OID', default="1.3.6.1.2.1.1.5 ")
    args = parser.parse_args()
    return args




print(get("192.168.56.210",["1.3.6.1.2.1.1.1.0","1.3.6.1.2.1.1.6.0"]))

"""