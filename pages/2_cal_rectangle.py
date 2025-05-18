import streamlit as st

st.set_page_config(
    page_title="Rectangle",
    page_icon="😀"
)

def area_rectangle(w, h):
    return w*h


st.title("Shape Calculator")
st.write("this is the calculator app.")

if 'name' in st.session_state:
    st.write(f"hello {st.session_state.name}")

width = st.text_input("Enter width")
height = st.text_input("Enter height")
submit_btn = st.button("submit")
if submit_btn:
    st.write(area_rectangle(int(width), int(height)))