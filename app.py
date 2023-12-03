import streamlit as st

placeholder = st.empty()

with placeholder.container():
    with st.form("my_form"):
        st.write("Inside the form")
        my_number = st.slider("Pick a number", 1, 10)
        my_color = st.selectbox(
            "Pick a color", ["red", "orange", "green", "blue", "violet"]
        )
        submit = st.form_submit_button("Submit my picks")
    if submit:
        placeholder.text("sfs")
