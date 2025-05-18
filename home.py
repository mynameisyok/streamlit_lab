import streamlit as st

st.set_page_config(
    page_title="้home",
    page_icon="home"
)

st.title("Shape calculator")
st.write("this is the calculator app.")

st.page_link("pages/1_profile.py", label="Profile")
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/2_cal_circle.py", label="Circle", icon="🔵")
    st.page_link("pages/3_cal_rectangle.py", label="Rectangle", icon="🟥")

with col2:
    st.page_link("pages/4_cal_ellipse.py", label="Ellipse", icon="🥚")
    st.page_link("pages/5_cal_square.py", label="Square", icon="🟩")

with col3:
    st.page_link("pages/6_cal_trapezoid.py", label="Trapezoid", icon="〰️")
    st.page_link("pages/7_cal_triangle.py", label="Triangle", icon="🔺")

# height = int(input("height :"))
# weight = int(input("weight :" ))
# radius = int(input("radius :"))

# rectangle_area = area_rectangle(weight, height)
# circle_area1 = round(area_circle(radius), 2)
# circle_area2 = f"{area_circle(radius):.2f}"

# print(f"area of rectangle is: {rectangle_area}")
# print(f"area of circle is: {circle_area2}")