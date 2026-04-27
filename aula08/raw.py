## Tales Henrique Silveira de Sousa

from models.connection_options.connection import get_database
from models.repository.projeto_repository import myProjectRepository

# Instancia o repositório
db = get_database()
repository = myProjectRepository(db)

# Busca com filtro
print("=== Filtro por nome ===")
result = repository.select_many({"nome": "Cliente 1"})
for doc in result: print(doc)

# Busca um documento
print("\n=== Select One ===")
result = repository.select_one({"nome": "Cliente 2"})
print(result)

# Busca se propriedade existe
print("\n=== Propriedade existe ===")
repository.select_if_property_exists()

# Busca com OR
print("\n=== Select OR ===")
repository.select_or()

# Busca com ordenação
print("\n=== Ordenação ===")
repository.select_many_order()

# Paginação
print("\n=== Paginação - Página 1 ===")
result = repository.select_with_pagination(page=1, page_size=3)
for doc in result: print(doc)

print("\n=== Paginação - Página 2 ===")
result = repository.select_with_pagination(page=2, page_size=3)
for doc in result: print(doc)