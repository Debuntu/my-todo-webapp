import os

#we will remove the dependancy of the initial 'todos.txt' file by adding a condition to create it if it doesn't exist.
if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass


FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """reads a text file and returns the list of todo items"""
    with open(filepath, "r") as file_local:
        local_todos = file_local.readlines()
        return local_todos

# in the below function we have 2 args, look at their order carefully- the default arg should always be followed by the non-default arg.
def write_todos(todos_arg, filepath=FILEPATH):
    """write/overwrite a file with given todos arg and filepath"""
    with open(filepath, "w") as file_local:
        return file_local.writelines(todos_arg)

#notice that when we import this entire functions.py and execute the standard_module.py, the below line will be printed out too
print("I am outside of the functions you wrote in functions.py file")


#notice that, when you run functions.py, __name__ variable will have a value of "__main__" and when you run standard_module.py,
# it will have a value of "functions"
print(__name__)
#if we want anything from this file not to be executed when calling the functions, we can exclude them by using the following condition-
if __name__ == "__main__":
    #you have to put everything here that you don't want to be executed in the standard_module.py when calling the functions
    print(get_todos())