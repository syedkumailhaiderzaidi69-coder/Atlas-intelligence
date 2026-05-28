import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from datetime import datetime
from io import BytesIO

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
            "Projected Growth":[10.8,9.6,8.2,12.4],
            "Rental Yield":[7.2,6.8,8.5,5.9],
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
# ---------- LIVE DATA STATUS ----------


current_time = datetime.now().strftime("%d %b %Y | %H:%M")

st.sidebar.markdown(f"""
### Live Market Status

🟢 Market Feed Active  
🟢 Forecast Engine Online  
🟢 AI Scoring Models Active  

Last Refresh:
{current_time}

---
""")
# ---------- MANUAL REFRESH CONTROL ----------

if st.sidebar.button("Refresh Market Intelligence"):
    st.sidebar.success("Market intelligence refreshed successfully.")
    st.rerun()
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
# ---------- EXECUTIVE MARKET SIGNALS ----------

st.write("")
st.markdown("""
---
### Executive Market Signals
""")

signal_col1, signal_col2 = st.columns(2)

with signal_col1:

    st.success("""
    📈 Investment Confidence: STRONG
    
    Atlas models indicate healthy long-term investment conditions across premium Dubai communities.
    """)

    st.info("""
    🏙️ Market Momentum: BULLISH
    
    Growth indicators remain positive across luxury and mid-market sectors.
    """)

with signal_col2:

    st.warning("""
    💰 Rental Yield Outlook: ATTRACTIVE
    
    Selected communities continue delivering strong passive income performance.
    """)

    st.success("""
    🤖 AI Forecast Reliability: HIGH
    
    Atlas Intelligence forecasting systems remain stable with strong confidence indicators.
    """)
    # ---------- AI CONFIDENCE HEAT METER ----------

st.write("")
st.markdown("""
---
### Atlas AI Confidence Meter
""")

confidence_score = np.random.randint(82,96)

confidence_color = (
    "green"
    if confidence_score >= 90
    else "orange"
)

st.markdown(f"""
<div style="
padding:25px;
border-radius:20px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.08);
">

<h3>AI Market Confidence</h3>

<div style="
width:100%;
background:#1c1c1c;
border-radius:20px;
overflow:hidden;
height:35px;
margin-top:15px;
">

<div style="
width:{confidence_score}%;
background:{confidence_color};
height:35px;
text-align:center;
line-height:35px;
font-weight:bold;
color:white;
">
{confidence_score}%
</div>

</div>

<p style="margin-top:15px;">
Atlas Intelligence forecasting systems indicate stable investment confidence across Dubai real estate sectors.
</p>

</div>
""", unsafe_allow_html=True)


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
# ---------- AI OPPORTUNITY SCANNER ----------

st.write("")
st.markdown("""
---
### Atlas AI Opportunity Scanner
""")

best_growth = (
    table_df.sort_values(
        "Projected Growth %",
        ascending=False
    )
    .iloc[0]
)

best_price = (
    table_df.sort_values(
        "Average Property Price"
    )
    .iloc[0]
)

best_score = (
    table_df.sort_values(
        "Investment Score",
        ascending=False
    )
    .iloc[0]
)

scan_col1, scan_col2, scan_col3 = st.columns(3)

scan_col1.markdown(f"""
<div class="insight">
<h4>🚀 Growth Opportunity</h4>

<p>
<b>{best_growth['Area']}</b>
</p>

<p>
Projected Growth:
<b>{best_growth['Projected Growth %']:.1f}%</b>
</p>
</div>
""", unsafe_allow_html=True)

scan_col2.markdown(f"""
<div class="insight">
<h4>💎 Premium Investment</h4>

<p>
<b>{best_score['Area']}</b>
</p>

<p>
Investment Score:
<b>{best_score['Investment Score']:.1f}</b>
</p>
</div>
""", unsafe_allow_html=True)

scan_col3.markdown(f"""
<div class="insight">
<h4>💰 Affordability Signal</h4>

<p>
<b>{best_price['Area']}</b>
</p>

<p>
Entry Pricing Advantage Detected
</p>
</div>
""", unsafe_allow_html=True)
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
# ---------- MARKET ALERT SYSTEM ----------

st.write("")
st.markdown("""
---
### Atlas Market Alerts
""")

alerts = [
    "📈 High-growth momentum detected in Dubai Creek Harbour.",
    "🏙️ Luxury demand increasing across Palm Jumeirah.",
    "💰 Rental yield strength improving in JVC.",
    "📊 Investment confidence remains bullish across Dubai Marina."
]

for alert in alerts:
    st.warning(alert)
    # ---------- INVESTOR PORTFOLIO ANALYZER ----------

st.write("")
st.markdown("""
---
### Investor Portfolio Analyzer
""")

portfolio_budget = st.slider(
    "Portfolio Budget (AED)",
    1000000,
    20000000,
    5000000,
    step=500000,
    key="portfolio_budget"
)

investment_goal = st.selectbox(
    "Investment Goal",
    [
        "Passive Income",
        "Balanced Growth",
        "Luxury Appreciation",
        "Aggressive Growth"
    ]
)

portfolio_df = pd.DataFrame({
    "Area":[
        "Downtown Dubai",
        "Dubai Marina",
        "JVC",
        "Palm Jumeirah"
    ]
})

if investment_goal == "Passive Income":

    portfolio_df["Allocation %"] = [20,30,40,10]

elif investment_goal == "Balanced Growth":

    portfolio_df["Allocation %"] = [30,30,25,15]

elif investment_goal == "Luxury Appreciation":

    portfolio_df["Allocation %"] = [20,20,10,50]

else:

    portfolio_df["Allocation %"] = [25,20,15,40]

portfolio_df["Investment Amount"] = (
    portfolio_df["Allocation %"] / 100 * portfolio_budget
).astype(int)

st.dataframe(
    portfolio_df,
    use_container_width=True
)

st.markdown(f"""
<div class="insight">
<h4>Atlas Portfolio Strategy</h4>

<p>
Atlas Intelligence generated a portfolio allocation strategy optimized for:
<b>{investment_goal}</b>
</p>

<p>
Portfolio Budget:
<b>AED {portfolio_budget:,}</b>
</p>

</div>
""", unsafe_allow_html=True)
# ---------- AI STRATEGY ENGINE ----------

st.write("")
st.markdown("""
---
### Atlas AI Strategy Engine
""")

investor_type = st.selectbox(
    "Investor Profile",
    [
        "Conservative",
        "Balanced",
        "Aggressive",
        "Luxury Investor"
    ]
)

investment_horizon = st.selectbox(
    "Investment Horizon",
    [
        "1-2 Years",
        "3-5 Years",
        "5-10 Years"
    ]
)

if investor_type == "Conservative":

    ai_strategy = """
    Atlas recommends focusing on stable rental-yield communities such as JVC and Dubai Marina with balanced cashflow opportunities.
    """

elif investor_type == "Balanced":

    ai_strategy = """
    Atlas recommends diversified allocation across Downtown Dubai, Dubai Marina, and Dubai Hills Estate for balanced growth and stability.
    """

elif investor_type == "Aggressive":

    ai_strategy = """
    Atlas recommends targeting high-growth areas such as Dubai Creek Harbour and emerging investment corridors.
    """

else:

    ai_strategy = """
    Atlas recommends premium luxury-focused allocation toward Palm Jumeirah and ultra-prime waterfront communities.
    """

st.markdown(f"""
<div class="insight">
<h4>AI Strategic Recommendation</h4>

<p>
Investor Profile:
<b>{investor_type}</b>
</p>

<p>
Investment Horizon:
<b>{investment_horizon}</b>
</p>

<p>
{ai_strategy}
</p>

</div>
""", unsafe_allow_html=True)
# ---------- MARKET REGIME ENGINE ----------

st.write("")
st.markdown("""
---
### Atlas Market Regime Engine
""")

avg_growth = df["Projected Growth"].mean()
avg_yield = df["Rental Yield"].mean()

if avg_growth >= 11 and avg_yield >= 7:
    regime = "Bull Market"
    regime_msg = """
    Dubai real estate is currently showing strong growth momentum with healthy rental performance.
    """

elif avg_growth >= 8:
    regime = "Stable Expansion"
    regime_msg = """
    Atlas Intelligence indicates balanced market conditions with moderate long-term growth.
    """

elif avg_growth >= 6:
    regime = "Selective Opportunity"
    regime_msg = """
    Certain communities continue showing strength while broader growth remains moderate.
    """

else:
    regime = "Correction Risk"
    regime_msg = """
    Atlas Intelligence detects slowing momentum and elevated investment caution signals.
    """

st.markdown(f"""
<div class="insight">
<h4>Current Market Regime: {regime}</h4>

<p>
{regime_msg}
</p>

<p>
Average Growth:
<b>{avg_growth:.1f}%</b><br>

Average Rental Yield:
<b>{avg_yield:.1f}%</b>
</p>

</div>
""", unsafe_allow_html=True)
# ---------- PDF REPORT EXPORT ----------

report_text = f"""
ATLAS INTELLIGENCE INVESTOR REPORT

Investment Goal:
{investment_goal}

Portfolio Budget:
AED {portfolio_budget:,}

Recommended Allocation:

{portfolio_df.to_string(index=False)}

Top Portfolio Area:
{portfolio_df.iloc[0]['Area']}

Primary Allocation:
{portfolio_df.iloc[0]['Allocation %']}%

Generated by Atlas Intelligence.
"""

report_bytes = BytesIO()
report_bytes.write(report_text.encode())

st.download_button(
    label="Generate Investor Report",
    data=report_bytes.getvalue(),
    file_name="atlas_investor_report.txt",
    mime="text/plain"
)
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
# ---------- RENTAL YIELD INTELLIGENCE ----------
# ---------- INVESTMENT STRATEGY CLASSIFIER ----------

st.write("")
st.markdown("""
---
### Investment Strategy Classification
""")

strategy_df = table_df.copy()

strategy_df["Rental Yield"] = (
    df.groupby("Area")["Rental Yield"]
    .mean()
    .values
)

strategies = []

for _, row in strategy_df.iterrows():

    if row["Rental Yield"] >= 8:
        strategies.append("Cashflow Play")

    elif row["Projected Growth %"] >= 11:
        strategies.append("High-Growth Opportunity")

    elif row["Average Property Price"] >= 5000000:
        strategies.append("Luxury Growth Play")

    else:
        strategies.append("Balanced Investment")

strategy_df["Strategy"] = strategies

st.dataframe(
    strategy_df[
        [
            "Area",
            "Rental Yield",
            "Projected Growth %",
            "Strategy"
        ]
    ],
    use_container_width=True
)

top_strategy = strategy_df.iloc[0]

st.markdown(f"""
<div class="insight">
<h4>Atlas Strategy Insight</h4>

<p>
Atlas Intelligence classifies Dubai communities into different investment strategies to support investor decision-making.
</p>

<p>
Current highlighted strategy:
<b>{top_strategy['Area']}</b> — <b>{top_strategy['Strategy']}</b>
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("""
---
### Rental Yield Intelligence
""")

yield_df = (
    df.groupby("Area")["Rental Yield"]
    .mean()
    .reset_index()
)

yield_df = yield_df.sort_values(
    "Rental Yield",
    ascending=False
)

top_yield = yield_df.iloc[0]

st.dataframe(
    yield_df,
    use_container_width=True
)

st.markdown(f"""
<div class="insight">
<h4>Atlas Rental Yield Signal</h4>

<p>
<b>{top_yield['Area']}</b> currently shows the strongest rental yield potential for passive income investors.
</p>

<p>
Estimated Rental Yield: <b>{top_yield['Rental Yield']:.1f}%</b>
</p>

</div>
""", unsafe_allow_html=True)

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
    width=700,
    height=500
)

st.plotly_chart(
    fig_radar,
    use_container_width=False,
    config={'displayModeBar': False}
)
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
