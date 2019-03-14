import pymongo
import json

"""access to database"""
client_conn = pymongo.MongoClient('127.0.0.1', 27017)
# client.admin.authenticate('root', 'samsung1', mechanism = 'SCRAM-SHA-1')
db = client_conn["mysinoptik"]
coll_1 = db["weather"]
coll_2 = db["seismicity"]

"""making list of values for weather"""
"""making city list"""
city_list = []
for x in list(coll_1.find({},{"_id":0,"temperature":0,"wind_speed":0,"humidity":0,"date":0})):
    while x not in city_list:
        city_list.append(x)
print(city_list)

"""making temp list"""
temp_list = []
for x in coll_1.find({},{"_id":0,"city":0,"wind_speed":0,"humidity":0,"date":0}):
    while x not in temp_list:
        temp_list.append(x)
print(temp_list)

"""making wind speed list"""
wind_list = []
for x in coll_1.find({},{"_id":0,"city":0,"temperature":0,"humidity":0,"date":0}):
    while x not in wind_list:
        wind_list.append(x)
print(wind_list)

"""making humidity list"""
hum_list = []
for x in coll_1.find({},{"_id":0,"city":0,"temperature":0,"wind_speed":0,"date":0}):
    while x not in hum_list:
        hum_list.append(x)
print(hum_list)

"""making date list"""

# Traceback (most recent call last):
#   File "mongo.py", line 15, in <module>
#     for x in coll_1.find({},{"_id":0,"temperature":0,"wind_speed":0,"humidity":0,"date":0}).items():
# AttributeError: 'Cursor' object has no attribute 'items'

# def handler(req):
#     if req == "initial request":
#
#     else:


# print(coll_1)
# print(db.list_collection_names())
# help(db.list_collection_names())
# db = client.["mysinoptik"]

# cursor = db.weather.find("city:Kyiv")
# print(cursor)


# print(client_conn.list_database_names())
# if "mysinoptik" in client_conn.list_database_names():
#     print("Eve is ok")
