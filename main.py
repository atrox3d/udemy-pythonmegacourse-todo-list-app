while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    print(f'user action: {user_action}')
    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"

            file = open("todos.txt", 'r')           # FileNotFoundError if file does not exist
            todos = file.readlines()
            file.close()

            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open("todos.txt", 'r')           # FileNotFoundError if file does not exist
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f'{index + 1}-{item}'
                print(row)
        case 'edit':
            pass
        case 'complete':
            pass
        case 'exit':
            break

print('goodbye')
