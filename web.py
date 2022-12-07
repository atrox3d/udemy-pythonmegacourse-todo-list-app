import streamlit as st
import functions

todos = functions.get_todos()


st.title("My TODO App")
st.subheader("this is my todo app")
st.write("this app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a TODO:", placeholder="Add new todo...")
