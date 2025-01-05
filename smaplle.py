import sqlite3
#create database
conn=sqlite3.connect("sample.db")
print("Databse is created")

cursor=conn.cursor()

cursor.execute("create table if not exists student(id integer primary key autoincrement,name text,age integer) ")
print("Table is created")

cursor.execute("insert into student(name,age) values('anagha',22)")
cursor.execute("insert into student(name,age) values('manu',22)")
cursor.execute("insert into student(name,age) values('sasu',22)")
conn.cursor()
print("insert succussfully")

cursor.execute("select * from student")
rows=cursor.fetchall()
print("record display")
for i in rows:
    print(i)
cursor.execute("update student set name='anju' where id=1")
conn.commit()
print("Update succussfully")
cursor.execute("delete from student where id=2")
conn.commit()
print("record display")
for i in rows:
    print(i)
cursor.execute
