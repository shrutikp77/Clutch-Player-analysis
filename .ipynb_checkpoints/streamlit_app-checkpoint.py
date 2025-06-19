import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("second_innings_with_wp.csv")
bat_profiles = pd.read_csv("player_batting_profiles.csv")
clutch_scores = pd.read_csv("clutch_scores.csv")
wp_impact = pd.read_csv("batsman_wp_impact.csv")

st.title("🏏 Clutch Player Detection Dashboard")

# Sidebar: Player selector
players = sorted(df['batsman'].unique())
selected_player = st.sidebar.selectbox("Select a Player", players)

# Filter data
player_df = df[df['batsman'] == selected_player]
profile_row = bat_profiles[bat_profiles['batsman'] == selected_player]
wp_row = wp_impact[wp_impact['batsman'] == selected_player]
clutch_row = clutch_scores[clutch_scores.index == selected_player]

st.header(f"Performance Profile: {selected_player}")

col1, col2, col3 = st.columns(3)
col1.metric("Avg Strike Rate (Last 5)", f"{profile_row['rolling_strike_rate'].mean():.2f}")
col2.metric("Form Index", f"{profile_row['form_index'].mean():.1f}")
col3.metric("Clutch Score", f"{clutch_row['clutch_score'].values[0]:.2f}" if not clutch_row.empty else "N/A")

st.subheader("📈 Win Probability Delta (Clutch Impact)")
st.line_chart(player_df.set_index('ball_number')['win_prob'])

st.subheader("🔥 Pressure Heatmap (Over × Wickets Remaining)")
heatmap_data = df.groupby(['over', 'wickets_remaining'])['is_pressure'].mean().unstack()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap="Reds", annot=True, fmt=".2f", ax=ax)
st.pyplot(fig)


st.header("🏅 Top 10 Bowlers Under Pressure (Clutch Score)")

# Ensure clutch_scores index is batsman
if 'batsman' in clutch_scores.columns:
    clutch_scores.set_index('batsman', inplace=True)

# Get top 10
top10_clutch = clutch_scores.sort_values('clutch_score', ascending=False).head(10)

# Plot bar chart
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top10_clutch['clutch_score'], y=top10_clutch.index, palette="viridis", ax=ax4)
ax4.set_title("Top 10 Clutch Players (by Clutch Score)")
ax4.set_xlabel("Clutch Score")
ax4.set_ylabel("Player")
st.pyplot(fig4)

st.header("🏏 Batsmen Who Perform Best Under Pressure")

# Optional: Filter out primarily bowlers manually (or use known list)
# For now, let's assume top batters based on clutch_score among known batsmen
bat_stats = pd.read_csv("player_batting_profiles.csv")
batsman_list = bat_stats.groupby('batsman')['balls_faced'].sum().sort_values(ascending=False).head(50).index

batsman_clutch = clutch_scores[clutch_scores.index.isin(batsman_list)]


# Sort and pick top 10 batsmen by clutch score
top10_batsmen = batsman_clutch.sort_values('clutch_score', ascending=False).head(10)

# Plot
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top10_batsmen['clutch_score'], y=top10_batsmen.index, palette="crest", ax=ax5)
ax5.set_title("Top 10 Batsmen Under Pressure (Clutch Score)")
ax5.set_xlabel("Clutch Score")
ax5.set_ylabel("Batsman")
st.pyplot(fig5)



