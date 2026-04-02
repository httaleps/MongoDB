from pymongo import MongoClient
from .mongo_db_configs import mongo_db_infos

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = 'mongodb://{username}:{password}@{host}:{port}/?authSource=admin'.format(
            username=mongo_db_infos["USERNAME"],
            password=mongo_db_infos["PASSWORD"],
            host=mongo_db_infos["HOST"],
            port=mongo_db_infos["PORT"]
        )
        self.__database_name = mongo_db_infos["DB_NAME"]
        self.__client = None
        self.__db_connection = None


    def connect_to_db(self):
        try:
            self.__client = MongoClient(self.__connection_string)
            self.__db_connection = self.__client[self.__database_name]
            print("Conexão bem-sucedida ao MongoDB!")
        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")

    def get_db_connection(self):
        return self.__db_connection
    
    def get_db_client(self):
        return self.__client

    def disconnect(self):
        if self.client:
            self.client.close()
            print("Desconectado do MongoDB.")