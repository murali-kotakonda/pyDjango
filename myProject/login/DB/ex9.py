import sqlite3

# connecting to the database
connection = sqlite3.connect("myTable.db")

crsr = connection.cursor()
print("conn success")



# SQL command to insert the data in the table
sql_command = """DELETE FROM PERSON WHERE Id=?"""
crsr.execute(sql_command,[26])

connection.commit()
print(crsr.rowcount, "record DELETED.")
# close the connection
connection.close()