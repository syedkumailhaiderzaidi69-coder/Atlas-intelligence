import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

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
# ---------- LOADING SCREEN ----------

loading = st.empty()

loading.markdown("""
<div class="hero">
<h1>Initializing Atlas Intelligence...</h1>
<h2>Loading Dubai Market Intelligence Systems</h2>
<p>AI engines starting...</p>
</div>
""", unsafe_allow_html=True)

time.sleep(2)

loading.empty()

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
# ---------- INVESTMENT SCORING MODEL ----------

max_price = df["Average Price"].max()

df["Affordability Score"] = (
    100 - (df["Average Price"] / max_price * 100)
)

df["Market Confidence"] = np.random.randint(
    75,
    96,
    size=len(df)
)

df["Luxury Demand"] = np.random.randint(
    70,
    98,
    size=len(df)
)
df["Rental Yield"] = np.random.uniform(
    5.0,
    9.5,
    size=len(df)
).round(1)

df["Investment Score"] = (
    df["Projected Growth"] * 4 * 0.35 +
    df["Affordability Score"] * 0.25 +
    df["Market Confidence"] * 0.15 +
    df["Luxury Demand"] * 0.10 +
    df["Rental Yield"] * 8 * 0.15
).round(1)
# ---------- LIVE DATA FUNCTION ----------

def load_live_property_data(api_source, api_key):
    """
    Prototype live-data function.
    Future version will connect to real APIs such as Bayut, Property Finder, or DLD.
    """
    
    if api_source == "Bayut API" and api_key:
        live_data = pd.DataFrame({
            "Area":["Dubai Marina","Business Bay","JVC","Palm Jumeirah"],
            "Investment Score":[89,86,80,95],
            "Average Price":[3200000,2800000,1450000,8500000],
            "Projected Growth":[10.8,9.6,8.2,12.4]
        })
        return live_data

    return df
# ---------- FILTERS ----------
# ---------- DATA SOURCE MODE ----------

st.sidebar.markdown("## Data Source")

data_source = st.sidebar.radio(
    "Select Data Mode",
    ["Demo Data", "Upload CSV", "Live API Mode Coming Soon"]
)

if data_source == "Live API Mode Coming Soon":
    st.sidebar.warning("Live API integration is planned for the next version.")
if data_source == "Upload CSV":

    uploaded_file = st.sidebar.file_uploader(
        "Upload Real Estate CSV",
        type=["csv"]
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.sidebar.success("Custom dataset uploaded successfully.")
    
sample_df = pd.DataFrame({
    "Area":["Downtown Dubai","Dubai Marina"],
    "Investment Score":[92,88],
    "Average Price":[4500000,3200000],
    "Projected Growth":[12.5,10.8]
})

csv = sample_df.to_csv(index=False).encode('utf-8')

st.sidebar.download_button(
    label="Download CSV Template",
    data=csv,
    file_name='atlas_template.csv',
    mime='text/csv'
)
# ---------- API CONNECTION PANEL ----------

st.sidebar.markdown("## API Connection")

api_source = st.sidebar.selectbox(
    "Choose API Source",
    [
        "None",
        "Dubai Land Department API",
        "Property Finder API",
        "Bayut API"
    ]
)

api_key = st.sidebar.text_input(
    "API Key",
    type="password"
)

if api_source != "None":
    if api_key:
        st.sidebar.success(f"{api_source} connected in prototype mode.")
    else:
        st.sidebar.warning("Enter API key to activate live data connection.")

if api_source != "None" and api_key:
    df = load_live_property_data(api_source, api_key)
       
    

    


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
st.sidebar.markdown("""
### System Status


🟢 AI Engine Online  
🟢 Dubai Market Feed Active  
🟢 Investment Models Running  
🟢 Forecast Engine Stable  

---
""")
# ---------- AI CHAT ASSISTANT ----------

st.sidebar.markdown("## Atlas AI Assistant")

user_question = st.sidebar.text_input(
    "Ask Atlas Intelligence"
)

if user_question:

    question = user_question.lower()

    if "best" in question or "investment" in question:
        response = "Palm Jumeirah and Downtown Dubai currently show the strongest Atlas investment intelligence scores."

    elif "growth" in question:
        response = "Dubai Creek Harbour is showing strong projected growth momentum based on Atlas forecasting models."

    elif "luxury" in question:
        response = "Palm Jumeirah remains one of Dubai’s strongest luxury investment zones."

    elif "marina" in question:
        response = "Dubai Marina continues attracting strong rental demand and investor activity."

    else:
        response = "Atlas AI is analyzing Dubai market intelligence. More advanced AI models coming soon."

    st.sidebar.success(response)

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

    st.markdown("""
---
### Dubai Investment Intelligence
""")

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

    st.markdown("""
---
### AI Market Intelligence
""")

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
st.caption(
"Bubble size represents investment strength. Darker color intensity represents stronger Atlas intelligence scoring."
)
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
gauge_fig = px.pie(
    values=[82,18],
    names=["AI Confidence",""],
    hole=0.75
)

gauge_fig.update_traces(
    textinfo='none'
)

gauge_fig.update_layout(
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    annotations=[
        dict(
            text="82%<br>AI Confidence",
            x=0.5,
            y=0.5,
            font_size=22,
            showarrow=False
        )
    ],
    height=350,
    showlegend=False
)

st.plotly_chart(gauge_fig, use_container_width=True)
# ---------- API INTEGRATION ROADMAP ----------

st.write("")
st.markdown("""
---
### Live Data Integration Roadmap

Atlas Intelligence is designed to evolve from demo analytics into an automated real estate intelligence platform.

Planned data integrations:
- Dubai Land Department transaction data
- Property listing market data
- Rental yield indicators
- Area-level growth trends
- Developer performance data

Future live mode will allow Atlas Intelligence to automatically refresh market insights without manual CSV uploads.
""")
# ---------- METHODOLOGY ----------

st.write("")
st.markdown("""
---
### Methodology

Atlas Intelligence currently uses simulated Dubai real estate data to prototype:

- Investment scoring
- Market growth analysis
- Geographic intelligence
- AI-generated recommendations
- Executive dashboard reporting

Future versions will integrate live market datasets and advanced predictive models.
""")
# ---------- AI SCORE GAUGES ----------

st.write("")
st.markdown("""
---
### Atlas Intelligence Indicators
""")

g1,g2,g3,g4 = st.columns(4)

g1.markdown("""
<div class="card">
<h3>92%</h3>
<p>Investment Strength</p>
</div>
""", unsafe_allow_html=True)

g2.markdown("""
<div class="card">
<h3>88%</h3>
<p>Market Confidence</p>
</div>
""", unsafe_allow_html=True)

g3.markdown("""
<div class="card">
<h3>85%</h3>
<p>Growth Potential</p>
</div>
""", unsafe_allow_html=True)

g4.markdown("""
<div class="card">
<h3>90%</h3>
<p>Luxury Demand</p>
</div>
""", unsafe_allow_html=True)
# ---------- UNDERVALUED AREA DETECTOR ----------
# ---------- FORECAST GROWTH ENGINE ----------

st.write("")
st.markdown("""
---
### Future Growth Forecast Engine
""")

forecast_df = table_df.copy()

forecast_df["Forecast Growth 2027"] = (
    forecast_df["Projected Growth %"] * np.random.uniform(1.1,1.4)
).round(1)

forecast_df["Confidence Score"] = np.random.randint(
    82,
    96,
    size=len(forecast_df)
)

forecast_df = forecast_df.sort_values(
    "Forecast Growth 2027",
    ascending=False
)

st.dataframe(
    forecast_df[
        [
            "Area",
            "Forecast Growth 2027",
            "Confidence Score"
        ]
    ],
    use_container_width=True
)

top_forecast = forecast_df.iloc[0]

st.markdown(f"""
<div class="insight">
<h4>Atlas Forecast Signal</h4>

<p>
<b>{top_forecast['Area']}</b> is projected to show the strongest future market momentum heading into 2027.
</p>

<p>
Forecast Growth: <b>{top_forecast['Forecast Growth 2027']:.1f}%</b><br>
Confidence Score: <b>{top_forecast['Confidence Score']}%</b>
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("""
---
### Undervalued Area Detector
""")

undervalued_df = table_df.copy()

undervalued_df["Undervalued Score"] = (
    undervalued_df["Investment Score"] * 0.45
    + undervalued_df["Projected Growth %"] * 4
    - (undervalued_df["Average Property Price"] / 1000000) * 2
)

undervalued_df = undervalued_df.sort_values("Undervalued Score", ascending=False)

top_undervalued = undervalued_df.iloc[0]

st.markdown(f"""
<div class="insight">
<h4>Atlas Undervalued Signal</h4>

<p>
<b>{top_undervalued['Area']}</b> appears to be the strongest undervalued opportunity based on price, growth, and investment score indicators.
</p>

<p>
Undervalued Score: <b>{top_undervalued['Undervalued Score']:.1f}</b>
</p>

</div>
""", unsafe_allow_html=True)

st.dataframe(
    undervalued_df[["Area", "Investment Score", "Average Property Price", "Projected Growth %", "Undervalued Score"]],
    use_container_width=True
)
# ---------- AREA COMPARISON ENGINE ----------

st.write("")
st.markdown("""
---
### Area Comparison Engine
""")

compare_col1, compare_col2 = st.columns(2)

area_1 = compare_col1.selectbox(
    "Select First Area",
    options=df["Area"].unique(),
    key="area_1"
)

area_2 = compare_col2.selectbox(
    "Select Second Area",
    options=df["Area"].unique(),
    key="area_2"
)

area_1_data = df[df["Area"] == area_1][["Investment Score", "Average Price", "Projected Growth"]].mean()
area_2_data = df[df["Area"] == area_2][["Investment Score", "Average Price", "Projected Growth"]].mean()

comparison_df = pd.DataFrame({
    "Metric": ["Investment Score", "Average Price", "Projected Growth"],
    area_1: [
        round(area_1_data["Investment Score"], 1),
        round(area_1_data["Average Price"], 0),
        round(area_1_data["Projected Growth"], 1)
    ],
    area_2: [
        round(area_2_data["Investment Score"], 1),
        round(area_2_data["Average Price"], 0),
        round(area_2_data["Projected Growth"], 1)
    ]
})

st.dataframe(comparison_df, use_container_width=True)

if area_1_data["Investment Score"] > area_2_data["Investment Score"]:
    winner = area_1
else:
    winner = area_2

st.markdown(f"""
<div class="insight">
<h4>Atlas Comparison Result</h4>

<p>
<b>{winner}</b> currently shows stronger overall investment intelligence based on Atlas scoring models.
</p>

</div>
""", unsafe_allow_html=True)

radar_df = pd.DataFrame({
    "Metric": ["Investment Score", "Projected Growth"],
    area_1: [
        area_1_data["Investment Score"],
        area_1_data["Projected Growth"] * 6
    ],
    area_2: [
        area_2_data["Investment Score"],
        area_2_data["Projected Growth"] * 6
    ]
})

fig_radar = px.line_polar(
    radar_df,
    r=area_1,
    theta="Metric",
    line_close=True
)

fig_radar.add_scatterpolar(
    r=radar_df[area_2],
    theta=radar_df["Metric"],
    fill='toself',
    name=area_2
)

fig_radar.update_layout(
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    height=500
)

st.plotly_chart(fig_radar, use_container_width=True)
# ---------- INVESTMENT SIMULATOR ----------

st.write("")
st.markdown("""
---
### AI Investment Simulator
""")

budget = st.slider(
    "Investment Budget (AED)",
    500000,
    10000000,
    3000000,
    step=500000
)

risk = st.selectbox(
    "Risk Preference",
    ["Low", "Medium", "High"]
)

luxury_pref = st.slider(
    "Luxury Preference",
    1,
    10,
    7
)

if budget >= 5000000 and luxury_pref >= 8:
    recommended = "Palm Jumeirah"

elif risk == "High":
    recommended = "Dubai Creek Harbour"

elif budget <= 2000000:
    recommended = "JVC"

else:
    recommended = "Downtown Dubai"

st.markdown(f"""
<div class="insight">
<h4>Atlas AI Investment Simulation</h4>

<p>
Based on your investment profile, Atlas Intelligence recommends focusing on <b>{recommended}</b>.
</p>

<p>
AI models analyzed budget allocation, luxury preference, and growth potential to generate this recommendation.
</p>

</div>
""", unsafe_allow_html=True)
# ---------- PRODUCT ROADMAP ----------

st.write("")
st.markdown("""
---
### Product Roadmap

**V1:** Luxury Dubai real estate intelligence dashboard  
**V2:** AI chatbot assistant and investment recommendation engine  
**V3:** Live market data integration  
**V4:** Predictive pricing and rental yield forecasting  
**V5:** Investor-ready PDF intelligence reports  
""")
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
