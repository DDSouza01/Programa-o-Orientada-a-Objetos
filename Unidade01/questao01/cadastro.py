from repositorio import alunos

while True:
    print("\n===== Cadastro de Alunos e Notas =====")
    print("1 - Adicionar aluno")
    print("2 - Atualizar notas de um aluno")
    print("3 - Remover aluno")
    print("4 - Exibir todos os alunos e notas")
    print("5 - Calcular médias dos alunos")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    
    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        notas = []
        for i in range(1, 5):
            nota = float(input(f"Digite a nota N{i}: "))
            notas.append(nota)
        alunos[nome] = notas
        print(f"Aluno '{nome}' cadastrado com sucesso!")

    
    elif opcao == "2":
        nome = input("Digite o nome do aluno para atualizar: ")
        if nome in alunos:
            novas_notas = []
            for i in range(1, 5):
                nota = float(input(f"Digite a nova nota N{i}: "))
                novas_notas.append(nota)
            alunos[nome] = novas_notas
            print(f"Notas do aluno '{nome}' atualizadas com sucesso!")
        else:
            print("Aluno não encontrado.")

    elif opcao == "3":
        nome = input("Digite o nome do aluno para remover: ")
        if nome in alunos:
            del alunos[nome]
            print(f"Aluno '{nome}' removido com sucesso.")
        else:
            print("Aluno não encontrado.")

    elif opcao == "4":
        if alunos:
            print("\n=== LISTA DE ALUNOS ===")
            for nome, notas in alunos.items():
                print(f"{nome}: {notas}")
        else:
            print("Nenhum aluno cadastrado.")

    elif opcao == "5":
        if alunos:
            print("\n=== MÉDIAS DOS ALUNOS ===")
            for nome, notas in alunos.items():
                media = sum(notas) / len(notas)
                print(f"{nome}: Média = {media:.2f}")
        else:
            print("Nenhum aluno cadastrado.")

    elif opcao == "6":
        print("Saindo do sistema... Até logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")