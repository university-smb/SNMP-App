from flask import Flask, render_template, request, session, redirect, send_from_directory, Markup, jsonify, Response
import json
import time
import calendar
import schedule
from threading import Thread



# import functions
from BDD.connect import *
from snmp import Snmp_server
from models import *



app = Flask(__name__)

stop_run = False

# secret key for session (mandatory)
app.secret_key = "session is used in this application!"





colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"
]






######################################################################################################
####################    SNMP Schedule   ############################
######################################################################################################

from models import *
from snmp_run_job import *



def snmp_job_run():
    global stop_run
    while not stop_run:
        #snmp_job()
        time.sleep(1)
        print("Snmp server running...")


def manual_run():
    t = Thread(target=snmp_job_run)
    t.start()
    return "Processing"



@app.route('/', methods=['GET', 'POST'])
def index():
   
    conn = connection.cursor(dictionary=True)
    conn.execute("SELECT * FROM snmp_result where equipement_id=1  ORDER BY id DESC LIMIT 10")
    result  = conn.fetchall()
    conn.close()

    debit_sortant = []
    debit_entrant = []
    cpu = []
    ram = []
    timestamp = []

    oids_name = []

    for row in result:
        
        data = row["data"]
        datatojson = json.loads(data)

        debit_entrant.append(datatojson['debit_entrant'])
        debit_sortant.append(datatojson['debit_sortant'])
        cpu.append(datatojson['cpu'])
        ram.append(datatojson['ram'])

        timestamp.append(row['timestamp'])

        if len(oids_name)  == 0:
            oids_name.append(list(datatojson.keys()))
        
        #s = json.dumps(data)   
    #print(oids_name) 

    p_chart_value = [max(cpu), max(ram), max(debit_entrant), max(debit_sortant)]

    data = {
        "debit_sortant": debit_sortant,
        "debit_entrant": debit_entrant,
        "cpu": cpu,
        "ram": ram,
        "set" : zip(p_chart_value, oids_name[0], colors),
        "timestamp" : timestamp,
        "oids_name": oids_name,
        "max" : max(debit_sortant),
        "labels" : [1,2,3,4,5,6,7,8,9,10]
    }
    

    return render_template('index.html', title='Débit sortant', data=data)

    #return render_template('index.html')


@app.route('/equipement/start-supervision', methods=['GET', 'POST'])
def start_supervision():
    global stop_run
    stop_run = False
    manual_run()
    #return Response(manual_run(), mimetype="text/html")
    return redirect('/')



@app.route('/equipement/stop-supervision', methods=['GET', 'POST'])
def stop_supervision():
    global stop_run
    stop_run = True
    #return "Application stopped"
    return redirect('/')


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

    response = Response(status=200)
    
    return response
        



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
        


if __name__ == '__main__':

    #Run web server for APP
    app.run('192.168.56.201')
    


    

