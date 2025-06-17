import streamlit as st
from review_scraper import scrape_reviews
from sentiment_model import analyze_sentiment
import pandas as pd


st.set_page_config(page_title="Amazon Review Sentiment Analyzer", layout="wide")


st.title("🛍️ Amazon Product Review Sentiment Analysis")
st.markdown("Analyze customer sentiments using **VADER** and a **Trained ML Model**.")


product_url = st.text_input("🔗 Enter Amazon Product URL:")

if product_url:
    with st.spinner("🔍 Fetching product reviews..."):
        result = scrape_reviews(product_url)

    if "error" in result:
        st.error(f"❌ {result['error']}")
    else:
        reviews = result["reviews"]
        category = result["category"]

        st.success("✅ Reviews successfully extracted!")
        st.markdown(f"**Product Category:** `{category}`")

        if not reviews:
            st.warning("⚠️ No reviews found.")
        else:
            st.markdown("### 🔍 Sample Extracted Reviews")
            for idx, review in enumerate(reviews[:5], 1):
                st.markdown(f"**{idx}.** {review}")

          
            st.markdown("### 📊 Sentiment Analysis Results")
            sentiments = []
            for review in reviews:
                sentiment_result = analyze_sentiment(review)
                sentiments.append({
                    "Review": review,
                    "VADER Sentiment": sentiment_result["VADER Sentiment"],
                    "VADER Score": sentiment_result["VADER Score"],
                    "ML Sentiment": sentiment_result["ML Sentiment"]
                })

            
            sentiment_df = pd.DataFrame(sentiments)

          
            st.markdown("#### 🔵 VADER Sentiment Distribution")
            vader_counts = sentiment_df["VADER Sentiment"].value_counts()
            st.bar_chart(vader_counts)

            st.markdown("#### 🟢 ML Model Sentiment Distribution")
            ml_counts = sentiment_df["ML Sentiment"].value_counts()
            st.bar_chart(ml_counts)

           
            st.markdown("### 📋 Detailed Sentiment Table")
            st.dataframe(sentiment_df, use_container_width=True)

          
            csv = sentiment_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Download Sentiment Report as CSV",
                data=csv,
                file_name='sentiment_analysis.csv',
                mime='text/csv',
            )
