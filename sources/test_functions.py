#This is a unit test I am trying to create for my-todo-webapp

import unittest
import functions

class TestFunctions(unittest.TestCase):

    def setUp(self):
        #printing to check that the setUp function is getting called before running every test.
        print("SETUP CALLED...")
        #providing a given filepath
        self.FILEPATH = "demo_todos.txt"
        #providing a given todos_arg.
        self.todos_arg = "Write a unit test"

    def tearDown(self):
        # printing to check that the teardown function is getting called after running every test to set the defined values to zero for the next test.
        print("TEARDOWN CALLED...")
        self.FILEPATH = " "
        self.todos_arg = ""
    """
    test the get-todos function from the functions library.
    """
    def test_get_todos(self):
        print("TEST-1 CALLED")
        #getting the actual contents of the file
        with open(self.FILEPATH, 'r') as file:
            content_list = file.readlines()
        #passing the FILEPATH through the get_todos function to get values
        result = functions.get_todos(self.FILEPATH)
        #comparing both the values
        self.assertEqual(result, content_list)

    def test_write_todos(self):
        print("TEST-2 CALLED")
        #first getting the actual content of the test file after writing
        with open(self.FILEPATH, "w") as file:
            modified_content =  file.writelines(self.todos_arg)
        #getting the values after writing the passed argument in the write_todos function.
        result = functions.write_todos(self.todos_arg, self.FILEPATH)
        self.assertEqual(result, modified_content)


if __name__ == '__main__':
    unittest.main()