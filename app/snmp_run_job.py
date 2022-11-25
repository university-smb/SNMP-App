
from models import *
from snmp import Snmp_server
from BDD.connect import *
import time
import json
import calendar





def snmp_job():
    
    # Variable global
    server = Snmp_server()
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)

    equipements = get_equipements()
    length_equipements = len(equipements)


    #for index in range(0, length_equipements):
    for row in equipements:
        # Get ip adresse and look for this ip adresse in oid list
        ipdns = row['ipdns']
        oid_level = row['level']
        equipement_id = row['id']

        
        oids_database = get_oids(oid_level)
        #print(oids_database[0]['id'])

        oids_dict = oids_database[0]['oids']
        oidtojson = json.loads(oids_dict)
        oid_values_list = list(oidtojson.values())
        oid_keys_list = list(oidtojson.keys())


        result = server.get(ipdns, oid_values_list)
        

        list_result = list(result)

        data = {}
        for i in range(0, len(list_result)):
            data[oid_keys_list[i]] = result[list_result[i]]

        
        insert_sql = "INSERT INTO snmp_result (timestamp, equipement_id, data) VALUES (%s, %s, %s)"
        insert_val = (time_stamp, equipement_id, json.dumps(data))

        conn = connection.cursor()
        conn.execute(insert_sql, insert_val)
        connection.commit()
        
        #print(oids_database[0]['id'])
    


"""
while True:
    print("it's running")
    snmp_job()
    time.sleep(3)

"""

