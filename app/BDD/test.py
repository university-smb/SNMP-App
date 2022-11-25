

from connect import *



conn.execute("SELECT constructeur,type_de_material,ipdns,description,level FROM equipements")
b = conn.fetchall()

print(conn.column_names[1])

