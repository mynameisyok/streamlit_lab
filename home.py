import streamlit as st

st.title("Shape calculator")
st.write("this is the calculator app.")

st.page_link("pages/1_cal_circle.py", label="Circle")
st.page_link("pages/2_cal_rectangle.py", label="Rectangle")
st.page_link("pages/3_profile.py", label="Profile")

from streamlit_chat import message

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right

# height = int(input("height :"))
# weight = int(input("weight :" ))
# radius = int(input("radius :"))

# rectangle_area = area_rectangle(weight, height)
# circle_area1 = round(area_circle(radius), 2)
# circle_area2 = f"{area_circle(radius):.2f}"

# print(f"area of rectangle is: {rectangle_area}")
# print(f"area of circle is: {circle_area2}")