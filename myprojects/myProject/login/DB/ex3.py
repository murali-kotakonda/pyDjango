import sqlite3

# connecting to the database
con = sqlite3.connect("myTable.db")

cursor = con.cursor()
print("conn success")

# SQL command to insert the data in the table
sql_command = """INSERT INTO PERSON VALUES (?,?,?,?)"""
cursor.execute(sql_command,(26, "Rishabh1", 89,1313))

con.commit()
print(cursor.rowcount, "record inserted.")
# close the connection
con.close()