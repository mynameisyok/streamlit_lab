import streamlit as st

st.set_page_config(
    page_title="Triangle",
    page_icon="📐"
)

def area_triangle(base, height):
    return 0.5 * base * height

st.title("Shape Calculator")
st.write("Calculate the area of a triangle.")

if 'name' in st.session_state:
    st.write(f"hello {st.session_state.name}")

base = st.number_input("Enter base")
height = st.number_input("Enter height")
submit_btn = st.button("Calculate Area")
if submit_btn:
    area = area_triangle(base, height)
    st.write(f"The area of the triangle is {area}")