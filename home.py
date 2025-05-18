import math
import streamlit as st

def area_rectangle(w, h):
    return w*h

def area_circle(r):
    return math.pi*r**2



st.title("Homepage")
st.write("this is the calculator app.")

radius = st.text_input("Enter radius")
submit_btn = st.button("submit")
if submit_btn:
    st.write(area_circle(int(radius)))

# height = int(input("height :"))
# weight = int(input("weight :" ))
# radius = int(input("radius :"))

# rectangle_area = area_rectangle(weight, height)
# circle_area1 = round(area_circle(radius), 2)
# circle_area2 = f"{area_circle(radius):.2f}"

# print(f"area of rectangle is: {rectangle_area}")
# print(f"area of circle is: {circle_area2}")