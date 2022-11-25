from flask import Flask, render_template, request, session, redirect, send_from_directory, Markup
import json
import time
import calendar
import schedule



# import functions
from BDD.connect import *
from snmp import Snmp_server



app = Flask(__name__)

# secret key for session (mandatory)
app.secret_key = "session is used in this application!"


labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]


values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"
    ]






######################################################################################################
####################    SNMP Schedule   ############################
######################################################################################################

from models import *



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
        insert_val = (time_stamp, equipement_id, str(data))

        conn = connection.cursor()
        conn.execute(insert_sql, insert_val)
        connection.commit()
        
        #print(oids_database[0]['id'])
    


#schedule.every(1).minutes.do(snmp_job)




"""
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
"""







@app.route('/', methods=['GET', 'POST'])
def index():
    bar_labels=labels
    bar_values=values


    conn = connection.cursor(dictionary=True)
    conn.execute("SELECT * FROM snmp_result")
    result  = conn.fetchall()

    conn.close()


    return render_template('index.html', title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels, values=bar_values)

    #return render_template('index.html')


@app.route('/equipement', methods=['GET', 'POST'])
def equipemnts():

    conn = connection.cursor()
    conn.execute("SELECT * FROM equipements")
    equipements = conn.fetchall()
    
    conn.close()
    
    return render_template('equipements.html', rows=equipements)



# Show equipement form
@app.route('/equipement/add-equipement', methods=['GET', 'POST'])
def add_equipemnts():
    conn = connection.cursor(dictionary=True)
    conn.execute("SELECT id,name FROM oids")
    data = conn.fetchall()
    conn.close()

    return render_template('add_equipement.html', ids=data)



@app.route('/equipement/create-equipement', methods=['POST'])
def create_equipemnts():
    data = request.form.to_dict()

    constructeur = data['constructeur']
    type_de_material = data['type_de_material']
    ipdns = data['ipdns']
    description = data['description']
    level = data['level']


    cur = connection.cursor(dictionary=True)

    sql_query = "INSERT INTO equipements (constructeur,type_de_material,ipdns,description,level) VALUES (%s,%s,%s,%s,%s)"
    data = (constructeur, type_de_material, ipdns, description, level)
    cur.execute(sql_query, data)
    connection.commit()

    cur.close()
    msg = "Record successfully added"
    
    return redirect('/equipement')
        



@app.route('/equipement/<equip_id>/edit-equipement', methods=['GET', 'POST'])
def edit_equipemnts(equip_id):
    equip_id = equip_id

    conn = connection.cursor()
    conn.execute("SELECT * FROM equipements where id="+equip_id)
    equipements = conn.fetchall()
    
    conn.close()

    return render_template('edit_equipement.html', data=equipements)





@app.route('/equipement/update-equipement', methods=['POST'])
def update_equipemnts():
    data = request.form.to_dict()

    print(data)
    try:
        conn = connection.cursor()
        
        sql_update_query = """UPDATE equipements SET constructeur=%s,type_de_material=%s,ipdns=%s,description=%s,level=%s WHERE id=%s"""
        data = (data['constructeur'],data['type_de_material'],data['ipdns'],data['description'],data['level'], data['id'])

        conn.execute(sql_update_query, data)
        conn.commit()
        msg = "Record successfully added"

    except mysql.connector.Error as error :
        print("Failed to update table record: {}".format(error))
    finally:
        #return render_template("result.html",msg = msg)
        if connection.is_connected():
            conn.close()
            return redirect('/equipement')




@app.route('/equipement/delete-equipement', methods=['POST'])
def delete_equipemnts():
    data = request.form.to_dict()
    equip_id = data['id']

    conn = connection.cursor()
    conn.execute("DELETE FROM equipements where id="+equip_id)
    connection.commit()
    conn.close()
    
    msg = "Record has been delete successfuly !"
    return redirect('/equipement')








############################################################################
############### OID ROUTES ################################################
###########################################################################


@app.route('/oids', methods=['GET', 'POST'])
def oids():
    conn = connection.cursor(dictionary=True)
    conn.execute("SELECT * FROM oids")
    oids = conn.fetchall()
    columns = conn.column_names

    # use dictionary=True in conn.cursor

    """
    oids_list = {}
    for i in range(0, len(oids)):
        temp = json.loads(oids[i][2])
        #oids_list.append(temp)
        oids_list[oids[i][0]] = temp
    """

    """
    print(type(oids))

    res = json.loads(oids[1][1])
    
    print(type(oids[1][1]))
    print(res)
    """
    conn.close()
    
    return render_template('oids.html', rows=oids)



# Show equipement form
@app.route('/oids/create-oid', methods=['GET', 'POST'])
def create_oid():
    return render_template('index.html')




@app.route('/oids/add-oid', methods=['POST'])
def add_oid():
    data = request.form.to_dict()

    
    try:
        conn = create_connection('BDD/database.db')
        cur = conn.cursor()

        cur.execute("INSERT INTO equipements (constructeur,type_de_material,ipdns,description,level) VALUES(?,?,?,?,?)",(data['constructeur'],data['type_de_material'],data['ipdns'],data['description'],data['level']))
        conn.commit()
        msg = "Record successfully added"

    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        #return render_template("result.html",msg = msg)
        close_connection(conn)
        return redirect('/')
        







"""
while True:
    schedule.run_pending()
    time.sleep(1)
""" 


if __name__ == '__main__':

    #Run web server for APP
    app.run('192.168.56.201')


    

