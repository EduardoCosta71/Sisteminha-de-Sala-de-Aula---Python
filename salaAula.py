# Login para professor ou diretoria

user = "admin"
password = 123

# Sistema de login para entrar no sistema
while True:

    # Aqui é pedido para o funcionário digite o usuario e a senha para logar no sistema.
    # Foi feito uma verificação de uso correto da senha ou do usuario.
    print("Digite a senha e o usuário para acessar o sistema.")
    usuario = input("Digite o usuário: ")
    senha = int(input("Digite a senha: "))

    if usuario == user and senha == password:
        print("Usuario logado com sucesso!")
        break

    else:
        print("Usuário ou senha incorreto.")
        continue

# Dicionarios criado para armazenar o nome e a matricula do aluno.
matricula = {
    "Eduardo": 1,
    "Lucas":2,
}

# Dicionario para guardar a nota de cada aluno.
notas = {
    "Eduardo": 9.5,
    "Lucas": 10,
}


while True:

    # Nesta parte foi dada algumas opções para o professor ou diretor escolher.
    print("SISTEMA ESCOLAR")
    print("ESCOLHA UMA DAS OPÇÕES PARA PROSSEGUIR:")

    print("1 - CADASTRAR ALUNO")
    print("2 - LISTAR ALUNOS")
    print("3 - LANÇAR NOTAS")
    print("4 - CONSULTAR BOLETIM")
    print("5 - SAIR")

    escolha = input("Escola o número da opção desejada: ")


    # Caso seja a escolha 1, ele pode fazer o cadastro de outro aluno, além dos que já estão pré definidos.
    if escolha == "1":

        print("CADASTRO DE ALUNO")

        while True:

            # O professor adiciona a matricula do aluno e o nome dele.
            matriculaAluno = input("Digite a matricula do aluno: ")
            nomeAluno = input("Digite o nome do aluno que irá cadastrar: ")

            matricula[nomeAluno] = matriculaAluno
            
            print("Aluno Matriculado com sucesso!")


            print("Deseja matricular outro aluno? (s/n)")

            opcao = input("Digite 's' para sim e 'n' para não: ")

            if opcao.lower() == 's':
                continue
            
            elif opcao.lower() == 'n':
                print("Voltando ao menu principal...")
                break


    if escolha == "2":

        while True:

            # Aqui o professor pode listar cada um dos alunos que foram,
            # cadastrados.
            nome = input("Digite o nome do aluno: ")
            if nome in matricula:

                print(f"Aluno: {nome}")
                print(f"Matricula: {matricula[nome]}")

            else:
                print("Aluno não encontrado")

            # Aqui um estrutura se o professor deseja consultar outro aluno.
            print("Deseja consultar outro aluno? (s/n)")
            resposta = input("Digite 's' para sim ou 'n' para não: ")

            if resposta.lower() == 's':
                continue

            elif resposta.lower() == 'n':
                print("Voltando ao menu principal...")
                break

            else:
                print("Resposta inválida. Voltando ao menu principal...")
                break

    
    elif escolha == "3":

        while True:

            # Aqui é a parte responsável por adicionar média do aluno que ele obteve durante o semestre
            nome = input("Digite o nome do aluno que irá lançar a média: ")
            nota = float(input("Digite a média do aluno: "))

            notas[nome] = nota

            print("Nota adicionada com sucesso")

            print("Deseja adicionar outra nota? (s/n)")
            resposta = input("Digite 's' para sim ou 'n' para não: ")

            if resposta.lower() == 's':
                continue

            elif resposta.lower() == 'n':
                print("Voltando ao menu principal...")
                break

            else:
                print("Resposta inválida. Voltando ao menu principal...")
                break

    elif escolha == "4":

        while True:

            # Aqui o professor pode consultar o boletim de cada aluno.
            nome = input("Digite o nome do aluno que deseja consultar o boletim: ")

            if nome in notas:
                print(f"Boletim do aluno: {nome}")
                print(f"Boletim {notas[nome]:.2f}")

            else:
                print("Boletim não encontrado.")

            print("Deseja consultar outro boletim? (s/n)")
            resposta = input("Digite 's' para sim ou 'n' para não: ")

            if resposta.lower() == 's':
                continue

            elif resposta.lower() == 'n':
                print("Voltando ao menu principal...")
                break

            else:
                print("Resposta inválida. Voltando ao menu principal...")
                break

    
    elif escolha == "5":

        print("Saindo do Sistema....")
        break

    else:
        print("Até logo...")