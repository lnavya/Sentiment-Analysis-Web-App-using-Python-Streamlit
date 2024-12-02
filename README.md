

# **Sentiment Analysis Web Application**

A web-based tool for performing sentiment analysis on text data using **Python**, **Streamlit**, and **TextBlob**. This application allows users to upload a CSV file with text data and outputs an enhanced CSV file with sentiment scores (positive, negative, neutral) and labels.



## **Features**

- **Upload CSV**: Input text data in a CSV format with a column containing text.
- **Sentiment Analysis**: Analyze polarity (positive/negative/neutral) and subjectivity using the TextBlob library.
- **Download Enhanced CSV**: Export results with sentiment scores and sentiment labels in a downloadable format.
- **Interactive Visualization**: View sentiment distribution through dynamic visualizations.



## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/lnavya/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```



## **Usage**

1. Upload a CSV file containing a column named `text` (case-insensitive).
2. View results:
   - Sentiment categories for each text entry.
   - Sentiment distribution visualized as a bar chart.
3. Download the enhanced CSV with sentiment scores and categories.



## **Tech Stack**

- **Streamlit**: User-friendly and interactive web UI framework.
- **TextBlob**: Sentiment analysis and natural language processing (NLP).
- **Pandas**: Efficient handling of CSV data.



## **How It Works**

1. **TextBlob Sentiment Analysis**:
   - **Polarity**: Measures the positivity or negativity of the text.
   - **Subjectivity**: Indicates the degree of opinion or factual content.

2. **Output CSV**:
   - Appends sentiment polarity and category labels to the original text data.

3. **Visualizations**:
   - Bar chart depicting sentiment distribution (Positive, Negative, Neutral).


