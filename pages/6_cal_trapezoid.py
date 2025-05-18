import streamlit as st

st.set_page_config(
    page_title = "Trapezoid",
    page_icon  = "〰️"
)

def area_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

st.title("Shape Calculator")
st.write("This is the calculator app.")

# แสดงชื่อผู้ใช้ถ้ามี
if 'name' in st.session_state:
    st.write(f"Hello {st.session_state.name}")

# ✅ สร้างค่าที่เก็บผลลัพธ์และจำนวนการคำนวณไว้ใน session_state
if 'trapezoid_calc_results' not in st.session_state:
    st.session_state.trapezoid_calc_results = []  # เก็บผลลัพธ์แต่ละครั้ง

if 'trapezoid_calc_count' not in st.session_state:
    st.session_state.trapezoid_calc_count = 0  # นับจำนวนครั้ง

# 🔘 รับ input
base1 = st.number_input("Enter base 1", min_value=0.0, step=1.0)
base2 = st.number_input("Enter base 2", min_value=0.0, step=1.0)
height = st.number_input("Enter height", min_value=0.0, step=1.0)
submit_btn = st.button("Submit")

if submit_btn:
    area = area_trapezoid(base1, base2, height)
    st.write(f"The area is {area:.2f}")

    # ⏺️ บันทึกผลลัพธ์
    st.session_state.trapezoid_calc_results.append({
        "base1": base1,
        "base2": base2,
        "height": height,
        "area": area
    })

    # ⬆️ เพิ่มจำนวนการคำนวณ
    st.session_state.trapezoid_calc_count += 1

    # แสดงสรุป
    st.success("Result saved!")

# 📋 แสดงผลทั้งหมดที่เคยคำนวณ
if st.session_state.trapezoid_calc_results:
    st.write("### 📝 ประวัติการคำนวณ:")
    for i, entry in enumerate(st.session_state.trapezoid_calc_results, 1):
        st.write(f"{i}. Base 1: {entry['base1']}, Base 2: {entry['base2']}, Height: {entry['height']} → Area: {entry['area']:.2f}")

    st.info(f"คุณคำนวณไปแล้วทั้งหมด {st.session_state.trapezoid_calc_count} ครั้ง")