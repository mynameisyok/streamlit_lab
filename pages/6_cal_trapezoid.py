import streamlit as st

st.set_page_config(
    page_title="Trapezoid",
    page_icon=" trapezoid"
)

def area_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

st.title("Shape Calculator")
st.write("Calculate the area of a trapezoid.")

if 'name' in st.session_state:
    st.write(f"hello {st.session_state.name}")

base1 = st.number_input("Enter base 1")
base2 = st.number_input("Enter base 2")
height = st.number_input("Enter height")
submit_btn = st.button("Calculate Area")
if submit_btn:
    area = area_trapezoid(base1, base2, height)
    st.write(f"The area of the trapezoid is {area}")