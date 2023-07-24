FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Opens an existing todos text file and return a
    list of todos"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

#print(help(get_todos))
def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
#the below lines are only run when functions.py is run directly
#not from a function call
if __name__ ==  "__main__":
    print('hello from functions')