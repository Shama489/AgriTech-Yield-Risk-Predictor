import streamlit as st
import joblib
import numpy as np
import os
import streamlit.components.v1 as components
import plotly.express as px
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="🌍 AgriTech Digital Twin",
    layout="wide",
    page_icon="🌱"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown(
    """
    <style>
    /* Main background color */
    .stApp {
        background-color: #f1f8e9; /* light earthy green */
        color: #0d3b66; /* default text color */
    }
    
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #c8e6c9 !important;
        color: #004d40 !important;
    }
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
        color: #004d40 !important;
        font-weight: bold;
    }
    
    /* Number input boxes */
    input[type="number"] {
        background-color: #004d40 !important;
        color: #ffffff !important;
        border-radius: 5px;
        padding: 5px;
    }

    /* Metric cards (Recommended Crop / Predicted Yield) */
    .stMetric > div {
        background-color: rgba(0, 77, 64, 0.85) !important;
        border-radius: 15px !important;
        padding: 10px !important;
        font-weight: bold;
    }
    /* Metric labels */
    .stMetric .css-1gk6nbg {
        color: #ffd700 !important;  /* golden/yellow label text */
        font-weight: bold;
    }
    /* Metric values */
    .stMetric .css-1v3fvcr {
        color: #ffffff !important;  /* white value text */
        font-size: 28px;
        font-weight: bold;
    }

    /* Button style */
    div.stButton > button {
        background-color: #26a69a;
        color: white;
        height: 3em;
        width: 100%;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #00796b;
        color: white;
    }

    /* Expander header */
    .streamlit-expanderHeader {
        font-weight: bold;
        color: #004d40;
    }

    /* Slider style */
    div[data-baseweb="slider"] > div > div > div > div {
        background: #004d40 !important;
    }

    /* Plotly dark chart text override */
    .plotly .main-svg text {
        fill: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# MODEL PATHS
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
crop_model_path = os.path.join(BASE_DIR, "backend", "models", "recommendation_model.pkl")
yield_model_path = os.path.join(BASE_DIR, "backend", "models", "yield_model.pkl")

# =========================
# LOAD MODELS
# =========================
@st.cache_resource
def load_models():
    crop_model = joblib.load(crop_model_path)
    yield_model = joblib.load(yield_model_path)
    return crop_model, yield_model

crop_model, yield_model = load_models()

# =========================
# SIDEBAR INPUTS
# =========================
st.sidebar.header("Enter Field Data 🌱", anchor=None)

with st.sidebar.expander("Soil Nutrients"):
    nitrogen = st.slider("Nitrogen (N)", 0, 200, 50)
    phosphorus = st.slider("Phosphorus (P)", 0, 200, 50)
    potassium = st.slider("Potassium (K)", 0, 200, 50)

with st.sidebar.expander("Environmental Factors"):
    temp = st.number_input("Temperature (°C)", value=25.0, step=0.1)
    hum = st.number_input("Humidity (%)", value=50.0, step=0.1)
    ph = st.number_input("pH Value", value=6.5, step=0.1)
    rain = st.number_input("Rainfall (mm)", value=100.0, step=0.1)

predict_btn = st.sidebar.button("Predict 🌾")

# =========================
# LAYOUT: MAP + RESULTS
# =========================
col1, col2 = st.columns([2, 1])

# -------------------------
# DIGITAL TWIN MAP
# -------------------------
with col1:
    st.subheader("Digital Twin Map 🌐", anchor=None)
    try:
        with open("cesium_map.html", "r") as f:
            html_data = f.read()
        components.html(html_data, height=600)
    except FileNotFoundError:
        st.error("Cesium map file not found!")

# -------------------------
# PREDICTION RESULTS (ENHANCED)
# -------------------------
with col2:
    st.subheader("Prediction Results 📊")

    if predict_btn:
        input_data = np.array([[nitrogen, phosphorus, potassium, temp, hum, ph, rain]])
        crop = crop_model.predict(input_data)[0]
        try:
            yield_pred = yield_model.predict([[0]])[0]
        except:
            yield_pred = "N/A"

        # -------------------------
        # CUSTOM CARDS
        # -------------------------
        st.markdown("""
        <style>
        .prediction-card {
            background-color: rgba(0, 77, 64, 0.85);
            color: white;
            border-radius: 15px;
            padding: 20px;
            font-family: 'Arial', sans-serif;
            margin-bottom: 15px;
            box-shadow: 4px 4px 12px rgba(0,0,0,0.3);
            text-align: center;
        }
        .prediction-card h3 {
            margin: 0;
            font-size: 20px;
            color: #ffd700; /* golden label */
        }
        .prediction-card p {
            margin: 5px 0 0;
            font-size: 28px;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)

        # Recommended Crop Card
        st.markdown(f"""
        <div class="prediction-card">
            <h3>🌱 Recommended Crop</h3>
            <p>{crop}</p>
        </div>
        """, unsafe_allow_html=True)

        # Predicted Yield Card
        st.markdown(f"""
        <div class="prediction-card">
            <h3>🌾 Predicted Yield</h3>
            <p>{yield_pred}</p>
        </div>
        """, unsafe_allow_html=True)

        # -------------------------
        # Soil & Environment Visualization
        # -------------------------
        st.markdown("### Soil & Environmental Factors")
        data = pd.DataFrame({
            "Factors": ["Nitrogen", "Phosphorus", "Potassium", "Temperature", "Humidity", "pH", "Rainfall"],
            "Values": [nitrogen, phosphorus, potassium, temp, hum, ph, rain]
        })
        fig = px.bar(
            data,
            x="Factors",
            y="Values",
            color="Values",
            color_continuous_scale=px.colors.sequential.Teal,
            template="plotly_dark"
        )
        fig.update_layout(
            plot_bgcolor="rgba(0, 77, 64, 0.7)",  
            paper_bgcolor="rgba(0, 77, 64, 0.7)",
            font_color="white",
            yaxis=dict(title_font=dict(color="white"), tickfont=dict(color="white")),
            xaxis=dict(title_font=dict(color="white"), tickfont=dict(color="white"))
        )
        st.plotly_chart(fig, use_container_width=True)
        
# =========================
# INTERACTIVE TIPS
# =========================
with st.expander("💡 Tips for Optimal Yield"):
    st.markdown("""
    - Maintain NPK levels according to crop requirements.
    - Monitor soil pH for nutrient absorption.
    - Ensure adequate irrigation based on rainfall data.
    - Track environmental factors daily for better predictions.
    """)