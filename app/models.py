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











"""
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()    # Required




class Contact( Base ):
    __tablename__ = 'T_Contacts'

    id = Column(Integer, primary_key=True)
    firstName = Column(Text)
    lastName = Column(Text)

    def __init__(self, pk=0, fn="John", ln="Doe"):
        self.id = pk
        self.firstName = fn
        self.lastName = ln

    def __str__(self):
        return self.firstName + " " + self.lastName
"""

