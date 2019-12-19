from carsDAO import carsDAO

#create
latestid = carsDAO.create(('Ford', 2010,15000))
# find by id
result = carsDAO.findByID(latestid);
print (result)

#update
carsDAO.update(('Fiat',2015,1900,latestid))
result = carsDAO.findByID(latestid);
print (result)

# get all 
allcars = carsDAO.getAll()
for cars in allcars:
  print(cars)

# delete
carsDAO.delete(latestid)
