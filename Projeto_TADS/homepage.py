from random import randint
import cadastroaluno
import cadastroprofessores
import cadastrodisciplinas
import cadastroturmas

alunos = []
professores = []
disciplinas = []
turmas = []


def num_matricula_aluno():
    num = str(randint(20000, 60000))
def num_matricula_prof():
    num = str(randint(10000, 50000))
def num_matricula():
    return str(randint(20000, 60000))

def filtrar_prof():
    disciplina = input('Digite o nome da disciplina para filtrar o professor: ')
    result = [prof for prof in professores if prof['disciplina'].lower() == disciplina.lower()]

    if result:
        print (f"Professores que ministram a disciplina '{disciplina}': ")
        for prof in result:
            print(f'{prof['nome']} (Matrícula: {prof['matricula']})')
    else:
        print (f"Nenhum professor encontrado em '{disciplina}'")  

def matricula_aluno():
    matricula = input('Digite a matrícula do aluno: ')
    cod = input('Digite o código da turma: ')

    aluno = None
    turma = None


def matricular_aluno_em_turma():
    print("\n--- Matrícula de Aluno em Turma ---")
    matricula_aluno = input("Digite a matrícula do aluno: ")
    turma_codigo = input("Digite o código da turma: ")

    aluno = next((aluno for aluno in alunos if aluno['matricula'] == matricula_aluno), None)
    turma = next((turma for turma in turmas if turma['codigo'] == turma_codigo), None)

    if aluno and turma:
        if aluno['nome'] not in turma['alunos']:
            turma['alunos'].append(aluno['nome'])
            print(f"Aluno {aluno['nome']} matriculado com sucesso na turma {turma['nome']}!")
        else:
            print(f"O aluno {aluno['nome']} já está matriculado na turma {turma['nome']}.")
    elif not aluno:
        print("Aluno não encontrado. Verifique a matrícula.")
    elif not turma:
        print("Turma não encontrada. Verifique o código.")



def menu():
    while True:
        print('1. Cadastrar Aluno')
        print('2. Cadastrar Professor')
        print('3. Cadastrar Disciplina')
        print('4. Cadastrar Turma')
        print('5. Filtrar Professores por Disciplina')
        print("6. Matricular Aluno em Turma")
        print('7. Sair')

        opc = input('Escolha uma opção: ')
        
        if opc == '1':
            cadastroaluno()
        elif opc == '2':
            cadastroprofessores()
        elif opc == '3':
            cadastrodisciplinas()
        elif opc == '4':
            cadastroturmas()
        elif opc == '5':
            filtrar_prof()
        elif opc == '6':
            print('Matricular Aluno em Turma')
        elif opc == '7':
            print('Saindo do sistema!')
            break
        else:
            print('Opção inválida. Tente novamente!')
menu()