def get_todos(filename="todos.txt"):
    """
    return a list of to-do items read from a file
    """
    with open(filename, 'r') as file:  # FileNotFoundError if file does not exist
        todos = file.readlines()
        return todos


def write_todos(todos, filename="todos.txt"):
    """
    write to-do items list to file
    """
    with open(filename, 'w') as file:
        file.writelines(todos)


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    print(f'user action: {user_action}')

    if user_action.startswith('add'):
        todos = get_todos()

        todo = user_action[len('add') + 1:]
        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1}-{item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            todos = get_todos()

            number = int(user_action[len('edit') + 1:])
            number -= 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            write_todos(todos)

        except ValueError:
            print("your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = get_todos()

            number = int(user_action[len('complete') + 1:])
            removed = todos.pop(number - 1).strip('\n')

            write_todos(todos)
            print(f"Todo {removed} was removed from the list")

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid')

print('goodbye')
