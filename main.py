# main.py
import streamlit as st
from streamlit_option_menu import option_menu

# Multipage import
import login
import create
import read
import update
import delete

st.set_page_config(page_title="Liane's Library", layout="wide")

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="📚 Liane's Library",
        options=["Home", "Add Data", "View Data", "Update", "Delete"],
        icons=["house", "plus-circle", "eye", "pencil-square", "trash"],
        menu_icon="book",
        default_index=0
    )

if selected == "Home":
    login.home()
elif selected == "Add Data":
    create.add_data()
elif selected == "View Data":
    read.view_data()
elif selected == "Update":
    update.update_data()
elif selected == "Delete":
    delete.delete_data()
