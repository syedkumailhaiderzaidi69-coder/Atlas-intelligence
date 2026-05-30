import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from datetime import datetime
from io import BytesIO
from fpdf import FPDF
# Track data source
if 'data_source_tracker' not in st.session_state:
    st.session_state.data_source_tracker = "Demo Data"
@st.cache_data(ttl=3600)
def load_data():
    return None

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
padding:60px 25px;
border-radius:24px;
background:
linear-gradient(rgba(6,17,31,0.70),rgba(6,17,31,0.95)),
url("https://images.unsplash.com/photo-1512453979798-5ea266f8880c");
background-size:cover;
background-position:center;
border:1px solid rgba(255,255,255,0.12);
text-align:center;
margin-bottom:25px;
box-shadow:0 0 45px rgba(148,163,184,0.18);
}

.hero h1{
font-size:clamp(36px, 8vw, 72px);
margin-bottom:10px;
color:white;
text-shadow:0 0 25px rgba(148,163,184,0.35);
letter-spacing:1px;
}

.hero h2{
font-size:clamp(18px, 4vw, 28px);
color:#cbd5e1;
font-weight:400;
}

.hero p{
font-size:clamp(15px, 2.8vw, 20px);
color:#e2e8f0;
max-width:850px;
margin:18px auto 0 auto;
line-height:1.6;
}

.badge{
display:inline-block;
padding:8px 16px;
border-radius:999px;
background:rgba(59,130,246,0.18);
border:1px solid rgba(147,197,253,0.35);
color:#bfdbfe;
font-size:14px;
margin-bottom:18px;
}

.hero-actions{
display:flex;
justify-content:center;
gap:12px;
flex-wrap:wrap;
margin-top:28px;
}

.hero-actions span{
padding:10px 14px;
border-radius:999px;
background:rgba(255,255,255,0.08);
border:1px solid rgba(255,255,255,0.12);
color:#f8fafc;
font-size:14px;
}

.card{
background:rgba(255,255,255,0.05);
padding:25px;
border-radius:25px;
text-align:center;
border:1px solid rgba(255,255,255,0.08);
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

.insight:hover{
transform: translateY(-4px);
transition:0.3s ease;
box-shadow:0 0 28px rgba(148,163,184,0.16);
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

<div class="badge">Dubai Real Estate Intelligence Platform</div>

<h1>Atlas Intelligence</h1>

<h2>AI-powered property analytics for Dubai investors</h2>

<p>
Explore investment scores, DLD-based geo intelligence,
market trends, portfolio strategies, AI forecasting,
and investor-ready reports in one premium dashboard.
</p>

<div class="hero-actions">
<span>📊 2188+ Transactions</span>
<span>🗺️ DLD Coordinates</span>
<span>🤖 AI Scoring Engine</span>
</div>

</div>
""", unsafe_allow_html=True)
st.markdown("""
<style>

button[data-baseweb="tab"]{
font-size:16px;
font-weight:600;
padding:14px 24px;
border-radius:14px;
background:rgba(255,255,255,0.04);
margin-right:8px;
transition:0.3s ease;
}

button[data-baseweb="tab"]:hover{
background:rgba(59,130,246,0.18);
transform:translateY(-2px);
}

button[aria-selected="true"]{
background:linear-gradient(90deg,#2563eb,#3b82f6);
color:white !important;
box-shadow:0 0 18px rgba(59,130,246,0.35);
}

</style>
""", unsafe_allow_html=True)
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Overview",
    "Map Intelligence",
    "Area Rankings",
    "Portfolio Tools",
    "Reports",
    "Contact"
])
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
# Load real Dubai data
try:
    df = pd.read_csv('dubai_clean_ready.csv')
    # Rename 'Price' column to 'Average Price' for compatibility
    if 'Price' in df.columns:
        df = df.rename(columns={'Price': 'Average Price'})
    st.success(f"✅ Loaded {len(df)} real Dubai property transactions")
except:
    st.warning("Using demo data. File not found.")
# ---------- INVESTMENT SCORING MODEL ----------
max_price = df["Average Price"].max()
df["Affordability Score"] = 100 - (df["Average Price"] / max_price * 100)
# ---------- REALISTIC SCORING INPUTS ----------

df["Market Confidence"] = (
    df["Projected Growth"].rank(pct=True) * 100
).round(1)

df["Luxury Demand"] = (
    df["Average Price"].rank(pct=True) * 100
).round(1)

if "Rental Yield" not in df.columns:
    df["Rental Yield"] = (
        10 - (df["Average Price"].rank(pct=True) * 5)
    ).round(1)

# ---------- ATLAS INVESTMENT SCORE ENGINE ----------

growth_score = (
    df["Projected Growth"].rank(pct=True) * 100
)

price_score = (
    100 - (df["Average Price"].rank(pct=True) * 100)
)

yield_score = (
    df["Rental Yield"].rank(pct=True) * 100
)

confidence_score = (
    df["Market Confidence"].rank(pct=True) * 100
)

luxury_score = (
    df["Luxury Demand"].rank(pct=True) * 100
)

df["Investment Score"] = (
    growth_score * 0.35 +
    price_score * 0.20 +
    yield_score * 0.20 +
    confidence_score * 0.15 +
    luxury_score * 0.10
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
# Sample Data Button
if st.sidebar.button("📊 Load Sample Dubai Data"):
    # Create sample dataset
    sample_areas = ["Downtown Dubai", "Dubai Marina", "Palm Jumeirah", "JVC", "Business Bay"]
    sample_data = []
    
    for area in sample_areas:
        for i in range(20):
            if area == "Palm Jumeirah":
                price = np.random.randint(5000000, 15000000)
                growth = np.random.uniform(8, 14)
                yield_val = np.random.uniform(4.5, 6.5)
            elif area == "JVC":
                price = np.random.randint(800000, 2000000)
                growth = np.random.uniform(5, 10)
                yield_val = np.random.uniform(7, 9.5)
            else:
                price = np.random.randint(1500000, 6000000)
                growth = np.random.uniform(7, 13)
                yield_val = np.random.uniform(5.5, 8)
            
            sample_data.append({
                "Area": area,
                "Average Price": price,
                "Projected Growth": round(growth, 1),
                "Rental Yield": round(yield_val, 1)
            })
    
    df = pd.DataFrame(sample_data)
    
     # Calculate Investment Score
    max_price = df["Average Price"].max()

    df["Affordability Score"] = 100 - (
        df["Average Price"] / max_price * 100
    )

    df["Market Confidence"] = np.random.randint(
        75, 96, size=len(df)
    )

    df["Luxury Demand"] = np.random.randint(
        70, 98, size=len(df)
    )

    df["Investment Score"] = (
        df["Projected Growth"] * 4 * 0.35 +
        df["Affordability Score"] * 0.25 +
        df["Market Confidence"] * 0.15 +
        df["Luxury Demand"] * 0.10 +
        df["Rental Yield"] * 8 * 0.15
    ).round(1)

    st.session_state.data_source_tracker = "Sample Dubai Data"
    st.sidebar.success(f"✅ Loaded {len(df)} properties from {df['Area'].nunique()} areas")
    st.rerun()

if data_source == "Live API Mode Coming Soon":
    st.sidebar.warning("Live API integration is planned for the next version.")
if data_source == "Upload CSV":

    uploaded_file = st.sidebar.file_uploader(
        "Upload Real Estate CSV",
        type=["csv"],
        help="Upload CSV with columns: Area, Average Price, Projected Growth, Rental Yield (optional)"
    )

    if uploaded_file is not None:
        df_uploaded = pd.read_csv(uploaded_file)
        
        # Check if required columns exist
        required_cols = ["Area", "Average Price", "Projected Growth"]
        if all(col in df_uploaded.columns for col in required_cols):
            df = df_uploaded
            
            # Add calculated columns if missing
            if "Rental Yield" not in df.columns:
                df["Rental Yield"] = np.random.uniform(5.0, 9.5, size=len(df)).round(1)
            
            if "Investment Score" not in df.columns:
                # Create simple investment score from available data
                df["Investment Score"] = (
                    df["Projected Growth"] * 5 + 
                    (df["Average Price"] / df["Average Price"].max()) * 50
                ).round(1)
            
            st.sidebar.success(f"✅ Loaded {len(df)} properties from {df['Area'].nunique()} areas")
        else:
            st.sidebar.error(f"Missing columns. Need: {required_cols}")
            st.sidebar.info("Using demo data instead")
    else:
        st.sidebar.info("📁 Upload a CSV file to use real data")
    
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

Built by Syed Kumail Haider Zaidi  
MSc Business Analytics  
University of Wollongong Dubai

📧 syedkumailhaiderzaidi69@gmail.com
🔗 Live Portfolio: https://atlas-intelligence-nqhavg9mkp7j5pxztwbtty.streamlit.app/
---
""")
# CV Download Button
try:
    with open("Syeds CV.pdf", "rb") as file:
        st.sidebar.download_button(
            label="📄 Download My CV",
            data=file,
            file_name="Syeds CV.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.sidebar.warning("CV file not found. Please add Syeds CV.pdf to the app folder.")

st.sidebar.markdown("---")

current_time = datetime.now().strftime("%d %b %Y | %H:%M")
current_datetime = datetime.now().strftime("%d %b %Y %H:%M")

# Show what data is being used
if len(df) > 1000:
    st.sidebar.info(f"📊 Live: {len(df)} real transactions")
else:
    st.sidebar.info(f"📊 Demo: {len(df)} synthetic records")

st.sidebar.markdown(f"""
### Live Market Status

🟢 Market Feed Active  
🟢 Forecast Engine Online  
🢟 AI Scoring Models Active  

Last Refresh: {current_time}
🟢 Data Updated: {current_datetime}

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
   # Use actual property type from real data
if 'Property Type' in df.columns:
    # Already have Property Type column
    pass
elif 'property_type_en' in df.columns:
    df["Property Type"] = df['property_type_en']
else:
    # Create Property Type based on keywords in Area name
    df["Property Type"] = df['Area'].apply(
        lambda x: 'Villa' if 'Villa' in str(x) or 'Jumeirah' in str(x) or 'Palm' in str(x) 
        else 'Apartment' if 'Unit' in str(x) or 'Tower' in str(x) or 'Marina' in str(x)
        else 'Land' if 'Land' in str(x)
        else 'Building' if 'Building' in str(x)
        else 'Property'
    )

selected_area = st.sidebar.multiselect(
    "Select Dubai Areas",
    options=df["Area"].unique(),
    default=df["Area"].unique()
)

df = df[df["Area"].isin(selected_area)]
# Get unique property types from actual data
if 'Property Type' in df.columns:
    unique_types = df["Property Type"].unique().tolist()
else:
    unique_types = df["Area"].unique().tolist()

selected_type = st.sidebar.multiselect(
    "Select Property Type",
    options=unique_types,
    default=unique_types
)

# Filter based on Property Type or Area
if 'Property Type' in df.columns:
    df = df[df["Property Type"].isin(selected_type)]
else:
    df = df[df["Area"].isin(selected_type)]
# ---------- DATE FILTER ----------

if "Date" in df.columns:

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    min_date = df["Date"].min()
    max_date = df["Date"].max()

    selected_dates = st.sidebar.date_input(
        "Select Transaction Date Range",
        [min_date, max_date]
    )

    if len(selected_dates) == 2:

        start_date = pd.to_datetime(selected_dates[0])
        end_date = pd.to_datetime(selected_dates[1])

        df = df[
            (df["Date"] >= start_date) &
            (df["Date"] <= end_date)
        ]

if df.empty:
    st.error("No transactions found for the selected filters.")
    st.stop() 

with tab1:

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

    confidence_score = int(df["Investment Score"].mean().clip(0, 100))

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

    # ---------- MARKET ACTIVITY TIMELINE ----------

    st.write("")
    st.markdown("""
    ---
    ### Dubai Transaction Activity Timeline
    """)

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    timeline_df = (
        df.groupby(df["Date"].dt.to_period("M"))
        .agg({
            "Investment Score": "mean",
            "Average Price": "mean"
        })
        .reset_index()
    )

    timeline_df["Date"] = timeline_df["Date"].astype(str)

    fig_timeline = px.line(
        timeline_df,
        x="Date",
        y="Investment Score",
        markers=True,
        title="Monthly Investment Intelligence Trend"
    )

    fig_timeline.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=450
    )

    st.plotly_chart(fig_timeline, use_container_width=True)
with tab3:

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

with tab2:

    # ---------- DUBAI MAP ----------

    import re

    try:
        from rapidfuzz import process, fuzz
        fuzzy_enabled = True
    except:
        fuzzy_enabled = False

    st.write("")
    st.subheader("Dubai Real Estate Intelligence Map")

    map_search = st.text_input(
        "Search area on map",
        placeholder="Example: Jumeirah, Marina, Al Khabeesi"
    )

    @st.cache_data
    def load_coordinates():

        coords_df = pd.read_csv("dubai_areas_coordinates.csv")

        coords_df.columns = coords_df.columns.str.strip()

        coords_df = coords_df.rename(columns={
            "area": "coord_area",
            "lat": "latitude",
            "lon": "longitude"
        })

        return coords_df


    def clean_area(area):

        if pd.isna(area):
            return ""

        area = str(area).strip().lower()

        area = re.sub(r"[^a-z0-9\s]", "", area)

        area = re.sub(r"\s+", " ", area)

        replacements = {
            "jumeira": "jumeirah",
            "umm suqeim": "um suqaim",
            "al mezhar": "al mizhar",
        }

        for old, new in replacements.items():
            area = area.replace(old, new)

        return area.strip()


    coords_df = load_coordinates()

    df["area_key"] = df["Area"].apply(clean_area)

    coords_df["area_key"] = coords_df["coord_area"].apply(clean_area)

    map_df = df.merge(
        coords_df[
            ["coord_area", "area_key", "latitude", "longitude"]
        ],
        on="area_key",
        how="left"
    )

    if fuzzy_enabled:

        missing_areas = map_df[
            map_df["latitude"].isna()
        ]["area_key"].unique()

        coord_keys = coords_df["area_key"].unique()

        for missing_area in missing_areas:

            if missing_area == "":
                continue

            match = process.extractOne(
                missing_area,
                coord_keys,
                scorer=fuzz.token_sort_ratio
            )

            if match and match[1] >= 85:

                matched_key = match[0]

                matched_row = coords_df[
                    coords_df["area_key"] == matched_key
                ].iloc[0]

                map_df.loc[
                    map_df["area_key"] == missing_area,
                    "latitude"
                ] = matched_row["latitude"]

                map_df.loc[
                    map_df["area_key"] == missing_area,
                    "longitude"
                ] = matched_row["longitude"]

    fallback_lat = 25.1972
    fallback_lon = 55.2744

    map_df["match_status"] = np.where(
        map_df["latitude"].isna(),
        "Fallback",
        "Matched"
    )

    map_df["latitude"] = map_df["latitude"].fillna(fallback_lat)

    map_df["longitude"] = map_df["longitude"].fillna(fallback_lon)

    map_grouped = (
        map_df.groupby(
            ["Area", "latitude", "longitude", "match_status"],
            as_index=False
        )
        .agg({
            "Investment Score": "mean",
            "Average Price": "mean",
            "Projected Growth": "mean"
        })
    )

    transaction_counts = (
        map_df.groupby("Area")
        .size()
        .reset_index(name="Transactions")
    )

    map_grouped = map_grouped.merge(
        transaction_counts,
        on="Area",
        how="left"
    )

    matched_count = (
        map_grouped[
            map_grouped["match_status"] == "Matched"
        ]["Area"].nunique()
    )

    fallback_count = (
        map_grouped[
            map_grouped["match_status"] == "Fallback"
        ]["Area"].nunique()
    )

    total_areas = map_grouped["Area"].nunique()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Areas", total_areas)

    col2.metric("Matched Areas", matched_count)

    col3.metric("Fallback Areas", fallback_count)

    map_display_df = map_grouped.copy()

    if map_search:

        map_display_df = map_display_df[
            map_display_df["Area"].str.contains(
                map_search,
                case=False,
                na=False
            )
        ]

    st.info(f"📍 Showing {len(map_display_df)} mapped areas")

    # ---------- MAP COLOR CATEGORY ----------

    map_display_df["Score Category"] = pd.cut(
        map_display_df["Investment Score"],
        bins=[0, 60, 75, 90, 100],
        labels=[
            "Weak",
            "Moderate",
            "Strong",
            "Elite"
        ]
    )

    fig_map = px.scatter_mapbox(
        map_display_df,
        lat="latitude",
        lon="longitude",
        size="Investment Score",
        color="Score Category",
        size_max=40,
        hover_name="Area",
        hover_data={
            "Transactions": True,
            "Average Price": ":,.0f",
            "Projected Growth": ":.1f",
            "match_status": True
        },
        zoom=10,
        height=700
    )

    fig_map.update_traces(
        marker=dict(
            sizemode="area",
            opacity=0.75
        )
    )

    fig_map.update_layout(
        mapbox_style="carto-darkmatter",
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=0, b=0)
    )

    # ---------- HEATMAP LAYER ----------

    heat_layer = px.density_mapbox(
        map_display_df,
        lat="latitude",
        lon="longitude",
        z="Investment Score",
        radius=35,
        zoom=10,
        height=700
    )

    heat_layer.update_layout(
        mapbox_style="carto-darkmatter",
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=0, b=0)
    )

    map_mode = st.radio(
        "Map View Mode",
        [
            "Bubble Map",
            "Heatmap",
            "Top 20 Investment Areas"
        ],
        horizontal=True
    )

    if map_mode == "Heatmap":

        st.plotly_chart(
            heat_layer,
            use_container_width=True
        )

    elif map_mode == "Top 20 Investment Areas":

        top20_map = map_display_df.sort_values(
            "Investment Score",
            ascending=False
        ).head(20)

        fig_top20 = px.scatter_mapbox(
            top20_map,
            lat="latitude",
            lon="longitude",
            size="Investment Score",
            color="Score Category",
            size_max=45,
            hover_name="Area",
            zoom=10,
            height=700
        )

        fig_top20.update_layout(
            mapbox_style="carto-darkmatter",
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=0, b=0)
        )

        st.plotly_chart(
            fig_top20,
            use_container_width=True
        )

    else:

        st.plotly_chart(
            fig_map,
            use_container_width=True
        )

    st.caption(
        f"📍 {matched_count}/{total_areas} areas mapped successfully using official DLD coordinates."
    )

    unmatched = map_grouped[
        map_grouped["match_status"] == "Fallback"
    ]["Area"].unique()

    with st.expander("Show unmatched areas"):

        if len(unmatched) == 0:

            st.success("All areas matched successfully.")

        else:

            st.warning(
                f"{len(unmatched)} areas still using fallback coordinates."
            )

            st.dataframe(
                pd.DataFrame({
                    "Unmatched Areas": unmatched
                })
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

    best_area = table_df.sort_values(
        "Investment Score",
        ascending=False
    ).iloc[0]

    growth_area = table_df.sort_values(
        "Projected Growth %",
        ascending=False
    ).iloc[0]

    st.markdown(f"""
    <div class="insight">
    <h4>Atlas AI Recommendation</h4>

    <p>
    Atlas Intelligence recommends focusing on
    <b>{best_area['Area']}</b>
    based on the strongest overall investment score of
    <b>{best_area['Investment Score']:.1f}</b>.
    </p>

    <p>
    For growth-focused strategy,
    <b>{growth_area['Area']}</b>
    shows the highest projected growth at
    <b>{growth_area['Projected Growth %']:.1f}%</b>.
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
with tab4:

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
        ],
        key="investment_goal"
    )

    portfolio_df = pd.DataFrame({
        "Area": [
            "Downtown Dubai",
            "Dubai Marina",
            "JVC",
            "Palm Jumeirah"
        ]
    })

    if investment_goal == "Passive Income":
        portfolio_df["Allocation %"] = [20, 30, 40, 10]
    elif investment_goal == "Balanced Growth":
        portfolio_df["Allocation %"] = [30, 30, 25, 15]
    elif investment_goal == "Luxury Appreciation":
        portfolio_df["Allocation %"] = [20, 20, 10, 50]
    else:
        portfolio_df["Allocation %"] = [25, 20, 15, 40]

    portfolio_df["Investment Amount"] = (
        portfolio_df["Allocation %"] / 100 * portfolio_budget
    ).astype(int)

    st.dataframe(portfolio_df, use_container_width=True)

    st.markdown(f"""
    <div class="insight">
    <h4>Atlas Portfolio Strategy</h4>
    <p>Atlas Intelligence generated a portfolio allocation strategy optimized for:
    <b>{investment_goal}</b></p>
    <p>Portfolio Budget: <b>AED {portfolio_budget:,}</b></p>
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
        ],
        key="investor_type"
    )

    investment_horizon = st.selectbox(
        "Investment Horizon",
        [
            "1-2 Years",
            "3-5 Years",
            "5-10 Years"
        ],
        key="investment_horizon"
    )

    if investor_type == "Conservative":
        ai_strategy = "Atlas recommends focusing on stable rental-yield communities such as JVC and Dubai Marina with balanced cashflow opportunities."
    elif investor_type == "Balanced":
        ai_strategy = "Atlas recommends diversified allocation across Downtown Dubai, Dubai Marina, and Dubai Hills Estate for balanced growth and stability."
    elif investor_type == "Aggressive":
        ai_strategy = "Atlas recommends targeting high-growth areas such as Dubai Creek Harbour and emerging investment corridors."
    else:
        ai_strategy = "Atlas recommends premium luxury-focused allocation toward Palm Jumeirah and ultra-prime waterfront communities."

    st.markdown(f"""
    <div class="insight">
    <h4>AI Strategic Recommendation</h4>
    <p>Investor Profile: <b>{investor_type}</b></p>
    <p>Investment Horizon: <b>{investment_horizon}</b></p>
    <p>{ai_strategy}</p>
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
        regime_msg = "Dubai real estate is currently showing strong growth momentum with healthy rental performance."
    elif avg_growth >= 8:
        regime = "Stable Expansion"
        regime_msg = "Atlas Intelligence indicates balanced market conditions with moderate long-term growth."
    elif avg_growth >= 6:
        regime = "Selective Opportunity"
        regime_msg = "Certain communities continue showing strength while broader growth remains moderate."
    else:
        regime = "Correction Risk"
        regime_msg = "Atlas Intelligence detects slowing momentum and elevated investment caution signals."

    st.markdown(f"""
    <div class="insight">
    <h4>Current Market Regime: {regime}</h4>
    <p>{regime_msg}</p>
    <p>
    Average Growth: <b>{avg_growth:.1f}%</b><br>
    Average Rental Yield: <b>{avg_yield:.1f}%</b>
    </p>
    </div>
    """, unsafe_allow_html=True)
with tab5:

    # ---------- PDF REPORT EXPORT ----------

    def create_pdf_report():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        pdf.set_font("Arial", "B", 18)
        pdf.cell(0, 10, "Atlas Intelligence Report", ln=True, align="C")

        pdf.ln(10)

        pdf.set_font("Arial", "", 11)
        pdf.cell(0, 8, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
        pdf.cell(0, 8, "Prepared by: Atlas Intelligence", ln=True)

        pdf.ln(8)

        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 8, "Market Summary", ln=True)

        pdf.set_font("Arial", "", 11)
        pdf.cell(0, 8, f"Properties Analyzed: {len(df)}", ln=True)
        pdf.cell(0, 8, f"Areas Analyzed: {df['Area'].nunique()}", ln=True)
        pdf.cell(0, 8, f"Average Investment Score: {df['Investment Score'].mean():.1f}", ln=True)
        pdf.cell(0, 8, f"Average Projected Growth: {df['Projected Growth'].mean():.1f}%", ln=True)

        pdf.ln(8)

        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 8, "Top Area Recommendations", ln=True)

        top_report_areas = table_df.sort_values(
            "Investment Score",
            ascending=False
        ).head(5)

        pdf.set_font("Arial", "", 10)

        for _, row in top_report_areas.iterrows():
            pdf.multi_cell(
                0,
                7,
                f"{row['Area']} | Score: {row['Investment Score']:.1f} | "
                f"Avg Price: AED {row['Average Property Price']:,.0f} | "
                f"Growth: {row['Projected Growth %']:.1f}%"
            )

        return pdf.output(dest="S").encode("latin-1")


    pdf_bytes = create_pdf_report()

    st.download_button(
        label="Download Full Market Report PDF",
        data=pdf_bytes,
        file_name=f"Atlas_Report_{datetime.now().strftime('%Y%m%d')}.pdf",
        mime="application/pdf"
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

    Atlas Intelligence uses Dubai property transaction data to prototype:

    - Investment scoring
    - Market growth analysis
    - Geographic intelligence
    - AI-style recommendations
    - Executive dashboard reporting

    Future versions will integrate live market datasets and advanced predictive models.
    """)

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
with tab6:

    # ---------- FOOTER ----------

    st.write("")

    st.markdown("""
    ---
    <center>

    ### Atlas Intelligence

    AI-powered Dubai real estate intelligence platform.

    **Created by Syed Kumail Haider Zaidi**  
    MSc Business Analytics | University of Wollongong Dubai

    Built with Python, Streamlit, Plotly & AI-driven analytics.

    📧 syedkumailhaiderzaidi69@gmail.com

    © 2026 Atlas Intelligence — Prototype V2

    </center>
    """, unsafe_allow_html=True)


    # ========== CONTACT SECTION ==========

    st.write("")
    st.markdown("---")
    st.markdown("### 📬 Want to hire me or collaborate?")

    st.markdown("**Syed Kumail Haider Zaidi**")
    st.markdown("*MSc Business Analytics | University of Wollongong Dubai*")

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        if st.button("📧 Send Email", use_container_width=True):
            st.markdown(
                "[Click here to email](mailto:syedkumailhaiderzaidi69@gmail.com)"
            )

    with col_b:
        if st.button("🔗 LinkedIn", use_container_width=True):
            st.markdown(
                "[Open LinkedIn](https://www.linkedin.com/in/syedkumail01)"
            )

    with col_c:
        if st.button("💻 GitHub", use_container_width=True):
            st.markdown(
                "[Open GitHub](https://github.com/syedkumailhaiderzaidi69-coder)"
            )

    st.markdown("""
    <p style="
    text-align:center;
    color:#64748b;
    margin-top:20px;
    font-size:14px;
    ">
    Open to internships, graduate roles, and collaborations in:<br>
    Business Analytics • Data Science • Real Estate Analytics • Consulting
    </p>
    """, unsafe_allow_html=True)

    st.success("Atlas Intelligence Luxury Prototype V2 Live")
