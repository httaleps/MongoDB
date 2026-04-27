## Tales Henrique Silveira de Sousa

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

# =============================================
# INSERCAO DE DOCUMENTOS PERSONALIZADOS
# =============================================

documentos = [
    {
        "nome": "Tales Sousa",
        "endereco": "Rua Florianópolis, 42",
        "pedidos": {
            "pizza": 3,
            "batata frita": 2
        },
        "cpf": "00000000001"
    },
    {
        "nome": "Tales Dev",
        "endereco": "Av. Palhoça, 100",
        "pedidos": {
            "hamburguer": 5,
            "refrigerante": 3
        },
        "cpf": "00000000002"
    },
    {
        "nome": "Cliente Sousa",
        "endereco": "Rua MongoDB, 8",
        "pedidos": {
            "pizza": 1,
            "sorvete": 4
        },
        "cpf": "00000000003"
    }
]

for doc in documentos:
    validate_project(doc)

my_collection_repository.insert_bulk(documentos)
print("Documentos inseridos com sucesso!")
print()

# =============================================
# CONSULTAS
# =============================================

# Filtro simples
print("=== Filtro por nome e pedido ===")
response = my_collection_repository.select_many({"nome": "Tales Sousa"})
for doc in response: print(doc)
print()

# Select one
print("=== Select One ===")
response2 = my_collection_repository.select_one({"nome": "Tales Dev"})
print(response2)
print()

# Propriedade existe
print("=== Propriedade CPF existe ===")
my_collection_repository.select_if_property_exists()
print()

# Ordenacao
print("=== Ordenação ===")
my_collection_repository.select_many_order()
print()

# OR
print("=== Select OR ===")
my_collection_repository.select_or()
print()

# Paginacao
print("=== Paginação - Página 1 ===")
result = my_collection_repository.select_with_pagination(page=1, page_size=2)
for doc in result: print(doc)
print()

print("=== Paginação - Página 2 ===")
result = my_collection_repository.select_with_pagination(page=2, page_size=2)
for doc in result: print(doc)