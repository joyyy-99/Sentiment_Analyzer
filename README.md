# Sentiment Analysis of Tweets About Beyoncé's Album *Cowboy Carter*

## Project Overview

This project is a real-time sentiment analysis tool that fetches tweets related to Beyoncé's album *Cowboy Carter* and classifies them as positive or negative. It utilizes machine learning techniques, specifically a Naïve Bayes classifier trained on the NLTK movie reviews dataset, to determine sentiment polarity.

## Features

- Fetches live tweets using the Twitter API (Tweepy).
- Cleans and preprocesses tweet text by removing URLs, mentions, hashtags, and stopwords.
- Transforms text data into numerical features using `CountVectorizer`.
- Classifies tweets as either positive or negative using a trained Naïve Bayes model.
- Performs real-time sentiment analysis at specified intervals.

## Technologies Used

- Python
- Tweepy (for fetching tweets)
- NLTK (for text processing and training data)
- Scikit-learn (for machine learning)
- Joblib (for model persistence)

## Installation and Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/joyyy-99/Sentiment_Analyzer.git
   ```
2. Navigate to the project folder:
   ```sh
   cd Sentiment_Analyzer
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up your Twitter API bearer token in `fetch_tweets.py`.
5. Train the sentiment analysis model:
   ```sh
   python scripts/train_model.py
   ```
6. Start real-time sentiment analysis:
   ```sh
   python scripts/analyze.py
   ```

## How It Works

- `fetch_tweets.py`: Fetches recent tweets containing the keyword *Cowboy Carter*.
- `preprocess.py`: Cleans the fetched tweets by removing noise and unnecessary characters.
- `train_model.py`: Trains the Naïve Bayes model using the NLTK movie reviews dataset.
- `analyze.py`: Loads the trained model and performs real-time sentiment analysis on tweets about *Cowboy Carter*.

## Results

- The trained model achieved an **accuracy of 81.75%** on the test dataset.
- Users can monitor live sentiment trends on *Cowboy Carter* based on real-time Twitter data.

## Future Improvements

- Improve accuracy by fine-tuning the model with a more relevant dataset.
- Implement visualization tools for real-time sentiment tracking.
- Expand analysis to include neutral sentiments and emotion detection.

## Author

Developed by Joy Awino


