# Clutch Player Detection: Who Performs Under Pressure?

> **"I built a data-driven way to quantify mental toughness in cricket."**

## Project Objective

This project analyzes IPL match data to identify **clutch players** — those who consistently perform under pressure — using advanced metrics like **win probability impact**, **pressure-phase strike rate**, and **custom clutch scores**.

---

## Key Features

-  Detects high-pressure match situations dynamically
-  Calculates **Clutch Score** combining strike rate & win probability delta
-  Profiles each player’s performance under pressure
-  Visual comparison tools (e.g., MS Dhoni vs Virat Kohli)
-  Streamlit Dashboard for real-time exploration

---

## Clutch Score Formula

A custom metric to quantify performance in pressure situations:
Clutch Score = 0.7 × Pressure Strike Rate + 0.3 × Avg WP Delta

Where:
- **Pressure SR** = Strike rate when required run rate is high or wickets are low
- **WP Delta** = Change in win probability per ball contributed by the player

---

## Techniques Used

-  Time-series modeling for run rate and game phase segmentation
-  Win Probability Model (WPA-style)
-  Context-aware feature engineering (e.g., required RR, wickets left)
-  Rolling metrics (form index, pressure SR)
-  Streamlit interactive dashboard

---

## Data Sources

- `matches.csv` – Match-level info (teams, venue, result, etc.)
- `deliveries.csv` – Ball-by-ball breakdown for each IPL match
- Data Source: [Cricsheet.org](https://cricsheet.org/) (T20 + IPL JSON converted to CSV)

---

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/shrutikp77/Clutch-Player-analysis.git
cd clutch-player-detection

### 2. Install dependency
pip install -r requirements.txt

### 3. Run the Streamlit dashboard
streamlit run streamlit_app.py



