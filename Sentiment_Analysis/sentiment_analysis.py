from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st


st.header('Sentiment Analysis')


text = st.text_input('Text here: ')
    
sid = SentimentIntensityAnalyzer()
Sentiment_score=sid.polarity_scores(text)
st.write(Sentiment_score)
