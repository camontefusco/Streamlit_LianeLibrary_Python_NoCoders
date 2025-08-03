# create.py

import streamlit as st
from library_connection import execute_command

def add_data():
    st.title("➕ Add New Records")
    st.markdown("Use the sections below to add books, friends, or loan records.")

    menu = st.radio("Choose a category:", ["📘 Add Book", "👤 Add Friend", "🔁 Add Loan"])

    if menu == "📘 Add Book":
        with st.form("add_book_form"):
            isbn = st.text_input("ISBN (e.g., 978-0-452-28423-4)")
            title = st.text_input("Title")
            author = st.text_input("Author")
            genre = st.text_input("Genre")
            condition = st.selectbox("Book Condition", ["Excellent", "Good", "Fair", "Poor"])
            shelf = st.text_input("Shelf Location (e.g., A1)")
            row = st.number_input("Shelf Row", min_value=1, step=1)

            submitted = st.form_submit_button("Add Book")
            if submitted:
                query = """
                    INSERT INTO Books (ISBN, Title, Author, Genre, BookCondition, IsInStock, ShelfLocation, ShelfRow)
                    VALUES (:isbn, :title, :author, :genre, :condition, 1, :shelf, :row)
                """
                execute_command(query, {
                    "isbn": isbn,
                    "title": title,
                    "author": author,
                    "genre": genre,
                    "condition": condition,
                    "shelf": shelf,
                    "row": row
                })
                st.success(f"Book '{title}' added successfully!")

    elif menu == "👤 Add Friend":
        with st.form("add_friend_form"):
            fname = st.text_input("First Name")
            lname = st.text_input("Last Name")
            max_loans = st.slider("Max Number of Loans", 1, 10, 3)

            submitted = st.form_submit_button("Add Friend")
            if submitted:
                query = """
                    INSERT INTO Friends (FName, LName, MaxLoans)
                    VALUES (:fname, :lname, :max_loans)
                """
                execute_command(query, {
                    "fname": fname,
                    "lname": lname,
                    "max_loans": max_loans
                })
                st.success(f"Friend '{fname} {lname}' added successfully!")

    elif menu == "🔁 Add Loan":
        with st.form("add_loan_form"):
            isbn = st.text_input("ISBN")
            friend_id = st.number_input("Friend ID", min_value=1, step=1)
            borrow_date = st.date_input("Borrow Date")
            due_date = st.date_input("Due Date")
            reminder = st.date_input("Return Reminder Date")

            submitted = st.form_submit_button("Add Loan")
            if submitted:
                query = """
                    INSERT INTO Loans (BorrowDate, DueDate, ReturnReminder, ISBN, FriendID)
                    VALUES (:borrow, :due, :reminder, :isbn, :friend)
                """
                execute_command(query, {
                    "borrow": str(borrow_date),
                    "due": str(due_date),
                    "reminder": str(reminder),
                    "isbn": isbn,
                    "friend": friend_id
                })

                execute_command("UPDATE Books SET IsInStock = 0 WHERE ISBN = :isbn", {"isbn": isbn})
                execute_command("UPDATE Friends SET MaxLoans = MaxLoans - 1 WHERE FriendID = :friend", {"friend": friend_id})

                st.success(f"Loan added! Book {isbn} borrowed by Friend ID {friend_id}.")

