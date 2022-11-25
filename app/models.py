import mysql.connector

from BDD.connect import *


def get_equipements():

    try:
        conn = connection.cursor(dictionary=True)
        sql_select_query = """SELECT * FROM equipements"""
        conn.execute(sql_select_query)
        equipements = conn.fetchall()
        
    except mysql.connector.Error as error :
        print("Failed to select table record: {}".format(error))
    finally:
        #return render_template("result.html",msg = msg)
        if connection.is_connected():
            conn.close()
            return equipements



def get_oids(level):
    
    try:
        conn = connection.cursor(dictionary=True)
        sql_select_query = "SELECT * FROM oids where id="+level
        conn.execute(sql_select_query)
        db_oids = conn.fetchall()
        
    except mysql.connector.Error as error :
        print("Failed to select table record: {}".format(error))
    finally:
        if connection.is_connected():
            conn.close()
            return db_oids





