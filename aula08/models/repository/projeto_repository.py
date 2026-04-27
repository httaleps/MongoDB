from typing import Dict, List

class myProjectRepository:
    def __init__(self, db_connection) -> None:
        self.__collection = db_connection.get_collection("my_collection")

    def insert_one(self, document):
        return self.__collection.insert_one(document)

    def insert_bulk(self, documents: List[Dict]) -> List[Dict]:
        return self.__collection.insert_many(documents)

    def select_many(self) -> List[Dict]:
        data = self.__collection.find(
            {"nome": "Cliente 2", "pedidos.pizza": 2}, # Filtro
        {"cpf": 0, "endereco": 0, "_id": 0} # Opções de retorno
        )

        print(data)

        for x in data:
            print(x)
            print()