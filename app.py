from task_manager import TaskManager

manager = TaskManager()

while True:
    print("\n=== Gerenciador de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    option = input("Escolha: ")

    if option == "1":
        task = input("Digite a tarefa: ")
        manager.add_task(task)

    elif option == "2":
        print("\nTarefas:")
        for i, task in enumerate(manager.list_tasks(), start=1):
            print(f"{i}. {task}")

    elif option == "3":
        task = input("Digite a tarefa que deseja remover: ")
        if manager.remove_task(task):
            print("Tarefa removida.")
        else:
            print("Tarefa não encontrada.")

    elif option == "4":
        break

    else:
        print("Opção inválida.")