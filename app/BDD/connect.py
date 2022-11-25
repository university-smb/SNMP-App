import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="phpmyadmin",
  password="root",
  database="snmp"
)


"""
try:
    conn = connection.cursor()

except Error as e:
    print("Error while connecting to MySQL", e)
"""
