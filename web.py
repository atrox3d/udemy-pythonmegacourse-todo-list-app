import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    print(f"INFO | RUN | add_todo() | {new_todo}")
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My TODO App")
st.subheader("this is my todo app")
st.write("this app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        message = f"INFO | removing checkbox | {index} {checkbox} '{todo}'"
        print(message)
        todos.pop(index)
        print(f"INFO | todos.pop({index}) | ", todos)
        functions.write_todos(todos)
        del st.session_state[todo]
        print(st.session_state)
        st.experimental_rerun()

st.session_state["new_todo"] = ""
st.text_input(
    label="Enter a TODO:",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo"
)


"session_state", st.session_state
print("INFO | RUN | end of script")
print("--------------------------")
