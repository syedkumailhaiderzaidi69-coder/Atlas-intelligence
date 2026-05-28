import streamlit as st

st.set_page_config(page_title="Atlas Intelligence", layout="wide")

st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#06111f,#0b1628,#111827);
color:white;
}

.hero{
padding:80px;
border-radius:30px;
background:rgba(15,23,42,0.85);
border:1px solid rgba(255,255,255,0.1);
text-align:center;
}

.hero h1{
font-size:70px;
margin-bottom:10px;
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

.card h3{
font-size:40px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>Atlas Intelligence</h1>
<h2>The Future of Dubai Intelligence</h2>
<p>AI-powered Dubai real estate intelligence platform built by Syed.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

c1,c2,c3 = st.columns(3)

c1.markdown("""
<div class="card">
<h3>350+</h3>
<p>Properties Analyzed</p>
</div>
""", unsafe_allow_html=True)

c2.markdown("""
<div class="card">
<h3>14</h3>
<p>Dubai Areas Covered</p>
</div>
""", unsafe_allow_html=True)

c3.markdown("""
<div class="card">
<h3>AI</h3>
<p>Market Intelligence Engine</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.subheader("Executive Vision")

st.write("""
Atlas Intelligence is an AI-powered Dubai real estate intelligence platform focused on investment analytics, market intelligence, and executive-level dashboards.
""")

st.success("Luxury prototype V1 live.")
