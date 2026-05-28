import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Atlas Intelligence",
    layout="wide"
)

# ---------- STYLING ----------

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#06111f,#0b1628,#111827);
color:white;
}

.hero{
padding:100px;
border-radius:34px;
background:
linear-gradient(rgba(6,17,31,0.70),rgba(6,17,31,0.95)),
url("https://images.unsplash.com/photo-1512453979798-5ea266f8880c");
background-size:cover;
background-position:center;
border:1px solid rgba(255,255,255,0.12);
text-align:center;
margin-bottom:35px;
box-shadow:0 0 45px rgba(148,163,184,0.18);
}

.hero h1{
font-size:72px;
margin-bottom:10px;
color:white;
text-shadow:0 0 25px rgba(148,163,184,0.35);
letter-spacing:1px;
}

.hero h2{
color:#cbd5e1;
font-weight:400;
}

.card{
background:rgba(255,255,255,0.05);
padding:25px;
border-radius:25px;
text-align:center;
border:1px solid rgba(255,255,255,0.08);
}
.insight:hover{
transform: translateY(-4px);
transition:0.3s ease;
box-shadow:0 0 28px rgba(148,163,184,0.16);
}

.card h3{
font-size:40px;
margin-bottom:5px;
}
.card:hover{
transform: translateY(-6px);
transition:0.3s ease;
box-shadow:0 0 30px rgba(148,163,184,0.18);
}

.insight{
background:rgba(255,255,255,0.05);
padding:22px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.08);
margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------

st.markdown("""
<div class="hero">
<h1>Atlas Intelligence</h1>
<h2>The Future of Dubai Intelligence</h2>
<p>AI-powered Dubai real estate intelligence platform built by Syed.</p>
</div>
""", unsafe_allow_html=True)

# ---------- DATA ----------

np.random.seed(42)

areas = [
    "Downtown Dubai",
    "Dubai Marina",
    "Business Bay",
    "Palm Jumeirah",
    "Dubai Hills Estate",
    "JVC",
    "Dubai Creek Harbour",
    "DAMAC Hills"
]

data = []

for area in areas:
    for i in range(40):

        investment = np.random.randint(60,98)
        price = np.random.randint(800000,9000000)
        growth = round(np.random.uniform(4,15),2)

        data.append({
            "Area": area,
            "Investment Score": investment,
            "Average Price": price,
            "Projected Growth": growth
        })

df = pd.DataFrame(data)
# ---------- FILTERS ----------

st.sidebar.title("Atlas Control Panel")
st.sidebar.markdown("""
---
### Atlas Intelligence
AI-powered Dubai real estate intelligence platform.

Built by Syed  
MSc Business Analytics  
University of Wollongong Dubai
---
""")

selected_area = st.sidebar.multiselect(
    "Select Dubai Areas",
    options=df["Area"].unique(),
    default=df["Area"].unique()
)

df = df[df["Area"].isin(selected_area)]
selected_type = st.sidebar.multiselect(
    "Select Property Type",
    options=["Apartment", "Villa", "Townhouse", "Penthouse"],
    default=["Apartment", "Villa", "Townhouse", "Penthouse"]
)

df["Property Type"] = np.random.choice(
    ["Apartment", "Villa", "Townhouse", "Penthouse"],
    size=len(df)
)

df = df[df["Property Type"].isin(selected_type)]

# ---------- KPI CARDS ----------

c1,c2,c3,c4 = st.columns(4)

c1.markdown(f"""
<div class="card">
<h3>↗ {len(df)}</h3>
<p>Properties Analyzed</p>
</div>
""", unsafe_allow_html=True)

c2.markdown(f"""
<div class="card">
<h3>◆ {df['Area'].nunique()}</h3>
<p>Dubai Areas</p>
</div>
""", unsafe_allow_html=True)

c3.markdown(f"""
<div class="card">
<h3>AI {df['Investment Score'].mean():.1f}</h3>
<p>Avg Investment Score</p>
</div>
""", unsafe_allow_html=True)

c4.markdown(f"""
<div class="card">
<h3>+{df['Projected Growth'].mean():.1f}%</h3>
<p>Avg Market Growth</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------- CHART ----------

left,right = st.columns([1.3,1])

with left:

    st.subheader("Dubai Investment Intelligence")

    chart_data = (
        df.groupby("Area")["Investment Score"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        chart_data,
        x="Investment Score",
        y="Area",
        orientation="h",
        color="Investment Score",
        height=500
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0,r=0,t=30,b=0)
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------- AI INSIGHTS ----------

with right:

    st.subheader("AI Market Intelligence")

    top_area = chart_data.iloc[0]["Area"]

    st.markdown(f"""
    <div class="insight">
    <h4>Growth Signal</h4>
    <p>{top_area} is showing the strongest investment momentum in Atlas Intelligence scoring models.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight">
    <h4>Luxury Market Trend</h4>
    <p>Dubai premium real estate continues showing resilience across waterfront and high-demand communities.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight">
    <h4>AI Forecast</h4>
    <p>Projected investment activity indicates increasing demand in luxury residential sectors.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
# ---------- DUBAI MAP ----------

st.subheader("Dubai Real Estate Intelligence Map")

map_df = pd.DataFrame({
    "Area":[
        "Downtown Dubai",
        "Dubai Marina",
        "Business Bay",
        "Palm Jumeirah",
        "Dubai Hills Estate",
        "JVC",
        "Dubai Creek Harbour",
        "DAMAC Hills"
    ],

    "lat":[
        25.1972,
        25.0800,
        25.1850,
        25.1124,
        25.1000,
        25.0520,
        25.2065,
        25.0272
    ],

    "lon":[
        55.2744,
        55.1400,
        55.2800,
        55.1390,
        55.2470,
        55.2110,
        55.3472,
        55.2236
    ],

    "Investment Score":[92,89,87,95,85,80,88,83]
})

fig_map = px.scatter_mapbox(
    map_df,
    lat="lat",
    lon="lon",
    size="Investment Score",
    color="Investment Score",
    hover_name="Area",
    zoom=10,
    height=650
)

fig_map.update_layout(
    mapbox_style="carto-darkmatter",
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0,r=0,t=0,b=0)
)

st.plotly_chart(fig_map, use_container_width=True)
# ---------- EXECUTIVE TABLE ----------

st.write("")
st.subheader("Executive Area Intelligence")

table_df = (
    df.groupby("Area")
    .agg({
        "Investment Score":"mean",
        "Average Price":"mean",
        "Projected Growth":"mean"
    })
    .reset_index()
)

table_df.columns = [
    "Area",
    "Investment Score",
    "Average Property Price",
    "Projected Growth %"
]

st.dataframe(
    table_df,
    use_container_width=True
)
# ---------- INVESTMENT RECOMMENDATION ENGINE ----------

st.write("")
st.subheader("AI Investment Recommendation")

best_area = table_df.sort_values("Investment Score", ascending=False).iloc[0]
growth_area = table_df.sort_values("Projected Growth %", ascending=False).iloc[0]

st.markdown(f"""
<div class="insight">
<h4>Atlas AI Recommendation</h4>

<p>
Atlas Intelligence recommends focusing on <b>{best_area['Area']}</b> based on the strongest overall investment score of <b>{best_area['Investment Score']:.1f}</b>.
</p>

<p>
For growth-focused strategy, <b>{growth_area['Area']}</b> shows the highest projected growth at <b>{growth_area['Projected Growth %']:.1f}%</b>.
</p>

</div>
""", unsafe_allow_html=True)
# ---------- MARKET TREND ----------

st.write("")
st.subheader("Dubai Market Growth Trend")

trend_df = pd.DataFrame({
    "Year":[2021,2022,2023,2024,2025,2026],
    "Growth":[5.2,7.8,9.4,11.3,13.1,15.0]
})

fig_trend = px.line(
    trend_df,
    x="Year",
    y="Growth",
    markers=True
)

fig_trend.update_layout(
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    height=450
)

st.plotly_chart(fig_trend, use_container_width=True)
# ---------- MARKET SENTIMENT ----------

st.write("")
st.subheader("Dubai Market Sentiment")

avg_score = df["Investment Score"].mean()

if avg_score >= 85:
    sentiment = "Bullish"
    message = "Dubai luxury real estate market is showing strong investment momentum."
elif avg_score >= 75:
    sentiment = "Stable Growth"
    message = "Dubai real estate market remains stable with healthy investment indicators."
else:
    sentiment = "Moderate"
    message = "Market conditions indicate selective investment opportunities."

st.markdown(f"""
<div class="insight">
<h4>Current Market Sentiment: {sentiment}</h4>
<p>{message}</p>
</div>
""", unsafe_allow_html=True)
# ---------- FOOTER ----------

st.write("")
st.markdown("""
---
<center>

### Atlas Intelligence

AI-powered Dubai real estate intelligence platform.

Built with Python, Streamlit, Plotly & AI-driven analytics.

© 2026 Atlas Intelligence — Prototype V2

</center>
""", unsafe_allow_html=True)
st.success("Atlas Intelligence Luxury Prototype V2 Live")
