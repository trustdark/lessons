import pymongo
import json

"""access to database"""
client_conn = pymongo.MongoClient('127.0.0.1', 27017)
# client.admin.authenticate('root', 'samsung1', mechanism = 'SCRAM-SHA-1')
db = client_conn["mysinoptik"]
coll_1 = db["weather"]
coll_2 = db["seismicity"]

def handler(req):
    if req == "initial request":
        """making list of values for weather"""
        """making city list"""


        x = ['Chernihiv', 'Kyiv']
        return x

        # return list(coll_1.distinct("city"))
        # print(city)

        """making temp list"""
        temp = list(coll_1.distinct("temperature"))
        print(temp)
#
        """making wind speed list"""
        wind = list(coll_1.distinct("wind_speed"))
        print(wind)

        """making humidity list"""
        hum = list(coll_1.distinct("humidity"))
        print(humidity)


        """making date list"""

    else:
        print("Here's new request")

#cursor
#
# """making city list"""
# city = list(coll_1.distinct("city"))
# print(city)
#
# """making temp list"""
# temp = list(coll_1.distinct("temperature"))
# print(temp)
# #
# """making wind speed list"""
# wind = list(coll_1.distinct("wind_speed"))
# print(wind)
#
# """making humidity list"""
# hum = list(coll_1.distinct("humidity"))
# print(hum)
# """making date list"""
# city_list = []
# result = []
# for x in coll_1.find({"city": { "$nin": []}},{"_id":0,"city":1}):
#     result.append(x)
# print(result)

# print(coll_1)
# print(db.list_collection_names())
# help(db.list_collection_names())
# db = client.["mysinoptik"]

# cursor = db.weather.find("city:Kyiv")
# print(cursor)
