usuarios = []

def cadastrar():
    print("\n== Cadastro de Usuário ==")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip().lower()
    senha = input("Senha: ").strip()
    
    tipo = input("Tipo (admin/voluntario): ").strip().lower()
    if tipo not in ("admin", "voluntario"):
        print("Tipo inválido. Escolha apenas 'admin' ou 'voluntario'.")
        return

    cpf = input("CPF (apenas números, 11 dígitos): ").strip()
    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido. Deve conter apenas números e 11 dígitos.")
        return

    if "@" not in email or email.split("@")[1] not in ("gmail.com", "hotmail.com"):
        print("Email inválido. Aceitamos apenas gmail.com ou hotmail.com.")
        return

    for u in usuarios:
        if u["email"] == email:
            print("Já existe um usuário com esse email.")
            return

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "tipo": tipo,
        "cpf": cpf
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def login():
    print("\n== Login ==")
    email = input("Email: ").strip().lower()
    senha = input("Senha: ").strip()
    for u in usuarios:
        if u["email"] == email and u["senha"] == senha:
            print(f"Login bem-sucedido! Bem-vindo(a), {u['nome']} ({u['tipo']})")
            return
    print("Email ou senha incorretos.")

def menu():
    while True:
        print("\n1 - Cadastrar usuário")
        print("2 - Login")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            login()
        else:
            print("Opção inválida.")

menu()
