from flask import Flask, jsonify, request, abort
from carsDAO import carsDAO
import mysql.connector

app = Flask(__name__, static_url_path='', static_folder='.')



#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/books"
@app.route('/cars')
def getAll():
    #print("in getall")
    results = carsDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/cars/<int:id>')
def findById(id):
    foundCar = carsDAO.findByID(id)

    return jsonify(foundCar)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"make\":\"Merc\",\"year\":\"2019\",\"price\":60000}" http://127.0.0.1:5000/books
@app.route('/cars', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    car = {
        "make": request.json['make'],
        "year": request.json['year'],
        "price": request.json['price'],
    }
    values =(car['make'],car['year'],car['price'])
    newId = carsDAO.create(values)
    car['id'] = newId
    return jsonify(car)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
@app.route('/cars/<int:id>', methods=['PUT'])
def update(id):
    foundCar = carsDAO.findByID(id)
    if not foundCar:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'year' in reqJson:
        foundCar['year'] = reqJson['year']
    if 'make' in reqJson:
        foundCar['make'] = reqJson['make']
    if 'price' in reqJson:
        foundCar['price'] = reqJson['price']
    values = (foundCar['make'],foundCar['year'],foundCar['price'],foundCar['id'])
    carsDAO.update(values)
    return jsonify(foundCar)
        

    

@app.route('/cars/<int:id>' , methods=['DELETE'])
def delete(id):
    carsDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)