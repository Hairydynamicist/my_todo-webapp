import streamlit as st
import modules.functions
todos = modules.functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    modules.functions.write_todos(todos)

st.title("My ToDo App")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        modules.functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="enter a todo:", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
