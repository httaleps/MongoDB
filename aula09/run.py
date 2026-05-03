## Tales Henrique Silveira de Sousa

from typing import Dict, List
from models.connection_options.connection import DBConnectionHandler
from models.repository.projeto_repository import myProjectRepository

# conexao com o banco de dados
db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

my_collection_repository = myProjectRepository(db_connection)

# filtro = { "profissao": "Programador" }
# propriedades = {
#     "endereco": {
#         "cep": "88136261",
#         "rua": "das Orquídeas",
#         "bairro": "São Sebastião",
#         "numero": 4
#     }
# }

# my_collection_repository.edit_many_registry(filtro, propriedades)

# my_collection_repository.edit_many_increment(-10)

my_collection_repository.delete_registry()