import math
import streamlit as st

st.set_page_config(
    page_title="Rectangle"
)

def area_rectangle(w, h):
    return w*h


st.title("Shape Calculator")
st.write("this is the calculator app.")

width = st.text_input("Enter width")
height = st.text_input("Enter height")
submit_btn = st.button("submit")
if submit_btn:
    st.write(area_rectangle(int(width), int(height)))