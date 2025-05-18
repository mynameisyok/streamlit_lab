import streamlit as st
from streamlit_apexjs import st_apexcharts

st.title("Graph from shape calculator")
st.write("📊 เปรียบเทียบการคำนวณพื้นที่ของรูปทรงต่าง ๆ")

# ข้อมูลจำลอง
shapes = ["Circle", "Rectangle", "Square", "Ellipse", "Trapezoid", "Triangle"]
area_sums = [314.16, 600.0, 225.0, 450.5, 375.0, 150.0]
calc_counts = [10, 8, 6, 7, 5, 9]
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
    col1, col2 = st.columns(2)

    with col1:
        st_apexcharts(options_donut, series_donut, 'donut', '100%', 'จำนวนการคำนวณแต่ละรูปทรง')

    with col2:
        st_apexcharts(options_bar, series_bar, 'bar', '100%', 'พื้นที่รวมของแต่ละรูปทรง')

with st.container():
    st_apexcharts(options_line, series_line, 'line', '700', 'แนวโน้มของพื้นที่แต่ละรูปทรง')
