from datetime import datetime

relatorios = []

def registrar_relatorio():
    print("\n== Registrar Relatório ==")
    tipo = input("Tipo (doacoes/despesas): ").strip().lower()
    if tipo not in ("doacoes", "despesas"):
        print("Tipo inválido. Digite 'doacoes' ou 'despesas'.")
        return

    valor = input("Valor (R$): ").strip()
    try:
        valor = float(valor)
    except ValueError:
        print("Valor inválido. Digite um número.")
        return

    descricao = input("Descrição: ").strip()
    
    data_input = input("Data (dd/mm/aaaa): ").strip()
    try:
        data = datetime.strptime(data_input, "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError:
        print("Data inválida. Digite no formato dd/mm/aaaa.")
        return

    relatorio = {
        "tipo": tipo,
        "valor": valor,
        "descricao": descricao,
        "data": data
    }

    relatorios.append(relatorio)
    print("Relatório registrado com sucesso!")

def listar_relatorios():
    if not relatorios:
        print("Nenhum relatório registrado.")
        return
    print("\n== Relatórios Registrados ==")
    for i, r in enumerate(relatorios, 1):
        print(f"{i}. Tipo: {r['tipo']} - Valor: R${r['valor']:.2f} - Descrição: {r['descricao']} - Data: {r['data']}")

def menu():
    while True:
        print("\n1 - Registrar relatório")
        print("2 - Listar relatórios")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            registrar_relatorio()
        elif opcao == "2":
            listar_relatorios()
        else:
            print("Opção inválida.")

menu()
