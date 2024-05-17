#make sure streamlit library package is installed first.
#in this program we will now build the same my to do app using web gui to run on browser.
#to run this webapp run the following command from the current dir or mention the right path of the web.py file from the terminal.
     #streamlit run web.py

#note that streamlit runs on port 8501 port.

import streamlit as st
import functions
st.title("My To Do")
st.subheader("This is my to do web app")
st.write("This app is to increase your productivity")

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

#in every iteration, checkbox will get a key, so to keep it unique, we named it as the todo,
# as todo will be different in every iteration
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]

#we are adding a call fucntion here to handle adding new todo, we defined the function add_todo earlier.
st.text_input(label="", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")
