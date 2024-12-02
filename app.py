import streamlit as st
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Sentiment Analysis Web App")
st.markdown("Analyze the sentiment of text and CSV data with this simple app!")

# Input Method Selection
st.sidebar.header("Input Options")
input_type = st.sidebar.selectbox("Choose input type:", ["Text Input", "Upload CSV"])

# Sentiment Analysis Function
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Text Input Analysis
if input_type == "Text Input":
    st.subheader("Analyze Single Text")
    user_input = st.text_area("Enter text to analyze:")
    if st.button("Analyze"):
        if user_input:
            sentiment = analyze_sentiment(user_input)
            st.write(f"**Sentiment:** {sentiment}")
        else:
            st.warning("Please enter some text!")

# CSV Upload Analysis
elif input_type == "Upload CSV":
    st.subheader("Batch Analysis via CSV Upload")
    uploaded_file = st.file_uploader("Upload your CSV file (must contain a 'text' column):", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if "text" in df.columns:
            df["Sentiment"] = df["text"].apply(analyze_sentiment)
            st.write("Analysis Complete:")
            st.write(df)

            # Visualization
            st.subheader("Sentiment Distribution")
            sentiment_counts = df["Sentiment"].value_counts()
            fig, ax = plt.subplots()
            sentiment_counts.plot(kind="bar", ax=ax, color=["green", "red", "blue"])
            st.pyplot(fig)

            # Download Results
            st.download_button(
                label="Download CSV with Sentiments",
                data=df.to_csv(index=False),
                file_name="sentiment_results.csv",
                mime="text/csv",
            )
        else:
            st.error("CSV must contain a 'text' column!")

# Footer
st.markdown("Developed with ❤️ using Python and Streamlit")
