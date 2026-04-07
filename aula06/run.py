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

# criando 10 projetos
projects: List[Dict] = [
    {
        "nome": f"Cliente {i}",
        "endereco": f"Rua {i}, {i*10}",
        "pedidos": {
            "pizza": i,
            "hamburguer": i + 1
        },
        "cpf": f"0000000000{i}"
    }
    for i in range(1, 11)
]

# validacao antes de inserir
validated_projects = []

for project in projects:
    try:
        if validate_project(project):
            validated_projects.append(project)
    except (ValueError, TypeError) as e:
        print(f"Erro no projeto {project.get('nome')}: {e}")

# insercao em lote
if validated_projects:
    my_collection_repository.insert_bulk(validated_projects)
    print(f"{len(validated_projects)} projetos inseridos com sucesso.")
else:
    print("Nenhum projeto válido para inserção.")