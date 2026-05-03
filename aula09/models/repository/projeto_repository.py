## Tales Henrique Silveira de Sousa

from bson.objectid import ObjectId
from typing import Dict, List


class myProjectRepository:
    def __init__(self, db_connection) -> None:
        self.__collection = db_connection.get_collection("my_collection")

    def insert_one(self, document):
        return self.__collection.insert_one(document)

    def insert_bulk(self, documents: List[Dict]) -> List[Dict]:
        return self.__collection.insert_many(documents)

    def select_many(self, filter) -> List[Dict]:
        data = self.__collection.find(
            filter,
            {"cpf": 0, "endereco": 0, "_id": 0}
        )
        response = []
        for elem in data:
            response.append(elem)
        return response

    def select_one(self, filter) -> Dict:
        return self.__collection.find_one(filter, {"_id": 0})

    def select_if_property_exists(self) -> None:
        data = self.__collection.find({"cpf": {"$exists": True}})
        for elem in data:
            print(elem)

    def select_many_order(self):
        data = self.__collection.find(
            {"nome": "Tales Sousa"},
            {"cpf": 0, "endereco": 0, "_id": 0}
        ).sort([("pedidos.pizza", 1)])
        for elem in data:
            print(elem)

    def select_or(self) -> None:
        data = self.__collection.find({
            "$or": [
                {"nome": "Tales Sousa"},
                {"pedidos.batata frita": {"$exists": True}}
            ]
        })
        for elem in data:
            print(elem)
            print()

    def select_by_object_id(self) -> None:
        data = self.__collection.find({"_id": ObjectId("69eeca74c8ef220c60ba6e44")})
        for elem in data:
            print(elem)

    def select_with_pagination(self, page: int, page_size: int) -> List[Dict]:
        data = self.__collection.find(
            {},
            {"cpf": 0, "endereco": 0, "_id": 0}
        ).skip((page - 1) * page_size).limit(page_size)
        response = []
        for elem in data:
            response.append(elem)
        return response

    def update_document(self, filter, updates) -> None:
        data = self.__collection.update_one(
            filter,
            {"$set": updates}
        )
        print(f"Documentos atualizados: {data.modified_count}")

    def delete_document(self, filter) -> None:
        data = self.__collection.delete_one(filter)
        print(f"Documentos removidos: {data.deleted_count}")