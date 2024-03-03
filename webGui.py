import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    # print(todo)
    todos.append(todo)
    functions.set_todos(todos)
    st.session_state['new_todo'] = ''


st.title('My ToDo List')
st.subheader('This is My todo App.')
st.write('This app is to increase your productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.rerun()#st.experimental_rerun()


st.text_input(label='Enter ToDo:', placeholder='Add a new todo....', on_change=add_todo,
              key='new_todo')

# st.session_state
