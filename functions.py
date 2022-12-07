FILEPATH = "todos.txt"


def get_todos(filename=FILEPATH):
    """
    return a list of to-do items read from a file
    """
    with open(filename, 'r') as file:  # FileNotFoundError if file does not exist
        todos = file.readlines()
        print(f"INFO | get_todos | {todos}")
        return todos


def write_todos(todos, filename=FILEPATH):
    """
    write to-do items list to file
    """
    with open(filename, 'w') as file:
        print(f"INFO | write_todos | {todos}")
        file.writelines(todos)


if __name__ == '__main__':
    print(get_todos())