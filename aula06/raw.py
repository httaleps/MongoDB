from pymongo import MongoClient

connection_string = "mongodb://admin:admin@localhost:27017/?authSource=admin"
client = MongoClient(connection_string)
db_connection = client["my_database"]

print(db_connection)
print()
collection = db_connection.get_collection("my_collection")

print(collection)
print()

search_filter = {"estou": "aqui"}
response = collection.find(search_filter)

for registry in response: print(registry)

collection.insert_one({
    "Estou": "Inserindo",
    "Números": [1, 2, 3, 4, 5]
    })
print("Documento inserido com sucesso!")