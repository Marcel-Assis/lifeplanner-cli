# lifeplanner/main.py
# Importa do arquivo storage as funções de salvar e carregar tarefas
from storage import carregar_tarefas, salvar_tarefas

# Primeiro Menu de Tarefas do LifePlanner - Versão CLI
def menu_tarefas(tarefas):
    while True:
        print("\n=== Menu de Tarefas ===")
        print("[1] Ver tarefas")
        print("[2] Adicionar tarefa")
        print("[3] Marcar tarefa como concluída")
        print("[4] Editar tarefa")
        print("[5] Remover tarefa")
        print("[6] Voltar ao menu principal")
        opcao = input("\nEscolha uma opção: ")
        if opcao == '1':
            ver_tarefas(tarefas)
        elif opcao == '2':
            adicionar_tarefa(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            editar_tarefa(tarefas)
        elif opcao == '5':
            remover_tarefa(tarefas)
        elif opcao == '6':
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Menu Inicial do LifePlanner - Versão CLI
def mostrar_menu_inicial(tarefas):
    while True:
        print(f"\n=== LifePlanner Menu ===\n"
            "[1] Gerenciar tarefas\n"
            "[2] Sair\n")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            menu_tarefas(tarefas)
        elif escolha == '2':
            print("Saindo do LifePlanner. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Listar Tarefas
def listar_tarefas(tarefas):
    for i, tarefa  in enumerate(tarefas, start=1):
            status_legivel = "Concluída" if tarefa["status"] else "Não concluída"
            print(f"{i}. {tarefa['titulo']} [{tarefa['categoria']}] - {status_legivel}")

# Visualizar Tarefas
def ver_tarefas(tarefas):
    print(f"\n=== Tarefas de Hoje ===")
    if tarefas == []:
        print("Nenhuma tarefa cadastrada ainda.")
    else:
        listar_tarefas(tarefas)

# Adicionar Tarefa
def adicionar_tarefa(tarefas):
    titulo = input("Título: ")
    categoria = input("Categoria: ")
    tarefa = {'titulo': titulo, 'categoria': categoria, 'status': False}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("\nTarefa adicionada com sucesso!")

# Marcar Tarefa como Concluída
def concluir_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas para selecionar.")
        return
    listar_tarefas(tarefas)
    print("\nDigite o número da tarefa que deseja marcar como concluída:")  
    escolha = int(input()) - 1
    tarefas[escolha]['status'] = True
    salvar_tarefas(tarefas)
    titulo = tarefas[escolha]['titulo']
    print(f"\n✔ Tarefa concluída: {titulo}")


# Editar Tarefa
def editar_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas para selecionar.")
        return
    listar_tarefas(tarefas)
    print("\nDigite o número da tarefa que deseja editar:")
    escolha = int(input()) - 1
    novo_titulo = input("Novo título: ")
    nova_categoria = input("Nova categoria: ")
    tarefas[escolha]['titulo'] = novo_titulo
    tarefas[escolha]['categoria'] = nova_categoria
    salvar_tarefas(tarefas)
    print("Tarefa editada com sucesso!")
    print(f"Tarefa {tarefas[escolha]['titulo']} [{tarefas[escolha]['categoria']}] atualizada.")

# Remover Tarefa
def remover_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas para selecionar.")
        return
    listar_tarefas(tarefas)
    print("\nDigite o número da tarefa que deseja remover:")
    escolha = int(input()) - 1
    print(f"Tarefa {tarefas[escolha]['titulo']} removida com sucesso!")
    tarefas.pop(escolha)
    salvar_tarefas(tarefas)

# Mensagem de Boas-Vindas
def mostrar_boas_vindas(nome):
    print("=" * 40)
    print("      LifePlanner - Versão CLI")
    print("=" * 40)
    print(f"Olá, {nome}! Vamos organizar seu dia?")

# Função Principal
def main():
    tarefas = carregar_tarefas()
    nome = input("Digite seu nome: ")
    mostrar_boas_vindas(nome)
    mostrar_menu_inicial(tarefas)

# Execução do Programa
if __name__ == "__main__":
    main()
