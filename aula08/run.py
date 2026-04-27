from typing import Dict, List
from models.connection_options.connection import DBConnectionHandler
from models.repository.projeto_repository import myProjectRepository    

# funcao de validacao
def validate_project(project: Dict) -> bool:
    required_fields = {
        "nome": str, 
        "endereco": str, 
        "pedidos": dict, 
        "cpf": str
    }
        
    # verifica campos obrigatorios
    for field, field_type in required_fields.items():
        if field not in project:
            raise ValueError(f"Campo obrigatório ausente: {field}")
        
        if not isinstance(project[field], field_type):
            raise TypeError(f"Campo '{field}' deve ser do tipo {field_type.__name__}")
        
    return True

# conexao com o banco de dados
db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

my_collection_repository = myProjectRepository(db_connection)

my_collection_repository.select_many()

# # Inserir um documento
# my_collection_repository.insert_one(
#     {
#         "nome": "Cliente 2",
#         "endereco": "Rua 2, 20",
#         "pedidos": {
#             "pizza": 2,
#             "batata frita": 1
#         },
#         "cpf": f"00000000002"
#     }
# )