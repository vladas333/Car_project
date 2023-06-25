import mysql.connector

mysqldb = mysql.connector.connect(
    host="localhost",
    database="myDB",
    user="vladas",
    password="vladas"
)
 
mycursor = mysqldb.cursor(dictionary=True)
mycursor.execute("SELECT * from VehicleModelYear;")
myresult = mycursor.fetchall()
 
# print(myresult)
import pymongo
 
mongodb_host = "mongodb://localhost:27017/"
mongodb_dbname = "All_cars"
myclient = pymongo.MongoClient(mongodb_host)
mydb = myclient[mongodb_dbname]
mycol = mydb["Cars"]
 
if len(myresult) > 0:
 
       x = mycol.insert_many(myresult) #myresult comes from mysql cursor
 
       print(len(x.inserted_ids))

print("VERY GOOD")