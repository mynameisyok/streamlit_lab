import math
import streamlit as st

st.set_page_config(
    page_title="Circle"
)

def area_circle(r):
    return math.pi*r**2

st.title("Shape Calculator")
st.write("this is the calculator app.")

radius = st.text_input("Enter radius")
submit_btn = st.button("submit")
if submit_btn:
    st.write(area_circle(int(radius)))