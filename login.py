# login.py

import streamlit as st

def home():
    st.title("📚 Welcome to Liane's Personal Library")
    st.subheader("Helping Liane track her beloved books and generous friends.")
    st.markdown("---")

    st.image("https://upload.wikimedia.org/.../Old_books_01.jpg", use_container_width=True)

    with st.expander("📖 Why this app exists?"):
        st.markdown("""
        Liane loves books. She also loves sharing them. But... people keep forgetting to return them!
        So we built this app to help her:
        - Track who borrowed what.
        - Know which books are currently in stock.
        - Organize her personal shelf with ease.
        """)

    st.markdown("### 🔧 App Features")
    st.success("✔ Add new books, friends, and loans.")
    st.info("✔ View and filter book inventory and loan history.")
    st.warning("✔ Get reminders for upcoming return dates.")
    st.error("✔ Prevent loaning more than allowed.")

    if st.checkbox("Show developer tip"):
        st.code("This is a Streamlit app built with 💡 usability for non-coders in mind!")

    mood = st.selectbox("How are you feeling today, Liane?", ["😊 Happy", "😐 Meh", "😥 Worried"])
    if mood == "😊 Happy":
        st.balloons()
    elif mood == "😥 Worried":
        st.write("Don't worry. This app has your back. 👍")

    st.markdown("---")
    st.caption("Built with ❤️ using Python and Streamlit.")
