while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    print(f'user action: {user_action}')
    match user_action:

        case 'add':
            todo = input("Enter a todo:") + "\n"

            with open("todos.txt", 'r') as file:    # FileNotFoundError if file does not exist
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case 'show':
            with open("todos.txt", 'r') as file:    # FileNotFoundError if file does not exist
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1}-{item}'
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= 1

            with open("todos.txt", 'r') as file:    # FileNotFoundError if file does not exist
                todos = file.readlines()

            new_todo = input("Enter new todo:") + "\n"
            todos[number] = new_todo

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to edit: "))

            with open("todos.txt", 'r') as file:    # FileNotFoundError if file does not exist
                todos = file.readlines()

            todos.pop(number - 1)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case 'exit':
            break

print('goodbye')
