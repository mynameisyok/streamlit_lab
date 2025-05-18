import math
import streamlit as st

st.set_page_config(
    page_title="Circle",
    page_icon="😀"
)

def area_circle(r):
    return math.pi*r**2

st.title("Shape Calculator")
st.write("this is the calculator app.")

if 'name' in st.session_state:
    st.write(f"hello {st.session_state.name}")

radius = st.number_input("Enter radius ")
submit_btn = st.button("submit")
if submit_btn:
    area = area_circle(radius)
    st.write(f"the area is {area}")

# radius = st.text_input("Enter radius")
# submit_btn = st.button("submit")
# if submit_btn:
#     st.write(area_circle(int(radius)))