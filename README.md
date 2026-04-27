# 🏃 FitSync — Health Analytics Platform
**Your personal health analytics dashboard — track recovery, sleep, and activity all in one place.**

---

## 📌 Project Overview
FitSync is a 3-page personal health analytics dashboard built with Python and Streamlit. It visualizes daily health signals — recovery score, sleep, steps, heart rate, and calories — in an interactive and filterable interface. The app leverages Pandas for data processing and Plotly for rich chart visualizations. FitSync empowers users to understand their long-term health trends through a clean, data-driven product.

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.8-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0-lightgrey)
![Pandas](https://img.shields.io/badge/Pandas-1.3.3-yellow)
![Plotly](https://img.shields.io/badge/Plotly-5.3.1-blue)
![Continue Agent](https://img.shields.io/badge/Continue_Agent-1.0-orange)
![GitHub Codespaces](https://img.shields.io/badge/GitHub%20Codespaces-Available-brightgreen)

---

## ✨ Features

| Page | Description |
|------|-------------|
| 🏠 Home | KPI cards for Avg Recovery Score, Steps, Sleep Hours, and Calories Burned |
| 📊 Dashboard | Time-filtered charts — recovery trends, step correlation, and calorie tracking |
| 📈 Trends | Monthly recovery patterns, summary stats, and health metric histograms |

---

## 🚀 How to Run

1. Clone the repository using:
   ```bash
   git clone https://github.com/your-username/fitsync.git
   ```

2. Open a new Codespace.

3. In the terminal, run the following command:
   ```bash
   streamlit run main.py
   ```

---

## 🧠 Recovery Score Logic
The Recovery Score (0–100) is the ML-style core feature of FitSync,
calculated from 3 daily health signals. Base score starts at 50.

**Sleep Hours**
- >= 7 hrs → +20 pts
- 6 to 7 hrs → +10 pts
- < 6 hrs → -20 pts

**Resting Heart Rate**
- Lower than 68 BPM → adds points
- Higher than 68 BPM → deducts points

**Daily Steps**
- 4,000 to 14,000 steps → no penalty (optimal zone)
- Below 4,000 or above 14,000 → -10 pts

> Final score is clamped between 0 and 100.

---

## 🤖 Built with AI
In the development of FitSync, Continue Agent inside GitHub Codespaces was used
to accelerate syntax and boilerplate generation. All core architecture decisions,
recovery score logic, and data pipeline design were fully owned and implemented
by the developer.

---
*Made with ❤️ using Streamlit · FitSync v1.0 · Built with GitHub Codespaces @ Saras AI Institute*