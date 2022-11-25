"""
import json

from equipements import Equipements



f = open('test.json', "w")


equi = Equipements("Mikrotik","routeur","192.168.140.140", "", "Routeur Mikrotik à surveiller", '1')

f.write(equi)

f.close()
"""
"""
import logging

#Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "logfile.log", filemode = "w", format = '%(asctime)s %(message)s', level = logging.ERROR)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#Testing our Logger
logger.debug("This is just a harmless debug message") 
logger.info("This is just an information for you") 
logger.warning("OOPS!!!Its a Warning") 
logger.error("Have you try to divide a number by zero") 
logger.critical("The Internet is not working....") 
"""





# importer library
import json
import time
import calendar
import logging
import collections


from snmp import Snmp_server

# import functions
from BDD.connect import *



conn = connection.cursor(dictionary=True)
conn.execute("SELECT * FROM snmp_result")

#snmp_result = dict(zip(conn.column_names, conn.fetchall()))

snmp_result = conn.fetchall()
conn.close()

#snmp_result_columns = conn.column_names

oids_list = []


"""
for row in snmp_result:
    #d = (row[0], row[1], row[2], row[3] )
    oids_list.append(d)
    print("%s, %s" % (row["id"], row["data"]))

ll = oids_list[0][3]
print(type(ll))
"""

data = snmp_result[0]['data']

r = json.loads(data)

print(r['cpu'])






"""
# Tableau pour stocker le resultat de SNMP
res = []



# association d'un equipement avec une module de OID

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
        data[oid_key_list[i]] = list_result[0]


    print(data)



    #print(server.get(equipements[index]['IP'],["1.3.6.1.2.1.31.1.1.1.10.1"]))
    #result = server.get(equipements[index]['IP'],["1.3.6.1.2.1.2.2.1.16.1"])
    #logger.info(f'OID result is:{result.get("1.3.6.1.2.1.2.2.1.16.1")}')

"""

