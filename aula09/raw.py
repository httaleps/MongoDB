## Tales Henrique Silveira de Sousa

from models.connection_options.connection import get_database
from models.repository.projeto_repository import myProjectRepository

# Instancia o repositório
db = get_database()
repository = myProjectRepository(db)

# -------------------------------------------------------
# INSERT - garante que os documentos existem para os testes
# -------------------------------------------------------
print("=== Inserindo documentos de teste ===")

repository.insert_bulk([
    {
        "nome": "Tales Sousa",
        "profissao": "Estudante de TI",
        "idade": 22,
        "tag": "projeto_tales",
        "pedidos": {"pizza": "calabresa", "batata frita": "media"}
    },
    {
        "nome": "Tales Henrique",
        "profissao": "Estagiário",
        "idade": 21,
        "tag": "projeto_tales",
        "pedidos": {"pizza": "frango", "refrigerante": "lata"}
    }
])
print("Documentos inseridos com sucesso.")

# -------------------------------------------------------
# SELECT - confirma os dados antes de editar
# -------------------------------------------------------
print("\n=== Documentos antes do update ===")
resultado = repository.select_many({"tag": "projeto_tales"})
for doc in resultado:
    print(doc)

# -------------------------------------------------------
# UPDATE - atualiza profissão do Tales Sousa
# -------------------------------------------------------
print("\n=== Executando update ===")
repository.update_document(
    {"nome": "Tales Sousa"},
    {"profissao": "Desenvolvedor Full Stack", "tag": "projeto_tales_atualizado"}
)

print("\n=== Documento após update ===")
resultado = repository.select_one({"nome": "Tales Sousa"})
print(resultado)

# -------------------------------------------------------
# DELETE - remove o documento do Tales Henrique
# -------------------------------------------------------
print("\n=== Executando delete ===")
repository.delete_document({"nome": "Tales Henrique"})

print("\n=== Documentos após delete (deve restar apenas Tales Sousa) ===")
resultado = repository.select_many({"tag": {"$in": ["projeto_tales", "projeto_tales_atualizado"]}})
for doc in resultado:
    print(doc)