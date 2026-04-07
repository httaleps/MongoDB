from typing import Dict, List

class myProjectRepository:
    def __init__(self, db_connection) -> None:
        self.__collection = db_connection.get_collection("my_collection")

    def insert_one(self, document):
        return self.__collection.insert_one(document)

    def insert_bulk(self, documents: List[Dict]) -> List[Dict]:
        return self.__collection.insert_many(documents)