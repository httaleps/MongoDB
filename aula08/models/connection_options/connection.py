from pymongo import MongoClient
from .mongo_db_configs import MONGO_URI, DATABASE_NAME


def get_database():
    client = MongoClient(MONGO_URI)
    return client[DATABASE_NAME]


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = MONGO_URI
        self.__database_name = DATABASE_NAME
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):
        try:
            self.__client = MongoClient(self.__connection_string)
            self.__client.admin.command('ping')
            self.__db_connection = self.__client[self.__database_name]
            print("Conexão bem-sucedida ao MongoDB!")
        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")

    def get_db_connection(self):
        return self.__db_connection

    def get_db_client(self):
        return self.__client

    def disconnect(self):
        if self.__client:
            self.__client.close()
            print("Desconectado do MongoDB.")