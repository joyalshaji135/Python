import sqlite3
#create database
conn=sqlite3.connect("dbdata.db")
print("Databse is created succussfully")

# creating a cursor object

cursor=conn.cursor()
#create a table

cursor.execute("create table if not exists student(id integer primary key autoincrement,name text,age integer)")
print("Table is craeted succussfully")
#insert rec into table

cursor.execute("insert into student(name,age) values('anju',21)")
cursor.execute("insert into student(name,age) values('anu',25)")
conn.commit()
print("Record are inserted succussfully")
#fetching records

cursor.execute("select * from student")
rows=cursor.fetchall()

print("Fetching records are :")
for i in rows:
    print(i)
#update records

cursor.execute("update  student set name='manu' where id=1")
conn.commit()
print("Updated succussfully")

#Deleteing rec
cursor.execute("delete from student where id=2")
conn.commit()
print("Deleting succussfully")

cursor.execute("select * from student")
rows=cursor.fetchall()
for i in rows:
    print(i)
cursor.execute("drop table if exists student")
conn.commit()
print("Table is succussfully deleted")
conn.close()

