import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    f"INFO | RUN | add_todo() | {new_todo}"
    print(f"INFO | RUN | add_todo() | {new_todo}")
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My TODO App")
st.subheader("this is my todo app")
st.write("this app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(
    label="Enter a TODO:",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo"
)

st.session_state
"INFO | RUN | end of script"
print("INFO | RUN | end of script")
