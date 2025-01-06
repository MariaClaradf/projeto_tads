from random import randint
list = []


def num_matricula():
    num = str(randint(10000, 50000))
    return num

def cadastro_aluno():
    nome = input('Digite seu nome: ')
    matricula = num_matricula()
    nascimento = input('Digite sua data de nascimento: ')
    genero = input('Digite seu genero: ')
    endereco = input('Digite seu endereço: ')
    telefone = input('Digite o seu telefone: ')
    email = input('Digite seu e-mail: ')
    list.append({'nome': nome, 'matricula': matricula, 'nascimento': nascimento, 'genero': genero, 'endereco': endereco, 'telefone': telefone, 'email': email})
cadastro_aluno()