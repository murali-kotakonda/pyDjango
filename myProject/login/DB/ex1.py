import sqlite3

# connecting to the database
connection = sqlite3.connect("myTable.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE PERSON (  
ID INTEGER PRIMARY KEY,  
NAME VARCHAR(20),  
AGE INTEGER,  
SALARY INTEGER);"""
#joining DATE
# execute the statement
crsr.execute(sql_command)
connection.commit()

print("table create success...")
# close the connection
connection.close()