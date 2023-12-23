def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt",):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    """ Write the to-do items list in the text file """


if __name__ == "__main__":
    print("Hello")

#__name__ == "__main__" to konkretna funkcja gdzie main odnosi się do pliku w którym jest zawarta nie do pliku o nazwie main