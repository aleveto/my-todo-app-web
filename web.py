import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    """Adds a new to_do from the text input box to the list and file."""
    # st.session_state["new_todo"] holds the text from the st.text_input widget
    todo_local = st.session_state["new_todo"] #dictionary value from key "new_todo"
    #is assigned to new fxn variable todo_local
    if todo_local:  # Only add if the string is not empty
        todos.append(todo_local)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # Clear the input box after adding

def complete_todo():
    todo_local = st.session_state["complete_todo"]


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

# --- DISPLAY AND COMPLETE TO-DOS ---
# We use st.container() to group the checkboxes and keep the structure clean

with st.container():
    for index, todo in enumerate(todos):
        # Create a unique key for each checkbox
        checkbox = st.checkbox(todo, key=f"{todo}")
        # Check if the checkbox was just clicked (checked = True)
        if checkbox:
            # Remove the to_do from the list
            todos.pop(index)
            # Update the file
            functions.write_todos(todos)
            del st.session_state[todo]
            st.rerun()

st.text_input(label="Enter a Todo", placeholder="Add new Todo...",
              on_change=add_todo, key="new_todo")
