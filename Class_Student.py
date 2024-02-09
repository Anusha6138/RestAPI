from dotenv import load_dotenv
import os
import urllib
from pymongo import MongoClient
import bson.objectid
import pprint

dotenv_path=os.path.join(os.path.dirname(__file__),".env")         #step-1
load_dotenv(dotenv_path)
password= os.environ.get("MONGODB_PWD")                            #step-2

e_username = urllib.parse.quote_plus("anusham6138")
e_password = urllib.parse.quote_plus(password)
connection_string = f"mongodb+srv://{e_username}:{e_password}@mongo-cluster.vaml93n.mongodb.net/?retryWrites=true&w=majority"    #step3

try:
    client=MongoClient(connection_string)                              #step-4
    dbs= client.list_database_names()
    print(dbs)


    db=client.Class
    collection=db.Students

    #2. insert users
    def insert_docs():
        first_names=["Tyler","Selena","John","Justin","Nicholas"]
        last_names=["Swift","Gomez","Victoria","Beiber","Hailey"]
        ages=[15,16,12,11,17]
        docs=[]
        for f_name,l_name,age in zip(first_names,last_names,ages):
            doc={
               "first_name": f_name,
               "last_name":l_name,
               "age":age
             }
            docs.append(doc)
        collection.insert_many(docs)
    insert_docs()

    #1. Get users 
    def find_student(name):
        student=collection.find_one({"first_name":name})
        pprint.printer.pprint(student)
    find_student("Tyler")

    #3. Update user
    def update_student(stud_id):
        _id =bson.objectid.ObjectId(stud_id)
        update={
            "$inc":{"age":3},
            "$rename":{"first_name":"Hailey", "last_name":"Beiber"}
        }
        collection.update_one({"_id":_id},update)
    update_student("65c5de6ee640b8a6884d2e02")  

    #4. delete user
    def delete_Student(stud_id):
        _id=bson.objectid.ObjectId(stud_id)
        collection.delete_one({"_id":_id})
    delete_Student("65c5de6ee640b8a6884d2e00")

except Exception as e:
    print("error connection to db")