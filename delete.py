# delete.py

import streamlit as st
from library_connection import run_query, execute_command

def delete_data():
    st.title("🗑️ Delete Records")
    option = st.radio("Choose a category to delete from:", ["Books", "Friends", "Loans"])

    if option == "Books":
        books = run_query("SELECT ISBN, Title FROM Books")
        if books.empty:
            st.info("No books available to delete.")
            return

        selected = st.selectbox("Select Book to Delete", books["Title"])
        isbn = books[books["Title"] == selected]["ISBN"].values[0]

        if st.button("Delete Book"):
            execute_command("DELETE FROM Books WHERE ISBN = :isbn", {"isbn": isbn})
            st.success(f"Book '{selected}' deleted successfully.")

    elif option == "Friends":
        friends = run_query("SELECT FriendID, FName, LName FROM Friends")
        if friends.empty:
            st.info("No friends available to delete.")
            return

        friends["FullName"] = friends["FName"] + " " + friends["LName"]
        selected = st.selectbox("Select Friend", friends["FullName"])
        friend_id = friends[friends["FullName"] == selected]["FriendID"].values[0]

        if st.button("Delete Friend"):
            execute_command("DELETE FROM Friends WHERE FriendID = :fid", {"fid": friend_id})
            st.success(f"Friend '{selected}' deleted successfully.")

    elif option == "Loans":
        loans = run_query("""
            SELECT L.LoanID, B.Title, F.FName, F.LName
            FROM Loans L
            JOIN Books B ON L.ISBN = B.ISBN
            JOIN Friends F ON L.FriendID = F.FriendID
        """)
        if loans.empty:
            st.info("No loans to delete.")
            return

        loans["Label"] = loans["FName"] + " " + loans["LName"] + " - " + loans["Title"]
        selected = st.selectbox("Select Loan to Delete", loans["Label"])
        loan_id = loans[loans["Label"] == selected]["LoanID"].values[0]

        if st.button("Delete Loan"):
            execute_command("DELETE FROM Loans WHERE LoanID = :lid", {"lid": loan_id})
            st.success(f"Loan record '{selected}' deleted successfully.")
