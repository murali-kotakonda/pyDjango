import sqlite3

# connecting to the database
con = sqlite3.connect("myTable.db")

cursor = con.cursor()
print("conn success")
sql = "INSERT INTO PERSON VALUES(6994,'raj kumada4',35,5000)"
cursor.execute(sql)
con.commit()

print(cursor.rowcount, "record inserted.")
print("1 record inserted, ID:", cursor.lastrowid)
if cursor:
        cursor.close()
if con:
        con.close()

