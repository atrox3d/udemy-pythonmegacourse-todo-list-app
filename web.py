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


def check(todo):
    print("check", todo, st.session_state[todo])
    if st.session_state[todo]:
        print(f"remove '{todo}'")
        todos.remove(todo)
        print(todos)
        functions.write_todos(todos)


for todo in todos:
    st.checkbox(
        label=todo,
        key=todo,
        on_change=check,
        args=(todo,)
    )

# https://github.com/streamlit/streamlit/issues/2209
st.session_state.new_todo = ""
st.text_input(
    label="Enter a TODO:",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo",

)

st.session_state
"INFO | RUN | end of script"
print("INFO | RUN | end of script")
