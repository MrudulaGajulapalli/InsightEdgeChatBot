import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load knowledge base from local JSON file
with open("database.json", "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)

# Prepare documents and answers
documents = [item["question"] for item in knowledge_base]
answers = [item["answer"] for item in knowledge_base]
sources = [item["source"] for item in knowledge_base]

# Vectorize questions using TF-IDF
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

def get_answer(user_question):
    # Convert user's question to vector
    question_vector = vectorizer.transform([user_question])

    # Compute cosine similarity
    similarities = cosine_similarity(question_vector, doc_vectors).flatten()

    # Find the best match
    max_index = similarities.argmax()
    max_score = similarities[max_index]

    if max_score < 0.2:
        return "I'm not confident about the answer. Could you rephrase the question?", "N/A"

    return answers[max_index], sources[max_index]


