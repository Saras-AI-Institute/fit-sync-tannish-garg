import streamlit as st
from modules.processor import process_data

st.set_page_config(layout="wide", page_title="FitSync")

# --- Header ---
st.markdown("""
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.2rem;">
    <span style="font-size: 28px;">🏃</span>
    <span style="font-size: 2rem; font-weight: 700; color: white;">FitSync</span>
</div>
""", unsafe_allow_html=True)

st.markdown("#### Your personal health analytics dashboard")
st.markdown("Track your **recovery**, **sleep**, and **activity** trends — all in one place. Powered by your daily health data.")

st.divider()

# --- Live Summary Metrics ---
st.markdown("### 📊 At a Glance")

df = process_data()

col1, col2, col3, col4 = st.columns(4)
col1.metric("💪 Avg Recovery Score", f"{df['Recovery_Score'].mean():.1f} / 100")
col2.metric("👟 Avg Daily Steps",     f"{df['Steps'].mean():,.0f}")
col3.metric("😴 Avg Sleep Hours",     f"{df['Sleep_Hours'].mean():.1f} hrs")
col4.metric("🔥 Avg Calories Burned", f"{df['Calories_Burned'].mean():,.0f} kcal")

st.divider()

# --- Feature Section ---
st.markdown("### 🗺️ What's Inside")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
    <div style="
        background-color: #1e2a3a;
        border-left: 4px solid #4A90D9;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
    ">
        <h4 style="color: #4A90D9; margin: 0 0 0.5rem;">📈 Dashboard</h4>
        <p style="color: #ccc; margin: 0; font-size: 0.95rem;">
            Interactive charts showing your daily recovery score, sleep hours, 
            step count, and calorie trends. Filter by last 7 days, 30 days, or all time.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <div style="
        background-color: #1e3a2a;
        border-left: 4px solid #4CAF82;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
    ">
        <h4 style="color: #4CAF82; margin: 0 0 0.5rem;">🔍 Trends & Insights</h4>
        <p style="color: #ccc; margin: 0; font-size: 0.95rem;">
            Monthly recovery patterns, distribution histograms for steps, 
            calories, sleep, and recovery — understand your long-term health trends.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- How Recovery Score Works ---
st.markdown("### 🧠 How Recovery Score Works")

st.markdown("""
The **Recovery Score** (0–100) is an ML-style composite metric calculated from your daily health signals:
""")

rc1, rc2, rc3 = st.columns(3)

with rc1:
    st.markdown("""
    <div style="background-color: #1a2535; border-radius: 8px; padding: 1rem; text-align: center;">
        <div style="font-size: 2rem;">😴</div>
        <h5 style="color: #A8DAFF; margin: 0.5rem 0 0.3rem;">Sleep Hours</h5>
        <p style="color: #aaa; font-size: 0.85rem; margin: 0;">
            ≥7 hrs → +20 pts<br>
            6–7 hrs → +10 pts<br>
            &lt;6 hrs → −20 pts
        </p>
    </div>
    """, unsafe_allow_html=True)

with rc2:
    st.markdown("""
    <div style="background-color: #1a2535; border-radius: 8px; padding: 1rem; text-align: center;">
        <div style="font-size: 2rem;">❤️</div>
        <h5 style="color: #FFB3B3; margin: 0.5rem 0 0.3rem;">Resting Heart Rate</h5>
        <p style="color: #aaa; font-size: 0.85rem; margin: 0;">
            Lower BPM = higher score<br>
            Deviation from 68 bpm<br>
            adjusts score up/down
        </p>
    </div>
    """, unsafe_allow_html=True)

with rc3:
    st.markdown("""
    <div style="background-color: #1a2535; border-radius: 8px; padding: 1rem; text-align: center;">
        <div style="font-size: 2rem;">👟</div>
        <h5 style="color: #B3FFD1; margin: 0.5rem 0 0.3rem;">Daily Steps</h5>
        <p style="color: #aaa; font-size: 0.85rem; margin: 0;">
            &gt;14k steps → −10 pts<br>
            &lt;4k steps → −10 pts<br>
            Optimal zone: 4k–14k
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- Quick Tip ---
st.info("💡 **Tip:** Use the **sidebar** on the left to navigate to the Dashboard or Trends page.")

st.caption("Made with ❤️ using Streamlit · FitSync v1.0")