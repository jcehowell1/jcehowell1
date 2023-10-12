FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a text file and Return the items in the to-do list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        # closing is not nesssesary in 'with-context'
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do to list in the todos file text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")