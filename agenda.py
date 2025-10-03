from datetime import datetime

agenda = []

def registrar_atividade():
    print("\n== Agenda de Voluntários ==")
    id_voluntario = input("ID do voluntário: ").strip()
    nome = input("Nome do voluntário: ").strip()
    atividade = input("Atividade: ").strip()
    status = input("Status (confirmado/pendente): ").strip().lower()
    
    if status not in ("confirmado", "pendente"):
        print("Status inválido. Digite 'confirmado' ou 'pendente'.")
        return

    data_input = input("Data (dd/mm/aaaa): ").strip()
    try:
        data = datetime.strptime(data_input, "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError:
        print("Data inválida. Digite no formato dd/mm/aaaa.")
        return

    evento = {
        "id_voluntario": id_voluntario,
        "nome": nome,
        "atividade": atividade,
        "status": status,
        "data": data
    }

    agenda.append(evento)
    print("Atividade registrada com sucesso!")

def listar_agenda():
    if not agenda:
        print("Nenhuma atividade registrada.")
        return
    print("\n== Agenda de Voluntários ==")
    for i, e in enumerate(agenda, 1):
        print(f"{i}. ID: {e['id_voluntario']} - Nome: {e['nome']} - Atividade: {e['atividade']} - Status: {e['status']} - Data: {e['data']}")

def menu():
    while True:
        print("1 - Registrar na agenda ")
        print("2 - Listar agenda")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            registrar_atividade()
        elif opcao == "2":
            listar_agenda()
        else:
            print("Opção inválida.")

menu()
