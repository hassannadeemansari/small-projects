import streamlit as st

# 🔵 Page configuration
st.set_page_config(page_title="Temperature Converter", page_icon="🌡️", layout="centered")

# 🌟 Custom CSS for background and card styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .main {
            background-color: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #3366cc;
        }
    </style>
""", unsafe_allow_html=True)

# 🟩 Temperature class
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

# 📦 Main layout container
with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)

    st.title("🌡️ Temperature Converter")
    st.write("Convert temperature from **Celsius** to 🔥 Fahrenheit and 🧊 Kelvin instantly.")

    # 🎛️ Input
    celsius = st.number_input("🌡️ Enter temperature in Celsius:", value=0.0, step=0.1, format="%.1f")

    # 📐 Conversion
    temp = Temperature(celsius)
    fahrenheit = temp.to_fahrenheit()
    kelvin = temp.to_kelvin()

    # 🧊 Output layout
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="🔥 Fahrenheit", value=f"{fahrenheit:.2f} °F")

    with col2:
        st.metric(label="🧊 Kelvin", value=f"{kelvin:.2f} K")

    st.markdown("</div>", unsafe_allow_html=True)
