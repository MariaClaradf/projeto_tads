from random import randint
list = []


def cod_disciplina():
    cod = str(randint(1000, 3000))
    return cod

def cadastro_disciplina():
    nome = input('Digite o nome da sua disciplina: ')
    codigo = cod_disciplina()
    horas = input('Digite sua carga horária: ')
    prof = input('Digite o nome do professor: ')
    
    list.append({'nome': nome, 'código': codigo, 'carga horária': horas, 'professor': prof})
cadastro_disciplina()