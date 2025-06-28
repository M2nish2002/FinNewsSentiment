import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(page_title="FinNews Sentiment Dashboard", layout="wide")

API_BASE = "http://localhost:8000"

st.markdown("""
    <style>
        .main {background-color: #f8f9fa;}
        .title {font-size: 42px; font-weight: bold; color: #003049;}
        .subtitle {font-size: 24px; color: #333; margin-bottom: 10px;}
        .box {background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);}
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📊 Real-Time FinNews Sentiment Dashboard</div>", unsafe_allow_html=True)

# Trigger News Pipeline
with st.sidebar:
    st.subheader("Manual Controls")
    if st.button("🔁 Run News Scraper"):
        with st.spinner("Running /analyze-news pipeline..."):
            r = requests.get(f"{API_BASE}/analyze-news")
            st.success("News scraped and analyzed successfully!")

# Sentiment Analysis Tool
st.markdown("<div class='subtitle'>🧠 Try Custom Sentiment Analysis</div>", unsafe_allow_html=True)
with st.form("sentiment_form"):
    user_input = st.text_area("Paste any news headline or paragraph", height=100)
    submitted = st.form_submit_button("Analyze")

    if submitted and user_input:
        res = requests.post(f"{API_BASE}/api/sentiment", json={"text": user_input})
        sentiment = res.json()["sentiment"]
        st.success(f"Prediction: **{sentiment['label']}** with confidence {sentiment['confidence']:.2f}")

# Fetch all news
st.markdown("<div class='subtitle'>📰 Latest Fetched Financial News</div>", unsafe_allow_html=True)
news = requests.get(f"{API_BASE}/api/news").json()

if news:
    df = pd.DataFrame(news)
    df['published'] = pd.to_datetime(df['published'])
    df['published_str'] = df['published'].dt.strftime('%Y-%m-%d %H:%M')
    df['sentiment'] = df['sentiment'].apply(lambda x: x['label'] if isinstance(x, dict) else x)

    # Display Table
    st.dataframe(df[['published_str', 'title', 'source', 'sentiment']], use_container_width=True)

    # Trend Chart
    sentiment_counts = df.groupby([df['published'].dt.date, 'sentiment']).size().reset_index(name='count')
    fig = px.area(sentiment_counts, x='published', y='count', color='sentiment',
                  title="📈 Sentiment Trend Over Time",
                  labels={'published': 'Date', 'count': 'Articles'})
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("No news articles found. Please run the scraper using the sidebar button.")
