# update.py

import streamlit as st
from library_connection import execute_command, run_query

def update_data():
    st.title("✏️ Update Records")
    action = st.radio("What do you want to update?", ["Book Condition", "Friend Loan Limit", "Loan Due Date"])

    if action == "Book Condition":
        books = run_query("SELECT ISBN, Title FROM Books")
        selected = st.selectbox("Choose a Book", books["Title"])
        isbn = books[books["Title"] == selected]["ISBN"].values[0]
        new_condition = st.selectbox("New Condition", ["Excellent", "Good", "Fair", "Poor"])

        if st.button("Update Condition"):
            execute_command("UPDATE Books SET BookCondition = :cond WHERE ISBN = :isbn", {"cond": new_condition, "isbn": isbn})
            st.success(f"Condition for '{selected}' updated to {new_condition}.")

    elif action == "Friend Loan Limit":
        friends = run_query("SELECT FriendID, FName, LName FROM Friends")
        selected = st.selectbox("Choose a Friend", [f"{r.FName} {r.LName}" for _, r in friends.iterrows()])
        fid = friends[f"{friends['FName']} {friends['LName']}" == selected]["FriendID"].values[0]
        new_limit = st.number_input("New Max Loans", 1, 10, step=1)

        if st.button("Update Limit"):
            execute_command("UPDATE Friends SET MaxLoans = :ml WHERE FriendID = :fid", {"ml": new_limit, "fid": fid})
            st.success(f"Max loans for {selected} updated to {new_limit}.")

    elif action == "Loan Due Date":
        loans = run_query("""
            SELECT L.LoanID, B.Title, F.FName, F.LName, L.DueDate
            FROM Loans L
            JOIN Books B ON L.ISBN = B.ISBN
            JOIN Friends F ON L.FriendID = F.FriendID
        """)
        loans["Label"] = loans.apply(lambda r: f"{r.FName} {r.LName} - {r.Title}", axis=1)
        selected = st.selectbox("Choose a Loan", loans["Label"])
        loan_id = loans[loans["Label"] == selected]["LoanID"].values[0]
        new_due = st.date_input("New Due Date")

        if st.button("Update Due Date"):
            execute_command("UPDATE Loans SET DueDate = :d WHERE LoanID = :lid", {"d": str(new_due), "lid": loan_id})
            st.success(f"Loan due date updated to {new_due}.")
