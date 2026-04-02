# Tales

from pymongo import MongoClient

client = MongoClient("localhost", 27017)
                     
db = client.tales_mydb

people = db.people

print("\nConexão bem-sucedida!")

for i in range(1, 6):
    nome = input(f"Digite o nome da pessoa {i}: ")
    idade = input(f"Digite a idade da pessoa {i}: ")
    disciplina = input(f"Digite a disciplina do aluno matriculado {i}: ")
    nota = input(f"Digite a nota do aluno matriculado {i}: ")
    aprovado = "Aprovado" if float(nota) >= 6.0 else "Reprovado"
    person = {"Nome": nome, "Idade": int(idade), "Disciplina": disciplina, "Nota": float(nota), "Status": aprovado}
    people.insert_one(person)

for person in people.find():
    print(person)


