import streamlit as st
from modules.processor import process_data

st.set_page_config(layout="wide", page_title="FitSync", page_icon="🏃")

df = process_data()
avg_recovery = df['Recovery_Score'].mean()
avg_sleep    = df['Sleep_Hours'].mean()
avg_steps    = df['Steps'].mean()
avg_calories = df['Calories_Burned'].mean()
avg_hr       = df['Heart_Rate_bpm'].mean()

health_score = round(
    (avg_recovery / 100) * 40 +
    (min(avg_sleep, 9) / 9) * 30 +
    (min(avg_steps, 10000) / 10000) * 30
)
if health_score >= 75:
    hs_color, hs_label = "#22c55e", "Excellent"
elif health_score >= 55:
    hs_color, hs_label = "#f59e0b", "Good"
else:
    hs_color, hs_label = "#ef4444", "Needs Attention"

# ══════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="display:flex; align-items:center; justify-content:space-between;
            padding:1.2rem 0 0.6rem;">
    <div style="display:flex; align-items:center; gap:16px;">
        <div style="width:52px; height:52px;
                    background:linear-gradient(135deg, #3b82f6 0%, #22c55e 100%);
                    border-radius:14px; display:flex; align-items:center;
                    justify-content:center; font-size:1.7rem;
                    box-shadow: 0 0 20px #3b82f630;">🏃</div>
        <div>
            <div style="font-size:2.2rem; font-weight:900; letter-spacing:-1.5px;
                        background:linear-gradient(90deg, #60a5fa 0%, #34d399 100%);
                        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                        line-height:1.1;">FitSync</div>
            <div style="font-size:0.8rem; color:#4b5563; font-weight:500;
                        letter-spacing:0.05em; margin-top:1px;">
                PERSONAL HEALTH ANALYTICS
            </div>
        </div>
    </div>
    <div style="display:flex; align-items:center; gap:12px;">
        <div style="background:#111827; border:1px solid #1f2937;
                    border-radius:12px; padding:0.7rem 1.3rem; text-align:center;">
            <div style="font-size:0.65rem; color:#4b5563; font-weight:700;
                        letter-spacing:0.1em; margin-bottom:3px;">HEALTH SCORE</div>
            <div style="font-size:2rem; font-weight:900; color:{hs_color};
                        line-height:1; letter-spacing:-1px;">{health_score}</div>
            <div style="font-size:0.7rem; color:{hs_color}; font-weight:600;
                        margin-top:2px; opacity:0.85;">{hs_label}</div>
        </div>
        <div style="background:#111827; border:1px solid #1f2937;
                    border-radius:10px; padding:6px 14px;">
            <span style="background:linear-gradient(90deg,#3b82f6,#22c55e);
                         -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                         font-size:0.78rem; font-weight:700;">v1.0</span>
        </div>
    </div>
</div>
<div style="width:100%; height:1px;
            background:linear-gradient(90deg,#3b82f620,#22c55e40,#3b82f620);
            margin-bottom:0.5rem;"></div>
<p style="color:#4b5563; font-size:0.88rem; margin:0.5rem 0 0;">
    Track your recovery, sleep, and activity — understand what your body is telling you.
</p>
""", unsafe_allow_html=True)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# AT A GLANCE
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="font-size:0.7rem; font-weight:700; color:#4b5563;
            letter-spacing:0.12em; margin-bottom:12px;">AT A GLANCE</div>
""", unsafe_allow_html=True)

glance = [
    ("💪", "RECOVERY SCORE", f"{avg_recovery:.1f}", "/ 100",  "#60a5fa", "#3b82f6"),
    ("😴", "SLEEP HOURS",    f"{avg_sleep:.1f}",    "hrs",    "#a78bfa", "#8b5cf6"),
    ("👟", "DAILY STEPS",    f"{avg_steps:,.0f}",   "steps",  "#34d399", "#10b981"),
    ("🔥", "CALORIES BURNED",f"{avg_calories:,.0f}","kcal",   "#f87171", "#ef4444"),
]

cols = st.columns(4)
for col, (icon, label, val, unit, light, dark) in zip(cols, glance):
    col.markdown(f"""
    <div style="background:#111827; border:1px solid #1f2937;
                border-radius:16px; padding:1.4rem 1.2rem;
                text-align:center; position:relative; overflow:hidden;
                transition:all 0.2s;">
        <div style="position:absolute; top:-20px; right:-20px; width:80px; height:80px;
                    background:radial-gradient(circle, {dark}20 0%, transparent 70%);
                    border-radius:50%;"></div>
        <div style="font-size:1.8rem; margin-bottom:8px; position:relative;">{icon}</div>
        <div style="font-size:0.65rem; font-weight:700; color:#4b5563;
                    letter-spacing:0.1em; margin-bottom:8px;">{label}</div>
        <div style="font-size:2rem; font-weight:900; color:{light};
                    line-height:1; letter-spacing:-1px;">{val}</div>
        <div style="font-size:0.75rem; color:#374151; font-weight:600;
                    margin-top:5px;">{unit}</div>
        <div style="position:absolute; bottom:0; left:0; right:0; height:2px;
                    background:linear-gradient(90deg, transparent, {dark}, transparent);
                    opacity:0.6;"></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# EXPLORE THE APP
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="font-size:0.7rem; font-weight:700; color:#4b5563;
            letter-spacing:0.12em; margin-bottom:12px;">EXPLORE THE APP</div>
""", unsafe_allow_html=True)

fc1, fc2 = st.columns(2)

pages = [
    (fc1, "📈", "Dashboard", "#3b82f6", "#60a5fa",
     "Your daily health metrics in one view. Use time filters to explore.",
     [("📉", "Recovery Score & Sleep — dual trend over time"),
      ("🔵", "Recovery vs Steps — coloured by sleep quality"),
      ("❤️", "Recovery vs Resting Heart Rate scatter"),
      ("🔥", "Daily Calories Burned over time")]),
    (fc2, "🔍", "Trends & Insights", "#10b981", "#34d399",
     "Discover long-term health patterns and monthly progress.",
     [("📋", "Summary statistics — mean, min, max"),
      ("📆", "Monthly average recovery score chart"),
      ("📊", "Steps & Calories burned distributions"),
      ("🛌", "Sleep Hours & Recovery score distributions")]),
]

for col, icon, title, dark, light, desc, items in pages:
    items_html = "".join(f"""
    <div style="display:flex; align-items:center; gap:10px; padding:9px 12px;
                background:#1f2937; border-radius:8px; margin-bottom:6px;
                border:1px solid #374151;">
        <span style="font-size:0.9rem; flex-shrink:0;">{i[0]}</span>
        <span style="font-size:0.82rem; color:#9ca3af; line-height:1.3;">{i[1]}</span>
    </div>
    """ for i in items)

    col.markdown(f"""
    <div style="background:#111827; border:1px solid #1f2937;
                border-radius:16px; padding:1.6rem 1.7rem;
                position:relative; overflow:hidden;">
        <div style="position:absolute; top:-30px; right:-30px; width:120px; height:120px;
                    background:radial-gradient(circle, {dark}15 0%, transparent 65%);
                    border-radius:50%;"></div>
        <div style="position:absolute; bottom:0; left:0; right:0; height:2px;
                    background:linear-gradient(90deg, transparent, {dark}80, transparent);"></div>
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
            <div style="width:42px; height:42px; background:{dark}20;
                        border:1px solid {dark}40; border-radius:10px;
                        display:flex; align-items:center; justify-content:center;
                        font-size:1.3rem; flex-shrink:0;">{icon}</div>
            <div style="font-size:1.2rem; font-weight:800; color:{light};">{title}</div>
        </div>
        <p style="color:#6b7280; font-size:0.85rem; margin:0 0 16px;
                  line-height:1.6; border-bottom:1px solid #1f2937;
                  padding-bottom:14px;">{desc}</p>
        <div style="font-size:0.65rem; font-weight:700; color:#374151;
                    letter-spacing:0.1em; margin-bottom:10px;">CHARTS INSIDE</div>
        {items_html}
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# UNDERSTANDING YOUR METRICS
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="font-size:0.7rem; font-weight:700; color:#4b5563;
            letter-spacing:0.12em; margin-bottom:4px;">UNDERSTANDING YOUR METRICS</div>
<p style="color:#4b5563; font-size:0.85rem; margin:0 0 14px;">
    What's considered healthy — and where you currently stand.
</p>
""", unsafe_allow_html=True)

def metric_card(icon, title, your_val, val_color, bg_dark, ranges):
    def dot(c):
        colors = {"green":"#22c55e","yellow":"#f59e0b","red":"#ef4444"}
        return f'<span style="display:inline-block;width:8px;height:8px;background:{colors[c]};border-radius:50%;flex-shrink:0;margin-top:4px;"></span>'

    rows_html = "".join(f"""
    <div style="display:flex; align-items:flex-start; gap:10px; padding:8px 0;
                border-bottom:1px solid #1f2937;">
        {dot(r[2])}
        <div style="flex:1; min-width:0;">
            <span style="font-size:0.8rem; color:#e5e7eb; font-weight:600;">{r[0]}</span>
            <span style="font-size:0.78rem; color:#4b5563; margin-left:6px;">{r[1]}</span>
        </div>
    </div>
    """ for r in ranges)

    return f"""
    <div style="background:#111827; border:1px solid #1f2937; border-radius:14px;
                padding:1.3rem 1.4rem; height:100%;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
            <span style="font-size:1.5rem;">{icon}</span>
            <span style="font-size:0.95rem; font-weight:800; color:#e5e7eb;">{title}</span>
        </div>
        <div style="background:{bg_dark}; border-radius:8px; padding:7px 12px;
                    margin-bottom:14px; display:inline-flex; align-items:center; gap:6px;">
            <span style="font-size:0.72rem; color:#6b7280; font-weight:600;">YOUR AVG</span>
            <span style="font-size:0.88rem; font-weight:800; color:{val_color};">{your_val}</span>
        </div>
        {rows_html}
    </div>
    """

benchmarks = [
    ("💪", "Recovery Score",    f"{avg_recovery:.1f} / 100", "#60a5fa", "#1e3a5f20",
     [("75 – 100", "Excellent — well rested & ready",     "green"),
      ("50 – 74",  "Good — moderate, stay consistent",    "yellow"),
      ("0 – 49",   "Low — rest up, ease off workouts",    "red")]),
    ("😴", "Sleep Hours",       f"{avg_sleep:.1f} hrs",      "#a78bfa", "#4c1d9520",
     [("7 – 9 hrs",    "Optimal — best for recovery",          "green"),
      ("6 – 7 hrs",    "Adequate — slight performance dip",     "yellow"),
      ("Under 6 hrs",  "Insufficient — impacts recovery badly", "red")]),
    ("👟", "Daily Steps",       f"{avg_steps:,.0f}",          "#34d399", "#06402020",
     [("8,000 – 14,000", "Active — great for health",          "green"),
      ("4,000 – 7,999",  "Moderate — try to move more",        "yellow"),
      ("Under 4,000",    "Sedentary — short walks help a lot",  "red")]),
    ("🔥", "Calories Burned",   f"{avg_calories:,.0f} kcal", "#f87171", "#45020220",
     [("2,800+",      "High activity — strong output",         "green"),
      ("2,000–2,799", "Moderate — typical healthy adult",      "yellow"),
      ("Under 2,000", "Low — move more daily",    "red")]),
    ("❤️", "Resting Heart Rate",f"{avg_hr:.0f} bpm",          "#fb7185", "#4c000820",
     [("50 – 68 bpm",  "Excellent cardiovascular fitness",     "green"),
      ("69 – 80 bpm",  "Average — healthy for most adults",    "yellow"),
      ("Above 80 bpm", "Elevated — more cardio can help",      "red")]),
]

# Row 1 — 3 cards
r1 = st.columns(3)
for col, (icon, title, your_val, val_color, bg_dark, ranges) in zip(r1, benchmarks[:3]):
    col.markdown(metric_card(icon, title, your_val, val_color, bg_dark, ranges),
                 unsafe_allow_html=True)

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

# Row 2 — 2 cards centred
_, c1, c2, _ = st.columns([0.5, 1, 1, 0.5])
for col, (icon, title, your_val, val_color, bg_dark, ranges) in zip([c1, c2], benchmarks[3:]):
    col.markdown(metric_card(icon, title, your_val, val_color, bg_dark, ranges),
                 unsafe_allow_html=True)

st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# HOW RECOVERY SCORE IS CALCULATED
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="font-size:0.7rem; font-weight:700; color:#4b5563;
            letter-spacing:0.12em; margin-bottom:4px;">HOW RECOVERY SCORE IS CALCULATED</div>
<p style="color:#4b5563; font-size:0.85rem; margin:0 0 14px;">
    Three daily signals are combined into one 0–100 score. Base starts at 50.
</p>
""", unsafe_allow_html=True)

formula = [
    ("😴", "Sleep Hours",         "#8b5cf6", "#a78bfa",
     "Biggest contributor — up to ±20 pts",
     [("≥ 7 hrs",  "+20 pts", "#22c55e"),
      ("6–7 hrs",  "+10 pts", "#f59e0b"),
      ("< 6 hrs",  "−20 pts", "#ef4444")]),
    ("❤️", "Resting Heart Rate",  "#be123c", "#fb7185",
     "Fine-tunes the score based on BPM",
     [("< 68 bpm",  "score rises",  "#22c55e"),
      ("= 68 bpm",  "no change",    "#6b7280"),
      ("> 68 bpm",  "score drops",  "#ef4444")]),
    ("👟", "Daily Steps",         "#065f46", "#34d399",
     "Extreme counts (too high or low) penalise",
     [("4k – 14k", "no penalty", "#22c55e"),
      ("> 14k",    "−10 pts",    "#f59e0b"),
      ("< 4k",     "−10 pts",    "#ef4444")]),
]

f1, f2, f3 = st.columns(3)
for col, (icon, title, dark, light, subtitle, rows) in zip([f1, f2, f3], formula):
    rows_html = "".join(f"""
    <div style="display:flex; justify-content:space-between; align-items:center;
                background:#1f2937; border-radius:8px; padding:9px 14px;
                margin-bottom:6px; border:1px solid #374151;">
        <span style="font-size:0.83rem; color:#d1d5db; font-weight:600;">{r[0]}</span>
        <span style="font-size:0.83rem; font-weight:800; color:{r[2]};">{r[1]}</span>
    </div>
    """ for r in rows)

    col.markdown(f"""
    <div style="background:#111827; border:1px solid #1f2937;
                border-radius:16px; padding:1.5rem 1.4rem;
                text-align:center; position:relative; overflow:hidden;">
        <div style="position:absolute; top:-25px; left:50%; transform:translateX(-50%);
                    width:100px; height:100px;
                    background:radial-gradient(circle, {dark}30 0%, transparent 70%);
                    border-radius:50%; pointer-events:none;"></div>
        <div style="font-size:2.2rem; margin-bottom:10px; position:relative;">{icon}</div>
        <div style="font-size:1rem; font-weight:800; color:{light};
                    margin-bottom:4px;">{title}</div>
        <div style="font-size:0.75rem; color:#4b5563; margin-bottom:16px;
                    padding-bottom:14px; border-bottom:1px solid #1f2937;">{subtitle}</div>
        {rows_html}
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="background:#111827; border:1px solid #1f2937; border-left:3px solid #3b82f6;
            border-radius:10px; padding:1rem 1.4rem; margin-top:14px;
            display:flex; align-items:flex-start; gap:12px;">
    <span style="font-size:1.1rem; flex-shrink:0; margin-top:1px;">💡</span>
    <span style="font-size:0.85rem; color:#6b7280; line-height:1.7;">
        <b style="color:#93c5fd;">Base score starts at 50.</b>
        Sleep contributes most (up to ±20 pts). Heart rate adjusts it based on deviation
        from the healthy baseline of 68 bpm. Very high or very low step counts deduct 10 pts.
        The final score is always clamped between <b style="color:#d1d5db;">0 and 100</b>.
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="background:#111827; border:1px solid #1f2937; border-radius:12px;
            padding:1rem 1.4rem; display:flex; align-items:center; gap:12px;">
    <span style="font-size:1.1rem;">💡</span>
    <span style="font-size:0.86rem; color:#6b7280;">
        <b style="color:#93c5fd;">Tip:</b>
        Use the <b style="color:#d1d5db;">sidebar on the left</b> to navigate to
        <b style="color:#60a5fa;">Dashboard</b> or
        <b style="color:#34d399;">Trends & Insights</b>.
    </span>
</div>
<div style="text-align:center; margin-top:16px; padding-bottom:8px;">
    <span style="font-size:0.75rem; color:#374151;">
        Made with ❤️ using Streamlit &nbsp;·&nbsp; FitSync v1.0
    </span>
</div>
""", unsafe_allow_html=True)