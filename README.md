

# Sentiment Analysis Web Application

A web-based tool for performing sentiment analysis on text data using **Python**, **Streamlit**, and **TextBlob**. Upload a CSV file with text data, and the app will return an enhanced CSV with sentiment scores (positive, negative, neutral).

## Features
- **Upload CSV**: Input text data in a CSV format.
- **Sentiment Analysis**: Analyze polarity (positive/negative/neutral) and subjectivity using **TextBlob**.
- **Download Enhanced CSV**: Get results with sentiment scores and labels.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```
2. Install dependencies:
   ```bash
   pip install streamlit textblob pandas
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage

- Upload a CSV file with a `text` column.
- View sentiment analysis results.
- Download the enhanced CSV with sentiment scores and categories.

## Tech Stack
- **Streamlit** for UI
- **TextBlob** for NLP
- **Pandas** for CSV handling

