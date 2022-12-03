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


