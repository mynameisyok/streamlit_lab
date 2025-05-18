import streamlit as st

st.set_page_config(
    page_title="Rectangle",
    page_icon="🟥"
)

def area_rectangle(w, h):
    return w * h

st.title("Shape Calculator")
st.write("This is the calculator app.")

# แสดงชื่อผู้ใช้ถ้ามี
if 'name' in st.session_state:
    st.write(f"Hello {st.session_state.name}")

# ✅ สร้างค่าที่เก็บผลลัพธ์และจำนวนการคำนวณไว้ใน session_state
if 'rectangle_calc_results' not in st.session_state:
    st.session_state.rectangle_calc_results = []  # เก็บผลลัพธ์แต่ละครั้ง

if 'rectangle_calc_count' not in st.session_state:
    st.session_state.rectangle_calc_count = 0  # นับจำนวนครั้ง

# 🔘 รับ input
width = st.number_input("Enter width", min_value=0.0, step=1.0)
height = st.number_input("Enter height", min_value=0.0, step=1.0)
submit_btn = st.button("Submit")

if submit_btn:
    area = area_rectangle(width, height)
    st.write(f"The area is {area:.2f}")

    # ⏺️ บันทึกผลลัพธ์
    st.session_state.rectangle_calc_results.append({
        "width": width,
        "height": height,
        "area": area
    })

    # ⬆️ เพิ่มจำนวนการคำนวณ
    st.session_state.rectangle_calc_count += 1

    # แสดงสรุป
    st.success("Result saved!")

# 📋 แสดงผลทั้งหมดที่เคยคำนวณ
if st.session_state.rectangle_calc_results:
    st.write("### 📝 ประวัติการคำนวณ:")
    for i, entry in enumerate(st.session_state.rectangle_calc_results, 1):
        st.write(f"{i}. Width: {entry['width']}, Height: {entry['height']} → Area: {entry['area']:.2f}")

    st.info(f"คุณคำนวณไปแล้วทั้งหมด {st.session_state.rectangle_calc_count} ครั้ง")