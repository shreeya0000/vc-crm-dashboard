import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import os
import numpy as np

st.set_page_config(
    page_title="Vacheron Constantin CRM",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@300;400;500&family=Raleway:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Raleway', sans-serif;
    background-color: #0D1B2A;
}
.stApp { background-color: #0D1B2A; }

[data-testid="stSidebar"] {
    background-color: #091422;
    border-right: 1px solid rgba(184,150,46,0.2);
}
[data-testid="stSidebar"] * {
    color: #C8D0D8 !important;
    font-family: 'Raleway', sans-serif !important;
}

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0D1B2A; }
::-webkit-scrollbar-thumb { background: #B8962E; border-radius: 2px; }

.brand-header {
    text-align: center;
    padding: 56px 0 40px 0;
    border-bottom: 1px solid rgba(184,150,46,0.3);
    margin-bottom: 48px;
    animation: fadeInDown 1s ease forwards;
}
.brand-name {
    font-family: 'EB Garamond', serif;
    font-size: 52px;
    font-weight: 300;
    letter-spacing: 0.6em;
    color: #FFFFFF;
    margin: 0;
    line-height: 1;
}
.brand-subtitle {
    font-family: 'Raleway', sans-serif;
    font-size: 9px;
    font-weight: 500;
    letter-spacing: 0.4em;
    color: #B8962E;
    margin-top: 14px;
    text-transform: uppercase;
}
.brand-year {
    font-family: 'EB Garamond', serif;
    font-size: 11px;
    color: rgba(184,150,46,0.5);
    letter-spacing: 0.3em;
    margin-top: 8px;
}
.maltese-cross {
    font-size: 18px;
    color: #B8962E;
    display: block;
    margin: 12px auto 0 auto;
    letter-spacing: 0.5em;
    opacity: 0.7;
}

.section-title {
    font-family: 'EB Garamond', serif;
    font-size: 26px;
    font-weight: 400;
    color: #FFFFFF;
    letter-spacing: 0.08em;
    margin-bottom: 2px;
}
.section-sub {
    font-size: 9px;
    color: #B8962E;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    margin-bottom: 24px;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #112236 0%, #0D1B2A 100%);
    border: 1px solid rgba(184,150,46,0.25);
    border-top: 2px solid #B8962E;
    border-radius: 0px;
    padding: 24px 20px;
    transition: all 0.3s ease;
}
[data-testid="stMetric"]:hover {
    border-color: rgba(184,150,46,0.6);
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(184,150,46,0.1);
}
[data-testid="stMetricLabel"] {
    font-size: 9px !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
    color: #B8962E !important;
    font-family: 'Raleway', sans-serif !important;
    white-space: normal !important;
    overflow: visible !important;
    text-overflow: unset !important;
    word-break: break-word !important;
}
[data-testid="stMetricValue"] {
    font-family: 'EB Garamond', serif !important;
    font-size: 28px !important;
    font-weight: 400 !important;
    color: #FFFFFF !important;
    white-space: normal !important;
    overflow: visible !important;
}

.narrative-block {
    background: linear-gradient(135deg, #112236 0%, #0D1B2A 100%);
    border: 1px solid rgba(184,150,46,0.2);
    border-left: 2px solid #B8962E;
    padding: 20px 24px;
    margin: 12px 0 28px 0;
    font-size: 13px;
    line-height: 1.9;
    color: #A8B4C0;
}
.narrative-block strong { color: #FFFFFF; font-weight: 500; }

.insight-tag {
    display: inline-block;
    font-size: 9px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    padding: 3px 12px;
    margin-bottom: 10px;
    font-family: 'Raleway', sans-serif;
    border: 1px solid currentColor;
}
.tag-gold  { color: #B8962E; background: transparent; }
.tag-alert { color: #E05C5C; background: transparent; }
.tag-green { color: #5CA88E; background: transparent; }
.tag-blue  { color: #5C8EA8; background: transparent; }

.health-card {
    background: linear-gradient(135deg, #112236 0%, #0D1B2A 100%);
    border: 1px solid rgba(184,150,46,0.2);
    padding: 24px 16px;
    text-align: center;
    transition: all 0.4s ease;
}
.health-card:hover {
    border-color: rgba(184,150,46,0.5);
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(184,150,46,0.08);
}
.health-boutique {
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #B8962E;
    margin-bottom: 12px;
    line-height: 1.4;
    min-height: 28px;
}
.health-score {
    font-family: 'EB Garamond', serif;
    font-size: 52px;
    font-weight: 300;
    line-height: 1;
    margin-bottom: 6px;
}
.health-status {
    font-size: 10px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 6px;
    font-weight: 500;
}
.health-detail {
    font-size: 10px;
    color: #6A7A8A;
    line-height: 1.6;
    margin-top: 10px;
    text-align: left;
}
.health-bar-bg {
    background: rgba(255,255,255,0.05);
    height: 2px;
    margin-top: 12px;
    border-radius: 1px;
}
.health-bar-fill {
    height: 2px;
    border-radius: 1px;
}

.campaign-card {
    background: linear-gradient(135deg, #112236 0%, #0D1B2A 100%);
    border: 1px solid rgba(184,150,46,0.2);
    padding: 24px;
    margin-bottom: 12px;
    transition: all 0.3s ease;
}
.campaign-card:hover {
    border-color: rgba(184,150,46,0.5);
    box-shadow: 0 8px 32px rgba(184,150,46,0.08);
}
.campaign-name {
    font-family: 'EB Garamond', serif;
    font-size: 17px;
    color: #FFFFFF;
    letter-spacing: 0.05em;
    margin-bottom: 14px;
}
.campaign-stat {
    display: flex;
    justify-content: space-between;
    padding: 7px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    font-size: 11px;
    color: #A8B4C0;
    letter-spacing: 0.03em;
}
.campaign-stat span { color: #FFFFFF; font-weight: 500; }

.rec-card {
    background: linear-gradient(135deg, #112236 0%, #0D1B2A 100%);
    border: 1px solid rgba(184,150,46,0.2);
    padding: 28px 24px;
    height: 100%;
    transition: all 0.3s ease;
}
.rec-card:hover {
    border-color: rgba(184,150,46,0.5);
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(184,150,46,0.08);
}
.rec-number {
    font-family: 'EB Garamond', serif;
    font-size: 52px;
    font-weight: 300;
    color: rgba(184,150,46,0.3);
    line-height: 1;
    margin-bottom: 8px;
}
.rec-card-title {
    font-family: 'EB Garamond', serif;
    font-size: 18px;
    font-weight: 400;
    color: #FFFFFF;
    margin-bottom: 20px;
    letter-spacing: 0.05em;
}
.rec-card ul { margin: 0; padding: 0; list-style: none; color: #A8B4C0; font-size: 12px; }
.rec-card li {
    padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    letter-spacing: 0.03em;
    transition: color 0.2s ease;
}
.rec-card li:hover { color: #FFFFFF; }
.rec-card li:last-child { border-bottom: none; }

.client-result-box {
    background: linear-gradient(135deg, #112236 0%, #0D1B2A 100%);
    border: 1px solid rgba(184,150,46,0.3);
    border-left: 3px solid #B8962E;
    padding: 24px 28px;
    margin-bottom: 32px;
    animation: fadeInLeft 0.5s ease forwards;
}

.waitlist-row {
    background: linear-gradient(135deg, #112236 0%, #0D1B2A 100%);
    border: 1px solid rgba(184,150,46,0.15);
    border-left: 2px solid #B8962E;
    padding: 12px 16px;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s ease;
}
.waitlist-row:hover {
    border-color: rgba(184,150,46,0.5);
    padding-left: 20px;
}
.waitlist-product {
    font-size: 11px;
    color: #C8D0D8;
    letter-spacing: 0.03em;
    line-height: 1.4;
    flex: 1;
    padding-right: 12px;
}
.waitlist-count {
    font-family: 'EB Garamond', serif;
    font-size: 22px;
    color: #B8962E;
    flex-shrink: 0;
}
.waitlist-label {
    font-size: 8px;
    color: #6A7A8A;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    display: block;
    text-align: right;
}

.thin-divider {
    border: none;
    border-top: 1px solid rgba(184,150,46,0.15);
    margin: 44px 0;
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInLeft {
    from { opacity: 0; transform: translateX(-20px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes pulse {
    0%   { opacity: 1; }
    50%  { opacity: 0.4; }
    100% { opacity: 1; }
}
.pulse { animation: pulse 2s infinite; }

.stDataFrame { border: 1px solid rgba(184,150,46,0.2) !important; }
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

VC_GOLD  = "#B8962E"
VC_DARK  = "#0D1B2A"
VC_NAVY  = "#112236"
VC_WHITE = "#FFFFFF"

SEGMENT_COLORS = {
    "Champion":   "#B8962E",
    "Loyal":      "#5CA88E",
    "New Client": "#5C8EA8",
    "At Risk":    "#E05C5C",
    "Lost":       "#4A5A6A",
}

BOUTIQUE_COLORS = ["#B8962E", "#5CA88E", "#5C8EA8", "#E05C5C", "#8E5CA8"]

base = "data/processed" if os.path.exists("data/processed/rfm_data.csv") else "."

@st.cache_data
def load_rfm():     return pd.read_csv(f"{base}/rfm_data.csv")
@st.cache_data
def load_monthly(): return pd.read_csv(f"{base}/monthly_revenue.csv")
@st.cache_data
def load_products(): return pd.read_csv(f"{base}/top_products.csv")
@st.cache_data
def load_kpis():
    with open(f"{base}/kpis.json") as f: return json.load(f)

rfm      = load_rfm()
monthly  = load_monthly()
products = load_products()
kpis     = load_kpis()

@st.cache_data
def enrich_rfm(rfm):
    np.random.seed(42)
    boutiques = ["Geneva", "New York", "Hong Kong", "Paris", "Dubai"]
    rfm = rfm.copy()
    rfm["Boutique"]    = np.random.choice(boutiques, size=len(rfm), p=[0.25,0.30,0.20,0.15,0.10])
    rfm["LoyaltyTier"] = rfm["Monetary"].apply(lambda m:
        "Connoisseur" if m >= 5000 else
        "Collector"   if m >= 2000 else
        "Enthusiast"  if m >= 800  else "Initiate")
    rfm["ClientType"]  = rfm["Frequency"].apply(lambda f: "Retention" if f > 1 else "Acquisition")
    rfm["DataScore"]   = np.random.randint(60, 100, size=len(rfm))
    campaigns = ["Overseas Launch — Email", "Les Cabinotiers Event", "Patrimony Reissue — Email", "VIP Client Evening", "Holiday Gifting — Email"]
    rfm["LastCampaign"]      = np.random.choice(campaigns, size=len(rfm))
    rfm["CampaignOpened"]    = np.random.choice([True, False], size=len(rfm), p=[0.42, 0.58])
    rfm["CampaignConverted"] = rfm["CampaignOpened"] & np.random.choice([True, False], size=len(rfm), p=[0.28, 0.72])
    return rfm

rfm = enrich_rfm(rfm)

total_clients    = rfm["Customer ID"].nunique()
champion_pct     = round(len(rfm[rfm["Segment"] == "Champion"]) / total_clients * 100, 1)
at_risk_pct      = round(len(rfm[rfm["Segment"] == "At Risk"]) / total_clients * 100, 1)
at_risk_count    = len(rfm[rfm["Segment"] == "At Risk"])
champion_rev     = rfm[rfm["Segment"] == "Champion"]["Monetary"].sum()
total_rev        = rfm["Monetary"].sum()
champion_rev_pct = round(champion_rev / total_rev * 100, 1)
peak_month       = monthly.loc[monthly["TotalSpend"].idxmax(), "Month"]
peak_val         = monthly["TotalSpend"].max()
retention_pct    = round(len(rfm[rfm["ClientType"] == "Retention"]) / total_clients * 100, 1)
acquisition_pct  = round(100 - retention_pct, 1)
open_rate        = round(rfm["CampaignOpened"].mean() * 100, 1)
conv_rate        = round(rfm["CampaignConverted"].mean() * 100, 1)

LEGEND_STYLE = dict(
    font=dict(size=11, color="#FFFFFF"),
    bgcolor="rgba(17,34,54,0.8)",
    bordercolor="rgba(184,150,46,0.3)",
    borderwidth=1
)

CHART_LAYOUT = dict(
    paper_bgcolor=VC_NAVY,
    plot_bgcolor=VC_NAVY,
    font=dict(family="Raleway", color="#FFFFFF", size=11),
    xaxis=dict(gridcolor="rgba(255,255,255,0.05)", color="#FFFFFF", title_font=dict(color="#FFFFFF")),
    yaxis=dict(gridcolor="rgba(255,255,255,0.05)", color="#FFFFFF", title_font=dict(color="#FFFFFF")),
    margin=dict(t=50, b=30)
)

# ── SIDEBAR ────────────────────────────────────────────────
with st.sidebar:
    st.markdown("<div style='padding:28px 0 4px;font-family:EB Garamond,serif;font-size:20px;letter-spacing:0.4em;color:#FFFFFF;'>VACHERON</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:EB Garamond,serif;font-size:20px;letter-spacing:0.4em;color:#FFFFFF;padding-bottom:4px;'>CONSTANTIN</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:8px;letter-spacing:0.3em;text-transform:uppercase;color:#B8962E;padding-bottom:20px;'>Est. 1755 · Geneva</div>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color:rgba(184,150,46,0.2);margin-bottom:20px;'>", unsafe_allow_html=True)

    st.markdown("<p style='font-size:9px;letter-spacing:.2em;text-transform:uppercase;color:#B8962E;margin-bottom:4px;'>Client Search</p>", unsafe_allow_html=True)
    search_id = st.text_input("", placeholder="Enter Customer ID", label_visibility="collapsed")
    st.markdown("<p style='font-size:10px;color:rgba(255,255,255,0.25);letter-spacing:.03em;margin-top:-12px;'>e.g. 14911, 16754, 13047</p>", unsafe_allow_html=True)

    st.markdown("<p style='font-size:9px;letter-spacing:.2em;text-transform:uppercase;color:#B8962E;margin:16px 0 4px;'>Segment</p>", unsafe_allow_html=True)
    segments = ["All"] + sorted(rfm["Segment"].unique().tolist())
    selected_segment = st.selectbox("", segments, label_visibility="collapsed")

    st.markdown("<p style='font-size:9px;letter-spacing:.2em;text-transform:uppercase;color:#B8962E;margin:16px 0 4px;'>Boutique</p>", unsafe_allow_html=True)
    boutiques = ["All"] + sorted(rfm["Boutique"].unique().tolist())
    selected_boutique = st.selectbox(" ", boutiques, label_visibility="collapsed")

    st.markdown("<p style='font-size:9px;letter-spacing:.2em;text-transform:uppercase;color:#B8962E;margin:16px 0 4px;'>Client Tier</p>", unsafe_allow_html=True)
    tiers = ["All", "Connoisseur", "Collector", "Enthusiast", "Initiate"]
    selected_tier = st.selectbox("  ", tiers, label_visibility="collapsed")

    st.markdown("<hr style='border-color:rgba(184,150,46,0.2);margin:20px 0;'>", unsafe_allow_html=True)
    csv_export = rfm.to_csv(index=False).encode("utf-8")
    st.download_button("Export Client List", csv_export, "vc_client_data.csv", "text/csv", use_container_width=True)
    st.markdown("<hr style='border-color:rgba(184,150,46,0.2);margin:20px 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size:9px;color:rgba(255,255,255,0.25);letter-spacing:.08em;margin-bottom:16px;'>CRM Analytics Portfolio<br>Built with Python and Streamlit</p>
    <div style='border-top:1px solid rgba(184,150,46,0.2);padding-top:16px;'>
        <p style='font-size:9px;color:rgba(184,150,46,0.5);letter-spacing:0.12em;margin-bottom:4px;text-transform:uppercase;'>Made with love by</p>
        <p style='font-family:EB Garamond,serif;font-size:16px;color:#FFFFFF;letter-spacing:0.1em;margin-bottom:8px;'>Shreeya Aggarwal</p>
        <a href='mailto:sa9172@nyu.edu' style='display:block;font-size:10px;color:rgba(255,255,255,0.4);letter-spacing:0.04em;margin-bottom:4px;text-decoration:none;'>sa9172@nyu.edu</a>
        <a href='https://aesthetic-canvas-sparkle.lovable.app' target='_blank' style='display:block;font-size:10px;color:#B8962E;letter-spacing:0.04em;text-decoration:none;'>Portfolio</a>
    </div>
    """, unsafe_allow_html=True)

# ── FILTERS ────────────────────────────────────────────────
rfm_f = rfm.copy()
if selected_segment != "All":  rfm_f = rfm_f[rfm_f["Segment"] == selected_segment]
if selected_boutique != "All": rfm_f = rfm_f[rfm_f["Boutique"] == selected_boutique]
if selected_tier != "All":     rfm_f = rfm_f[rfm_f["LoyaltyTier"] == selected_tier]

# ── HEADER ─────────────────────────────────────────────────
st.markdown("""
<div class='brand-header'>
    <div class='brand-name'>VACHERON CONSTANTIN</div>
    <div class='brand-subtitle'>CRM & Client Intelligence — Americas Region</div>
    <div class='brand-year'>Founded Geneva, 1755 · Maison de Haute Horlogerie</div>
    <div class='maltese-cross'>✦ ✦ ✦</div>
</div>
""", unsafe_allow_html=True)

# ── CLIENT SEARCH ──────────────────────────────────────────
if search_id:
    try:
        cid = float(search_id)
        c_rfm = rfm[rfm["Customer ID"] == cid]
        if c_rfm.empty:
            st.warning("No client found with that ID.")
        else:
            row = c_rfm.iloc[0]
            st.markdown(f"""
            <div class='client-result-box' id='client-result'>
                <div style='font-size:9px;letter-spacing:0.25em;text-transform:uppercase;color:#B8962E;margin-bottom:10px;'>Client Record Located</div>
                <div style='font-family:EB Garamond,serif;font-size:28px;font-weight:400;color:#FFFFFF;margin-bottom:8px;'>Customer {search_id}</div>
                <div style='font-size:11px;color:rgba(255,255,255,0.5);letter-spacing:0.08em;'>
                    {row['Boutique']} &nbsp;✦&nbsp; {row['LoyaltyTier']} Tier &nbsp;✦&nbsp; {row['Segment']} &nbsp;✦&nbsp; Last Campaign: {row['LastCampaign']}
                </div>
            </div>
            <script>
                window.addEventListener('load', function() {{
                    document.getElementById('client-result').scrollIntoView({{behavior:'smooth'}});
                }});
            </script>
            """, unsafe_allow_html=True)
            cc1, cc2, cc3, cc4, cc5 = st.columns(5)
            cc1.metric("Segment",             row["Segment"])
            cc2.metric("Days Since Purchase",  int(row["Recency"]))
            cc3.metric("Total Orders",         int(row["Frequency"]))
            cc4.metric("Lifetime Value",       f"£{row['Monetary']:,.0f}")
            cc5.metric("Data Score",           f"{row['DataScore']}/100")
            st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)
    except:
        st.warning("Please enter a valid numeric Customer ID.")

# ── EXECUTIVE SUMMARY ──────────────────────────────────────
st.markdown("<div class='section-title'>Executive Summary</div><div class='section-sub'>Americas region — full client database</div>", unsafe_allow_html=True)
st.markdown(f"""
<div class='narrative-block'>
    <strong>{total_clients:,} active clients</strong> across five global Maison locations.
    Champion clients represent <strong>{champion_pct}% of the base</strong> and drive <strong>{champion_rev_pct}% of revenue</strong>.
    Retention stands at <strong>{retention_pct}%</strong> with a campaign open rate of <strong>{open_rate}%</strong> and conversion rate of <strong>{conv_rate}%</strong>.
    <strong class='pulse' style='color:#E05C5C;'>{at_risk_count:,} clients require immediate re-engagement.</strong>
</div>
""", unsafe_allow_html=True)

# ── KPIs ───────────────────────────────────────────────────
st.markdown("<div class='section-title'>Key Performance Indicators</div><div class='section-sub'>Live metrics — filtered view</div>", unsafe_allow_html=True)
k1, k2, k3, k4, k5, k6 = st.columns(6)
k1.metric("Total Revenue",      f"£{kpis['total_revenue']:,.0f}")
k2.metric("Unique Clients",     f"{kpis['unique_clients']:,}")
k3.metric("Total Orders",       f"{kpis['total_orders']:,}")
k4.metric("Avg Order Value",    f"£{kpis['avg_order_value']:,.2f}")
k5.metric("Retention Rate",     f"{retention_pct}%")
k6.metric("Campaign Open Rate", f"{open_rate}%")

st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)

# ── CRM HEALTH SCORES ──────────────────────────────────────
st.markdown("<div class='section-title'>Boutique CRM Health</div><div class='section-sub'>Composite score — data quality (40%) · retention (35%) · campaign engagement (25%)</div>", unsafe_allow_html=True)

boutique_list = sorted(rfm["Boutique"].unique())
health_cols   = st.columns(len(boutique_list))

for col, boutique in zip(health_cols, boutique_list):
    b_data       = rfm[rfm["Boutique"] == boutique]
    data_score   = round(b_data["DataScore"].mean())
    ret_score    = round(len(b_data[b_data["ClientType"] == "Retention"]) / len(b_data) * 100)
    engage_score = round(b_data["CampaignOpened"].mean() * 100)
    health       = round((data_score * 0.4) + (ret_score * 0.35) + (engage_score * 0.25))
    color        = "#5CA88E" if health >= 75 else "#B8962E" if health >= 60 else "#E05C5C"
    status       = "Excellent" if health >= 75 else "Good" if health >= 60 else "Needs Attention"

    col.markdown(f"""
    <div class='health-card'>
        <div class='health-boutique'>{boutique}</div>
        <div class='health-score' style='color:{color};'>{health}<span style='font-size:18px;color:rgba(255,255,255,0.3);'>/100</span></div>
        <div class='health-status' style='color:{color};'>{status}</div>
        <div class='health-detail'>
            Data Quality: {data_score}/100<br>
            Retention Rate: {ret_score}%<br>
            Campaign Engagement: {engage_score}%
        </div>
        <div class='health-bar-bg'>
            <div class='health-bar-fill' style='width:{health}%;background:{color};'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div class='narrative-block'>
    <span class='insight-tag tag-gold'>How to read this</span><br>
    Each boutique is scored out of 100 based on three weighted components:
    <strong>Data Capture Quality (40%)</strong> — how completely client records are filled in,
    <strong>Retention Rate (35%)</strong> — the share of clients who have purchased more than once, and
    <strong>Campaign Engagement (25%)</strong> — the share of clients who opened their last campaign.
    Green indicates excellent CRM health (75+). Gold indicates good but improvable (60-74). Red requires immediate CRM enablement support (below 60).
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)

# ── CAMPAIGN PERFORMANCE ───────────────────────────────────
st.markdown("<div class='section-title'>Campaign Performance</div><div class='section-sub'>Email and event campaign analytics — reach, engagement, and revenue</div>", unsafe_allow_html=True)

campaigns_list = rfm["LastCampaign"].unique()
camp_data = []
for c in campaigns_list:
    c_df = rfm[rfm["LastCampaign"] == c]
    camp_data.append({
        "Campaign":   c,
        "Reach":      len(c_df),
        "Open Rate":  round(c_df["CampaignOpened"].mean() * 100, 1),
        "Conv Rate":  round(c_df["CampaignConverted"].mean() * 100, 1),
        "Revenue":    round(c_df[c_df["CampaignConverted"] == True]["Monetary"].sum()),
        "Type":       "Event" if "Event" in c or "Evening" in c else "Email"
    })
camp_df = pd.DataFrame(camp_data).sort_values("Revenue", ascending=False)

ca, cb = st.columns(2)
with ca:
    for _, row in camp_df.iterrows():
        type_color = "#B8962E" if row["Type"] == "Event" else "#5C8EA8"
        st.markdown(f"""
        <div class='campaign-card'>
            <div style='display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;'>
                <div class='campaign-name'>{row['Campaign']}</div>
                <span class='insight-tag' style='color:{type_color};border-color:{type_color};margin:0;font-size:8px;'>{row['Type']}</span>
            </div>
            <div class='campaign-stat'>Clients Reached <span>{row['Reach']:,}</span></div>
            <div class='campaign-stat'>Open Rate <span>{row['Open Rate']}%</span></div>
            <div class='campaign-stat'>Conversion Rate <span>{row['Conv Rate']}%</span></div>
            <div class='campaign-stat'>Revenue Generated <span>£{row['Revenue']:,}</span></div>
        </div>
        """, unsafe_allow_html=True)

with cb:
    fig_c1 = px.bar(camp_df, x="Revenue", y="Campaign", orientation="h",
                    title="Revenue Generated by Campaign",
                    color="Type",
                    color_discrete_map={"Event": "#B8962E", "Email": "#5C8EA8"})
    fig_c1.update_layout(
        paper_bgcolor=VC_NAVY, plot_bgcolor=VC_NAVY,
        font=dict(family="Raleway", color="#FFFFFF", size=11),
        title=dict(font=dict(family="EB Garamond", size=17, color="#FFFFFF")),
        legend=dict(**LEGEND_STYLE),
        xaxis=dict(title="Revenue (£)", gridcolor="rgba(255,255,255,0.05)", color="#FFFFFF"),
        yaxis=dict(title="", color="#FFFFFF"),
        margin=dict(t=50, b=30)
    )
    st.plotly_chart(fig_c1, use_container_width=True)

    fig_c2 = px.scatter(camp_df, x="Open Rate", y="Conv Rate", size="Reach",
                        text="Campaign", color="Type",
                        title="Open Rate vs Conversion Rate",
                        color_discrete_map={"Event": "#B8962E", "Email": "#5C8EA8"})
    fig_c2.update_traces(textposition="top center", textfont=dict(size=9, color="#FFFFFF"))
    fig_c2.update_layout(
        paper_bgcolor=VC_NAVY, plot_bgcolor=VC_NAVY,
        font=dict(family="Raleway", color="#FFFFFF", size=11),
        title=dict(font=dict(family="EB Garamond", size=17, color="#FFFFFF")),
        legend=dict(**LEGEND_STYLE),
        xaxis=dict(title="Open Rate (%)", gridcolor="rgba(255,255,255,0.05)", color="#FFFFFF"),
        yaxis=dict(title="Conversion Rate (%)", gridcolor="rgba(255,255,255,0.05)", color="#FFFFFF"),
        margin=dict(t=50, b=30)
    )
    st.plotly_chart(fig_c2, use_container_width=True)

st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)

# ── DATA CAPTURE QUALITY ───────────────────────────────────
st.markdown("<div class='section-title'>Data Capture Quality</div><div class='section-sub'>How completely client records are filled in across each boutique — scored 0 to 100</div>", unsafe_allow_html=True)

quality_data = rfm.groupby("Boutique").agg(
    Score=("DataScore", "mean"),
    Clients=("Customer ID", "nunique")
).reset_index()
quality_data["Score"]  = quality_data["Score"].round(1)
quality_data["Status"] = quality_data["Score"].apply(
    lambda s: "Compliant" if s >= 80 else "Needs Review" if s >= 65 else "Non-Compliant"
)
quality_data["Color"] = quality_data["Score"].apply(
    lambda s: "#5CA88E" if s >= 80 else "#B8962E" if s >= 65 else "#E05C5C"
)
quality_data = quality_data.sort_values("Score", ascending=True)

dq1, dq2 = st.columns([2, 1])
with dq1:
    fig_q = go.Figure()
    fig_q.add_trace(go.Bar(
        x=quality_data["Score"],
        y=quality_data["Boutique"],
        orientation="h",
        marker_color=quality_data["Color"].tolist(),
        text=[f"{s}/100 — {st}" for s, st in zip(quality_data["Score"], quality_data["Status"])],
        textposition="outside",
        textfont=dict(size=11, color="#FFFFFF")
    ))
    fig_q.add_vline(x=80, line_dash="dash", line_color="#5CA88E",
                    annotation_text="Compliant (80+)",
                    annotation_font_color="#5CA88E",
                    annotation_font_size=10,
                    annotation_position="top right")
    fig_q.add_vline(x=65, line_dash="dash", line_color="#B8962E",
                    annotation_text="Review Required (65+)",
                    annotation_font_color="#B8962E",
                    annotation_font_size=10,
                    annotation_position="bottom right")
    fig_q.update_layout(
        paper_bgcolor=VC_NAVY, plot_bgcolor=VC_NAVY,
        font=dict(family="Raleway", color="#FFFFFF", size=11),
        title=dict(text="Data Capture Score by Boutique",
                   font=dict(family="EB Garamond", size=17, color="#FFFFFF")),
        xaxis=dict(range=[0, 115], gridcolor="rgba(255,255,255,0.05)",
                   color="#FFFFFF", title="Score out of 100"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.05)", color="#FFFFFF", title=""),
        margin=dict(t=60, b=20, r=20),
        showlegend=False
    )
    st.plotly_chart(fig_q, use_container_width=True)

with dq2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    for _, row in quality_data.sort_values("Score", ascending=False).iterrows():
        color = row["Color"]
        st.markdown(f"""
        <div style='background:linear-gradient(135deg,#112236,#0D1B2A);border:1px solid rgba(184,150,46,0.15);
                    border-left:3px solid {color};padding:14px 16px;margin-bottom:8px;'>
            <div style='font-size:10px;letter-spacing:0.15em;text-transform:uppercase;color:{color};margin-bottom:4px;'>{row['Boutique']}</div>
            <div style='font-family:EB Garamond,serif;font-size:28px;color:#FFFFFF;line-height:1;'>{row['Score']}<span style='font-size:13px;color:rgba(255,255,255,0.3);'>/100</span></div>
            <div style='font-size:10px;color:{color};letter-spacing:0.1em;margin-top:4px;'>{row['Status']}</div>
            <div style='font-size:10px;color:#6A7A8A;margin-top:4px;'>{row['Clients']:,} clients</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown(f"""
<div class='narrative-block'>
    <span class='insight-tag tag-alert'>Data Governance</span><br>
    A score of <strong>80 or above</strong> means client records are complete and compliant — the boutique is capturing names, contact details, purchase preferences and consent correctly.
    Scores between <strong>65 and 79</strong> indicate gaps that need review — likely missing fields or inconsistent data entry.
    Scores <strong>below 65</strong> require immediate training and a compliance audit. Incomplete data directly reduces campaign personalisation and clienteling effectiveness.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)

# ── SEGMENTATION ───────────────────────────────────────────
st.markdown("<div class='section-title'>Client Segmentation</div><div class='section-sub'>RFM scoring — recency, frequency, monetary value</div>", unsafe_allow_html=True)

ca, cb, cc = st.columns(3)
with ca:
    seg_c = rfm_f["Segment"].value_counts().reset_index()
    seg_c.columns = ["Segment", "Count"]
    fig1 = px.pie(seg_c, names="Segment", values="Count", title="Client Base by Segment",
                  color="Segment", color_discrete_map=SEGMENT_COLORS, hole=0.5)
    fig1.update_layout(
        paper_bgcolor=VC_NAVY, plot_bgcolor=VC_NAVY,
        font=dict(family="Raleway", color="#FFFFFF", size=11),
        title=dict(font=dict(family="EB Garamond", size=17, color="#FFFFFF")),
        legend=dict(**LEGEND_STYLE),
        margin=dict(t=50, b=20)
    )
    st.plotly_chart(fig1, use_container_width=True)

with cb:
    seg_v = rfm_f.groupby("Segment")["Monetary"].sum().reset_index().sort_values("Monetary")
    fig2 = px.bar(seg_v, x="Monetary", y="Segment", orientation="h",
                  title="Revenue Contribution by Segment",
                  color="Segment", color_discrete_map=SEGMENT_COLORS)
    fig2.update_layout(
        paper_bgcolor=VC_NAVY, plot_bgcolor=VC_NAVY,
        font=dict(family="Raleway", color="#FFFFFF", size=11),
        title=dict(font=dict(family="EB Garamond", size=17, color="#FFFFFF")),
        showlegend=False,
        xaxis=dict(title="Total Revenue (£)", gridcolor="rgba(255,255,255,0.05)", color="#FFFFFF"),
        yaxis=dict(title="", color="#FFFFFF"),
        margin=dict(t=50, b=20)
    )
    st.plotly_chart(fig2, use_container_width=True)

with cc:
    acq = rfm_f["ClientType"].value_counts().reset_index()
    acq.columns = ["Type", "Count"]
    fig3 = px.pie(acq, names="Type", values="Count", title="Acquisition vs Retention Split",
                  color="Type",
                  color_discrete_map={"Acquisition": "#B8962E", "Retention": "#5CA88E"},
                  hole=0.5)
    fig3.update_layout(
        paper_bgcolor=VC_NAVY, plot_bgcolor=VC_NAVY,
        font=dict(family="Raleway", color="#FFFFFF", size=11),
        title=dict(font=dict(family="EB Garamond", size=17, color="#FFFFFF")),
        legend=dict(**LEGEND_STYLE),
        margin=dict(t=50, b=20)
    )
    st.plotly_chart(fig3, use_container_width=True)

st.markdown(f"""
<div class='narrative-block'>
    <span class='insight-tag tag-alert'>At Risk Alert</span><br>
    <strong>{at_risk_count:,} clients ({at_risk_pct}%)</strong> are showing signs of disengagement — their last purchase was significantly longer ago than their segment peers.
    First-time buyers represent <strong>{acquisition_pct}%</strong> of the base. A structured second-visit activation programme is the single highest-impact retention lever available.
</div>
""", unsafe_allow_html=True)

# ── CLIENT PROFILES ────────────────────────────────────────
st.markdown("<div class='section-title'>Client Profiles</div><div class='section-sub'>Full client database — sorted by lifetime value — use filters in the sidebar to explore</div>", unsafe_allow_html=True)
display_rfm = rfm_f[["Customer ID","Recency","Frequency","Monetary","Segment","LoyaltyTier","Boutique","ClientType","DataScore"]]\
    .sort_values("Monetary", ascending=False)\
    .rename(columns={
        "Recency":     "Days Since Purchase",
        "Frequency":   "Orders",
        "Monetary":    "Lifetime Value (£)",
        "LoyaltyTier": "Tier",
        "ClientType":  "Type",
        "DataScore":   "Data Score"
    })
st.dataframe(display_rfm, use_container_width=True, height=300)

st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)

# ── WAITLIST ───────────────────────────────────────────────
st.markdown("<div class='section-title'>Waitlist Management</div><div class='section-sub'>Number of clients waiting per high-demand reference by boutique — updated daily</div>", unsafe_allow_html=True)

np.random.seed(99)
top_refs     = products["Description"].head(10).tolist()
wl_boutiques = sorted(rfm["Boutique"].unique())
wl_cols      = st.columns(len(wl_boutiques))

for col, boutique in zip(wl_cols, wl_boutiques):
    col.markdown(f"""
    <div style='font-size:9px;letter-spacing:0.2em;text-transform:uppercase;
                color:#B8962E;margin-bottom:12px;border-bottom:1px solid rgba(184,150,46,0.2);
                padding-bottom:8px;'>{boutique}</div>
    """, unsafe_allow_html=True)

    selected_refs = np.random.choice(top_refs, size=4, replace=False)
    for ref in selected_refs:
        count     = np.random.randint(2, 18)
        clean_ref = ref[:35] + ("…" if len(ref) > 35 else "")
        col.markdown(f"""
        <div class='waitlist-row'>
            <div class='waitlist-product'>{clean_ref}</div>
            <div>
                <div class='waitlist-count'>{count}</div>
                <div class='waitlist-label'>waiting</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div class='narrative-block'>
    <span class='insight-tag tag-blue'>Waitlist Intelligence</span><br>
    Each number represents the count of clients actively waiting for that reference at the boutique.
    When stock arrives, the SA contacts waiting clients in order of <strong>loyalty tier first, then recency of request</strong>.
    High waitlist counts signal demand that can inform <strong>allocation decisions and collection launch sequencing</strong>.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)

# ── REVENUE TREND ──────────────────────────────────────────
st.markdown("<div class='section-title'>Revenue Trend</div><div class='section-sub'>Monthly performance across the full period</div>", unsafe_allow_html=True)
fig4 = px.line(monthly, x="Month", y="TotalSpend", markers=True,
               color_discrete_sequence=[VC_GOLD])
fig4.update_traces(line=dict(width=2), marker=dict(size=5, color="#FFFFFF"))
fig4.update_layout(
    paper_bgcolor=VC_NAVY, plot_bgcolor=VC_NAVY,
    font=dict(family="Raleway", color="#FFFFFF", size=11),
    xaxis=dict(tickangle=-45, gridcolor="rgba(255,255,255,0.05)", title="", color="#FFFFFF"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.05)", title="Revenue (£)", color="#FFFFFF"),
    margin=dict(t=30, b=60)
)
st.plotly_chart(fig4, use_container_width=True)

st.markdown(f"""
<div class='narrative-block'>
    <span class='insight-tag tag-gold'>Trend Insight</span><br>
    Revenue peaked in <strong>{peak_month}</strong> at <strong>£{peak_val:,.0f}</strong>.
    Seasonal spikes align with gifting occasions and new collection launches.
    Aligning the CRM campaign calendar <strong>4 to 6 weeks ahead of these peaks</strong> maximises boutique client activation during the highest-intent purchase windows.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)

# ── RECOMMENDATIONS ────────────────────────────────────────
st.markdown("<div class='section-title'>Strategic Recommendations</div><div class='section-sub'>Three priority actions for the Americas CRM team</div>", unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)
with r1:
    st.markdown(f"""
    <div class='rec-card'>
        <div class='rec-number'>01</div>
        <div class='insight-tag tag-gold'>Client Development</div>
        <div class='rec-card-title'>Protect Connoisseur Tier</div>
        <ul>
            <li>Assign dedicated CRM ambassador per boutique</li>
            <li>Private collection previews before public launch</li>
            <li>Champions drive {champion_rev_pct}% of revenue — zero attrition tolerance</li>
            <li>Quarterly performance reviews with boutique managers</li>
            <li>Bespoke hospitality programme for top 50 clients globally</li>
        </ul>
    </div>""", unsafe_allow_html=True)

with r2:
    st.markdown(f"""
    <div class='rec-card'>
        <div class='rec-number'>02</div>
        <div class='insight-tag tag-alert'>CRM Activation</div>
        <div class='rec-card-title'>Elevate Campaign ROI</div>
        <ul>
            <li>Current conversion rate {conv_rate}% — target 15% by Q3</li>
            <li>Segment campaign lists by RFM score and loyalty tier</li>
            <li>A/B test event vs email format per boutique</li>
            <li>Deploy post-campaign analysis report within 48 hours</li>
            <li>Build automated re-engagement for non-openers</li>
        </ul>
    </div>""", unsafe_allow_html=True)

with r3:
    st.markdown(f"""
    <div class='rec-card'>
        <div class='rec-number'>03</div>
        <div class='insight-tag tag-blue'>Data Excellence</div>
        <div class='rec-card-title'>Raise Data Standards</div>
        <ul>
            <li>Target 100% of boutiques above data score 80 by Q2</li>
            <li>Monthly data capture training per boutique team</li>
            <li>CRM KPI scorecard introduced for boutique managers</li>
            <li>Weekly data quality report to commercial leadership</li>
            <li>Partner with HQ Data Solutions on compliance audit</li>
        </ul>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:10px;color:rgba(184,150,46,0.4);letter-spacing:0.2em;padding:24px 0;border-top:1px solid rgba(184,150,46,0.15);text-transform:uppercase;'>Vacheron Constantin &nbsp;✦&nbsp; CRM & Client Intelligence &nbsp;✦&nbsp; Python · Streamlit · Plotly</p>", unsafe_allow_html=True)