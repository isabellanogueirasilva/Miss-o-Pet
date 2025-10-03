adocoes = []

def registrar_adocao():
    print("\n== Registro de Adoção ==")
    id_animal = input("ID do animal: ").strip()
    nome_animal = input("Nome do animal: ").strip()
    adotante = input("Nome do adotante: ").strip()
    contato = input("Contato (telefone ou email): ").strip()
    data = input("Data (dd/mm/aaaa): ").strip()
    status = input("Status (em andamento/concluido): ").strip().lower()
    
    if status not in ("em andamento", "concluido"):
        print("Status inválido. Digite 'em andamento' ou 'concluido'.")
        return

    adocao = {
        "id_animal": id_animal,
        "nome_animal": nome_animal,
        "adotante": adotante,
        "contato": contato,
        "data": data,
        "status": status
    }

    adocoes.append(adocao)
    print("Adoção registrada com sucesso!")

def listar_adocoes():
    if not adocoes:
        print("Nenhuma adoção registrada.")
        return
    print("\n== Adoções Registradas ==")
    for i, a in enumerate(adocoes, 1):
        print(f"{i}. Animal ID: {a['id_animal']} - Nome: {a['nome_animal']} - Adotante: {a['adotante']} - Contato: {a['contato']} - Data: {a['data']} - Status: {a['status']}")

def menu():
    while True:
        print("\n1 - Registrar adoção")
        print("2 - Listar adoções")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            registrar_adocao()
        elif opcao == "2":
            listar_adocoes()
        else:
            print("Opção inválida.")

menu()
