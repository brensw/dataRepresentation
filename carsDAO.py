import mysql.connector
import dbconfig as dbc
import MySQLdb





class CarsDAO:

    def connectDB(self):
        self.db = mysql.connector.connect(
        host= dbc.mysql['host'],
        user =dbc.mysql['user'],
        password=dbc.mysql['password'],
        database=dbc.mysql['database']
        )


    db=""
    def __init__(self): 
        self.connectDB()

    def getCursor(self):
        if not self.db.is_connected():
            self.connectDB()
            
        return self.db.cursor()        
            
    def create(self, values):
        cursor = self.getCursor()
        sql="insert into cars (make,year, price) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        cursor.close()   
        return cursor.lastrowid

    def getAll(self):
         cursor = self.getCursor()
        sql="select * from cars"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        cursor.close()    
        return returnArray

    def findByID(self, id):
         cursor = self.getCursor()
        sql="select * from cars where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()   
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.getCursor()
        sql="update cars set make= %s,year=%s, price=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()   


    def delete(self, id):
         cursor = self.getCursor()
        sql="delete from cars where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        cursor.close()   
       

    def convertToDictionary(self, result):
        colnames=['id','make','year', "price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
carsDAO = CarsDAO()
