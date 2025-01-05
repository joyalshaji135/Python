import sqlite3
conn=sqlite3.connect("sampledb.db")
print("Database created and connect succussfully")

cursor=conn.cursor()

cursor.execute("create table if not exists student(id integer primary key autoincrement,name text,age integer)")
print("Table created succussfully")

cursor.execute("insert into student(name,age) values('abhi',20)")
cursor.execute("insert into student(name,age) values('susu',21)")
conn.commit()
print("Records inserted succussfully")

cursor.execute("select * from student")
rows=cursor.fetchall()
for i in rows:
    print(i)


cursor.execute("update student set name='subhi' where id=1")
conn.commit()
print("Rec update succussfully")

cursor.execute("Delete from student where id=1 ")
conn.commit()
print("Delete succussfully")

cursor.execute("select * from student")
rows=cursor.fetchall()
for i in rows:
    print(i)


cursor.execute("drop table if exists student")
conn.commit()
print(" table Delete succussfully")
conn.close()