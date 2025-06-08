# Amazon-Review-Scrapping
📦 Amazon Product Review Scraper & Sentiment Analysis

📝 Project Overview
This project is a Python-based Streamlit application that allows users to scrape product reviews from any Amazon product page and perform sentiment analysis on those reviews using a custom-trained machine learning model (model.p). The model classifies each review as positive or negative, providing valuable insights into customer opinions.

🎯 Objectives

✔️ Automate the collection of real user reviews from Amazon product pages.

✔️ Preprocess and clean review data for analysis.

✔️ Use a machine learning model to analyze sentiment (positive/negative).

✔️ Display results interactively using Streamlit.

🛠️ Technologies Used:

Component                Technology

Interface	               Streamlit
Web Scraping	           BeautifulSoup + requests
ML Model	               scikit-learn
Model Serialization	     pickle
Programming Language	   Python 3.x

📁 Project Structure

amazon_sentiment_analysis/
│
├── app.py              
├── scraper.py          
├── sentiment.py        
├── model.p             
├── requirements.txt    
└── README.md        

💻 Installation Instructions

1. Clone the Repository

git clone https://github.com/yourusername/amazon-sentiment-analysis.git
cd amazon-sentiment-analysis

2. Install Requirements

pip install -r requirements.txt

3. Run the Streamlit App

streamlit run app.py



