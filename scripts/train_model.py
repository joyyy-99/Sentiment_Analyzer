
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import movie_reviews
from preprocess import clean_tweet

# Download the movie reviews dataset
nltk.download('movie_reviews')

# Load the dataset
reviews = [(movie_reviews.raw(fileid), category) 
           for category in movie_reviews.categories() 
           for fileid in movie_reviews.fileids(category)]
df = pd.DataFrame(reviews, columns=['text', 'sentiment'])

# Clean the text
df['cleaned_text'] = df['text'].apply(clean_tweet)

# Convert text to numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['cleaned_text'])
y = df['sentiment'].apply(lambda x: 1 if x == 'pos' else 0)  # 1 for positive, 0 for negative

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")


import joblib
joblib.dump(model, "data/sentiment_model.pkl")
joblib.dump(vectorizer, "data/vectorizer.pkl")