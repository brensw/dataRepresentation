import mysql.connector
class carsDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="project"
        )
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into cars (make,year,price ) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from cars"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from cars where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result
    def update(self, values):
        cursor = self.db.cursor()
        sql="update cars set make= %s, year= %s, price= %s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from cars where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

carsDAO = carsDAO()