from random import randint
list = []


def cod_turma():
    cod = str(randint(1000, 3000))
    return cod

def cadastro_turmas():
    nome = input('Digite o nome da sua turma: ')
    cod = cod_turma()
    disciplina = input('Digite a sua disciplina: ')
    prof = input('Digite o nome do professor: ')
    aluno = input('Digite os nomes dos alunos separados por vírgula: ').split(',')
    
    list.append({'nome': nome, 'código': cod, 'disciplina': disciplina, 'professor': prof, 'aluno': aluno})
cadastro_turmas()