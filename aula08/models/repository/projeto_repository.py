from bson.objectid import ObjectId
from typing import Dict, List

from run import response


class myProjectRepository:
    def __init__(self, db_connection) -> None:
        self.__collection = db_connection.get_collection("my_collection")

    def insert_one(self, document):
        return self.__collection.insert_one(document)

    def insert_bulk(self, documents: List[Dict]) -> List[Dict]:
        return self.__collection.insert_many(documents)

    def select_many(self, filter) -> List[Dict]:
        data = self.__collection.find(
            filter, # Filtro
            {"cpf": 0, "endereco": 0, "_id": 0} # Opções de retorno
        )

        response = []
        for elem in data: response.append(elem)

        return response

    def select_one(self, filter) -> Dict:
        return self.__collection.find_one(filter, {"_id": 0})

    def select_if_property_exists(self) -> None:
        data = self.__collection.find({"cpf": { "$exists": True }})

        for elem in data: print(elem)

    def select_many_order(self):
        data = self.__collection.find(
            {"nome": "Cliente 2"},  # Filtro
            {"cpf": 0, "endereco": 0, "_id": 0}  # Opções de retorno
        ).sort([("pedidos.pizza", 1)])

        response = []
        for elem in data: print(elem)

    def select_or(self) -> None:
        data = self.__collection.find({ "$or": [{"nome": "Cliente 1"}, {"pedidos.batata frita": { "$exists" : True }}]})
        for elem in data:
            print(elem)
            print()

    def select_by_object_id(self) -> None:
        data = self.__collection.find({"_id": ObjectId("69d47383fd29de3f454a1189")})
        for elem in data: print(elem)

    def select_with_pagination(self, page: int, page_size: int) -> List[Dict]:
        data = self.__collection.find(
            {},
            {"cpf": 0, "endereco": 0, "_id": 0}
        ).skip((page -1) * page_size).limit(page_size)

        response = []
        for elem in data: response.append(elem)

        return response