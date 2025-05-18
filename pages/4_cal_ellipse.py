import streamlit as st
import math

st.set_page_config(
    page_title="Ellipse",
    page_icon="🥚"
)

def area_ellipse(a, b):
    return math.pi * a * b

st.title("Shape Calculator")
st.write("Calculate the area of an ellipse.")

if 'name' in st.session_state:
    st.write(f"hello {st.session_state.name}")

semi_major_axis = st.number_input("Enter semi-major axis (a)")
semi_minor_axis = st.number_input("Enter semi-minor axis (b)")
submit_btn = st.button("Calculate Area")
if submit_btn:
    area = area_ellipse(semi_major_axis, semi_minor_axis)
    st.write(f"The area of the ellipse is {area}")