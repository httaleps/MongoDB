from models.connection_options.connection import DBConnectionHandler
from models.repository.my_collection_repository import myCollectionRepository

db_handler = DBConnectionHandler()
db_handler.connect_to_db()
db_connection = db_handler.get_db_connection()

my_collection_repository = myCollectionRepository(db_connection)


order = {
    "nome": "Lhama",
    "endereço": "Rua das Lhamas, 123",
    "pedidos": {
        "pizza": "1",
        "refrigerante": "2",
        "batata": "1"
    }
}

my_collection_repository.insert_documents(order)