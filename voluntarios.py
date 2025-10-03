voluntarios = []

def voluntarios_menu():
    print("\n== Voluntários ==")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip().lower()

    if "@" not in email or email.split("@")[1] not in ("gmail.com", "hotmail.com", "outlook.com", "yahoo.com"):
        print("Email inválido. Aceitamos apenas gmail, hotmail, outlook ou yahoo.")
        return

    telefone = input("Telefone (apenas números, incluindo DDD): ").strip()
    if not telefone.isdigit() or len(telefone) < 10:
        print("Telefone inválido. Deve conter apenas números e incluir DDD.")
        return

    disponibilidade = input("Disponibilidade (ex: 'segunda a sexta 14h-18h'): ").strip()
    funcao = input("Função (ex: 'alimentação', 'limpeza', 'administração'): ").strip()

    voluntario = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "disponibilidade": disponibilidade,
        "funcao": funcao
    }

    voluntarios.append(voluntario)
    print("Voluntário cadastrado com sucesso!")

def listar_voluntarios():
    if not voluntarios:
        print("Nenhum voluntário cadastrado.")
        return
    print("\n== Voluntários Cadastrados ==")
    for i, v in enumerate(voluntarios, 1):
        print(f"{i}. {v['nome']} - {v['email']} - {v['telefone']} - {v['disponibilidade']} - {v['funcao']}")

def menu():
    while True:
        print("\n1 - Voluntários")
        print("2 - Listar voluntários")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            voluntarios_menu()
        elif opcao == "2":
            listar_voluntarios()
        else:
            print("Opção inválida.")

menu()
