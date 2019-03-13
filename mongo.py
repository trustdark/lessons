import pymongo


client_conn = pymongo.MongoClient('127.0.0.1', 27017)
# client.admin.authenticate('root', 'samsung1', mechanism = 'SCRAM-SHA-1')
db = client_conn["mysinoptik"]
collection = db["weather"]

# print(collection)
# print(db.list_collection_names())

# db = client.["mysinoptik"]

# cursor = db.weather.find("city:Kyiv")
# print(cursor)


# print(client.list_database_names())  #divniy vuvid u bazi, yak ce vihlyadae u 2?
# if "mysinoptik" in client.list_database_names():
#     print("Eve is ok") ####eve is ok     u'mysinoptik == "mysinoptik"
