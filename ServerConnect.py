import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='root',
    database ='project'
)

cursor=  db.cursor()
sql='insert into cars (make, year, price) values (%s,%s,%s)'
values= ('Ford', '2016','15000')
cursor.execute(sql,values)

db.commit()