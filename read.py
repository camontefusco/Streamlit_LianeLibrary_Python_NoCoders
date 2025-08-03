# read.py

import streamlit as st
from library_connection import run_query
import pandas as pd

def view_data():
    st.title("👁 View Library Data")
    st.markdown("Choose a table to view or filter.")

    table = st.selectbox("Select Table", ["Books", "Friends", "Loans"])

    if table == "Books":
        books = run_query("SELECT * FROM Books")
        st.subheader("📘 All Books")
        
        with st.expander("🔍 Filter Options"):
            genre = st.multiselect("Filter by Genre", books["Genre"].unique())
            condition = st.multiselect("Filter by Condition", books["BookCondition"].unique())
            stock = st.checkbox("Show Only In-Stock Books", value=True)

            if genre:
                books = books[books["Genre"].isin(genre)]
            if condition:
                books = books[books["BookCondition"].isin(condition)]
            if stock:
                books = books[books["IsInStock"] == 1]

        st.dataframe(books, use_container_width=True)

    elif table == "Friends":
        friends = run_query("SELECT * FROM Friends")
        st.subheader("👥 Friends")
        st.dataframe(friends, use_container_width=True)

    elif table == "Loans":
        loans = run_query("""
            SELECT L.LoanID, L.BorrowDate, L.DueDate, L.ReturnReminder,
                   B.Title AS Book, F.FName AS FirstName, F.LName AS LastName
            FROM Loans L
            JOIN Books B ON L.ISBN = B.ISBN
            JOIN Friends F ON L.FriendID = F.FriendID
        """)
        st.subheader("🔁 Loans")

        with st.expander("🔍 Filter by Date"):
            from_date = st.date_input("From", pd.to_datetime("2025-07-01"))
            to_date = st.date_input("To", pd.to_datetime("2025-08-31"))
            loans["BorrowDate"] = pd.to_datetime(loans["BorrowDate"])
            loans = loans[(loans["BorrowDate"] >= pd.to_datetime(from_date)) & (loans["BorrowDate"] <= pd.to_datetime(to_date))]

        st.dataframe(loans, use_container_width=True)
