import streamlit as st
import functions


def log(*items):
    message = f"INFO | RUN | " + " | ".join(map(str, items))
    print(message)
    st.messages = getattr(st, "messages", [])
    st.messages.append(message)


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    log("add_todo", new_todo.strip())
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state.new_todo = ""


log("--------------------------")
log("start of script")
log("--------------------------")
todos = functions.get_todos()

log("write headers")
st.title("My TODO App")
st.subheader("this is my todo app")
st.write("this app is to increase your productivity")

log("create checkboxes")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        log("removing checkbox", index, checkbox, todo.strip())
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

log("create input")
# st.session_state.new_todo = ""
st.text_input(
    label="Enter a TODO:",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo",
    value=""
)


# st.session_state.eos = True
"session_state", st.session_state
log("--------------------------")
log("end of script")
log("--------------------------")
# for message in st.messages:
st.code("\n".join(st.messages))
st.messages = []
