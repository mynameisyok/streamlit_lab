import streamlit as st
from streamlit_apexjs import st_apexcharts

st.set_page_config(
    page_title="graph",
    page_icon="📊"
)

# ✅ ย่อด้วย loop
for shape in ["circle", "rectangle", "ellipse", "square", "trapezoid", "triangle"]:
    key = f"{shape}_calc_results"
    if key not in st.session_state:
        st.session_state[key] = []

for shape in ["circle", "rectangle", "ellipse", "square", "trapezoid", "triangle"]:
    key = f"{shape}_calc_count"
    if key not in st.session_state:
        st.session_state[key] = 0


st.title("Graph from shape calculator")
st.write("📊 เปรียบเทียบการคำนวณพื้นที่ของรูปทรงต่าง ๆ")
# st.write(st.session_state.circle_calc_results)

area_sums_rounded = {}

for shape in ["circle", "rectangle", "ellipse", "square", "trapezoid", "triangle"]:
    key = f"{shape}_calc_results"
    total = sum(entry['area'] for entry in st.session_state[key])
    area_sums_rounded[shape] = round(total, 2)
# st.write(st.session_state[key])

count_circle = st.session_state.circle_calc_count
count_rectangle = st.session_state.rectangle_calc_count
countellipse = st.session_state.ellipse_calc_count
coutsquare = st.session_state.square_calc_count
counttrapezoid =st.session_state.trapezoid_calc_count
counttriangle = st.session_state.triangle_calc_count

# ข้อมูลจำลอง
shapes = ["Circle", "Rectangle", "Square", "Ellipse", "Trapezoid", "Triangle"]
# ถ้าอยากได้ลิสต์สำหรับกราฟ bar
area_sums = [
    area_sums_rounded["circle"],
    area_sums_rounded["rectangle"],
    area_sums_rounded["square"],
    area_sums_rounded["ellipse"],
    area_sums_rounded["trapezoid"],
    area_sums_rounded["triangle"]
]
calc_counts = [count_circle, count_rectangle, countellipse, coutsquare, counttrapezoid, counttriangle]
colors = ["#FFCE56", "#FF9F40", "#FF6384", "#4BC0C0", "#36A2EB", "#9966FF"]

# 🔘 Donut Chart
options_donut = {
    "chart": {"id": "calc_count", "toolbar": {"show": False}},
    "labels": shapes,
    "legend": {"show": True, "position": "bottom"},
    "colors": colors,
    "tooltip": {
        "theme": "dark",
        "style": {
            "fontSize": "14px"
        }
    }
}
series_donut = calc_counts

# 📊 Bar Chart
options_bar = {
    "chart": {"id": "area_chart", "toolbar": {"show": False}},
    "xaxis": {"categories": shapes},
    "legend": {"show": False},
    "plotOptions": {
        "bar": {
            "dataLabels": {
                "position": "top"
            }
        }
    },
    "dataLabels": {
        "enabled": True,
        "style": {
            "colors": ["red"]
        },
        "background": {
            "enabled": True,
            "foreColor": "white",
            "color": "red",
            "borderRadius": 2,
            "padding": 4
        }
    },
    "tooltip": {
        "theme": "dark",
        "style": {
            "fontSize": "14px"
        }
    },
    "states": {
        "hover": {
            "filter": {
                "type": "darken",
                "value": 0.8
            }
        }
    }
}
series_bar = [{
    "name": "Total Area",
    "data": area_sums
}]

# 📈 Line Chart
options_line = {
    "chart": {"id": "line_chart", "toolbar": {"show": False}},
    "xaxis": {"categories": shapes},
    "legend": {"show": False},
    "dataLabels": {
        "enabled": True,
        "style": {
            "colors": ["red"]
        },
        "background": {
            "enabled": True,
            "foreColor": "white",
            "color": "red",
            "borderRadius": 2,
            "padding": 4
        }
    },
    "tooltip": {
        "theme": "dark",
        "style": {
            "fontSize": "14px"
        }
    },
    "stroke": {
        "width": 3
    },
    "markers": {
        "size": 6,
        "hover": {
            "size": 8
        }
    }
}
series_line = [{
    "name": "Total Area",
    "data": area_sums
}]

# 📌 แสดงผลกราฟ
with st.container():
    # col1, col2 = st.columns(2)

    # with col1:
        st_apexcharts(options_donut, series_donut, 'donut', '700', 'จำนวนการคำนวณแต่ละรูปทรง')

    # with col2:
    #     st_apexcharts(options_bar, series_bar, 'bar', '100%', 'พื้นที่รวมของแต่ละรูปทรง')


with st.container():
    st_apexcharts(options_bar, series_bar, 'bar', '700', 'พื้นที่รวมของแต่ละรูปทรง')

with st.container():
    st_apexcharts(options_line, series_line, 'line', '700', 'แนวโน้มของพื้นที่แต่ละรูปทรง')
