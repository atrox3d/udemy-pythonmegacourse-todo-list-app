FILEPATH = "todos.txt"


def get_todos(filename=FILEPATH):
    """
    return a list of to-do items read from a file
    """
    with open(filename, 'r') as file:  # FileNotFoundError if file does not exist
        todos = file.readlines()
        print(f"INFO | RUN | get_todos | ", list(map(str.strip, todos)))
        return todos


def write_todos(todos, filename=FILEPATH):
    """
    write to-do items list to file
    """
    print(f"INFO | RUN | write_todos | ", list(map(str.strip, todos)))
    with open(filename, 'w') as file:
        file.writelines(todos)


if __name__ == '__main__':
    print(get_todos())