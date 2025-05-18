import streamlit as st

st.set_page_config(
    page_title="Square",
    page_icon="⏹️"
)

def area_square(side):
    return side * side

st.title("Shape Calculator")
st.write("Calculate the area of a square.")

if 'name' in st.session_state:
    st.write(f"hello {st.session_state.name}")

side = st.number_input("Enter side length")
submit_btn = st.button("Calculate Area")
if submit_btn:
    area = area_square(side)
    st.write(f"The area of the square is {area}")