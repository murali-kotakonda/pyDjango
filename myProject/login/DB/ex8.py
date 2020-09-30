import sqlite3

# connecting to the database
connection = sqlite3.connect("myTable.db")

crsr = connection.cursor()
print("conn success")



# SQL command to insert the data in the table
sql_command = """UPDATE PERSON SET NAME = ? WHERE Id=?"""
crsr.execute(sql_command,("suchi",26))

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()
print(crsr.rowcount, "record updated.")
# close the connection
connection.close()