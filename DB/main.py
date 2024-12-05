

import sqlite3
from models import *
connection = sqlite3.connect("c:\\Users\\Lenovo\\DB\\data.db")
cursor = connection.cursor()

# cursor.execute(create_table)
cursor.execute('''INSERT INTO USER VALUES (1,"jOHN","JN4488")''')
cursor.execute('''INSERT INTO USER VALUES (2,'RAJU','RAJU@123')''')

cursor.execute('''INSERT INTO EMP VALUES (1,"jOHN","LONDON","IT")''')