FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of todos from a file. """
    with open(filepath, "r") as file_read:
        todos_local = file_read.readlines()
    # 1. Strip the newline from every item
    todos_local = [item.strip("\n") for item in todos_local]
    # 2. Add a filter: only keep the item if it's not an empty string
    todos_local = [item for item in todos_local if item != ""]
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a list of todos to a text file. No Return output. """
    todos_with_newlines = [item + "\n" for item in todos_arg]
    with open(filepath, "w") as file_write:
        file_write.writelines(todos_with_newlines)
#No need to return anything because this is more of a procedure.

#the lines below are only executed when this function.py file is
#executed directly. It is not executed when running cli.py
#if __name__ == "__main__":
 #   print("Hello")
  #  print(get_todos())