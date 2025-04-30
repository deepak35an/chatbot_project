# train_model.py

from training_data import training_data
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pickle

# Extract inputs (texts) and labels (intents)
texts = [item["text"] for item in training_data]
intents = [item["intent"] for item in training_data]

# Create a pipeline: Vectorizer + Naive Bayes Classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(texts, intents)

# Save the trained model to a file
with open("intent_model.pkl", "wb") as f:
    pickle.dump(model, f)

print(" Model trained and saved as 'intent_model.pkl'")
