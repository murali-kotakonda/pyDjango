import sqlite3

# connecting to the database
con = sqlite3.connect("myTable.db")

cursor = con.cursor()
print("conn success")

cursor.execute("SELECT ID,NAME FROM person")
myresult = cursor.fetchall()
for x in myresult:
  print(x)

if cursor:
    cursor.close()
if con:
    con.close()


