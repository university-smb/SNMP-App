from flask import Flask, render_template, request, session, redirect, send_from_directory
import json

from routes.connect import *

app = Flask(__name__)

@app.route('/oids', methods=['GET', 'POST'])
def oids():

    conn = connection.cursor()
    conn.execute("SELECT * FROM oids")
    oids = conn.fetchall()
    
    conn.close()
    
    return render_template('../oid.html', rows=oids)



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
        




