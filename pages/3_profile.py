import streamlit as st

st.set_page_config(
    page_title="Profile",
    page_icon="😀"
)

if 'name' in st.session_state:
    st.write("Hello " + st.session_state.name)

name = st.text_input("name")
if name:
    st.session_state.name = name
    st.rerun()
