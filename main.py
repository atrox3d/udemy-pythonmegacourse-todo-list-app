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
            pass
        case 'edit':
            pass
        case 'complete':
            pass
        case 'exit':
            break

print('goodbye')
