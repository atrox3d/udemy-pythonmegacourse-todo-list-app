def get_todos(filename):
    with open(filename, 'r') as file:  # FileNotFoundError if file does not exist
        todos = file.readlines()
        return todos


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    print(f'user action: {user_action}')

    if user_action.startswith('add'):
        todo = user_action[len('add') + 1:]

        todos = get_todos("todos.txt")
        todos.append(todo + "\n")

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1}-{item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[len('edit') + 1:])
            number -= 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            with open("todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[len('complete') + 1:])

            todos = get_todos("todos.txt")

            removed = todos.pop(number - 1).strip('\n')

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

            print(f"Todo {removed} was removed from the list")
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid')

print('goodbye')
