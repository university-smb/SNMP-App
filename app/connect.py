#!/usr/bin/python  
  
import sqlite3  
import json
  
#connection = sqlite3.connect('BDD/database.db')  

#if (conn):
#    print("Opened database successfully") 


def create_connection(db_file):
    #-------------------------------------------------------
    """ Create a database connection to a SQLite database 
    :param db_file: SQLite database file name/path
    :return: Connection or None on error. 
    """
    #-------------------------------------------------------

    conn = None

    #Let's try and open the database. Will auto-create if not found.
    try:
        conn = sqlite3.connect(db_file)
        #print(sqlite3.version) #pyselite version
        #print(sqlite3.sqlite_version) #SQLLite engine version
        return conn
    except Error as e:
        print(e)
        return None


def close_connection(conn):
    #-------------------------------------------------------
    """ Close a database connection to a SQLite database 
    :param conn: Connection object
    :return: True-Success, False-Error
    """
    #-------------------------------------------------------

    # Let's attempt to close our database connection 
    try:
        conn.close()
        return True;
    except Error as e:
        print(e)
        return False


def create_table(conn, create_table_sql):
    #----------------------------------------------------------
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return: True-Success, False-Error
    """
     #----------------------------------------------------------
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        return True
    except Error as e:
        print(e)  
        return False


def execute(conn, sql):
    #----------------------------------------------------------
    """ Execute an SQL action query that does not return results
    :param conn: Connection object
    :param sql: SQL action query
    :return: True-Success, False-Error
    """
     #----------------------------------------------------------
    try:
        c = conn.cursor()
        c.execute(sql)
        return True
    except Error as e:
        print(e)  
        return False

def execute_query(conn, sql):
    #----------------------------------------------------------
    """ Execute an SQL query that does return results
    :param conn: Connection object
    :param sql: SQL query expecting results
    :return: Resulting cursor or None
    """
     #----------------------------------------------------------
    try:
        c = conn.cursor()
        c.execute(sql)
        return c
    except Error as e:
        print(e)  
        return None



def datatojson(data):

    tab = []

    for row in data:
        new_row = {
            "constructeur": row[0],
            "type_de_material": row[1],
            "IP": row[2],
            "DNS": row[3],
            "description": row[4],
            "level": row[5]
        }
        tab.append(new_row)
    return tab

