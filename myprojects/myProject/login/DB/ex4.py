import sqlite3

# connecting to the database
con = sqlite3.connect("myTable.db")

cursor = con.cursor()
print("conn success")


List = [(1008, 'User1', 30, 2390),(1009, 'User2', 30, 2390),(1020, 'User3', 30, 2391)]
cursor.executemany("INSERT INTO PERSON VALUES(?,?,?,?);", List)
con.commit()
print(cursor.rowcount, "record inserted.")


if cursor:
   cursor.close()
if con:
    con.close()


