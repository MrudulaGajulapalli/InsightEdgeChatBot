# from utils import load_documents, compute_embeddings, cosine_similarity, build_vocab, embed_text
# # from ingestion import word_index
# # # Similarity threshold: Only accept answers above this value
# # SIMILARITY_THRESHOLD = 0.5

# # # def get_best_answer(question):
# # #     # Load all documents
# # #     documents = load_documents()
# # #     contents = [doc['content'] for doc in documents]

# # #     # Build vocabulary from all document contents
# # #     word_index = build_vocab(contents)

# # #     # Compute embeddings
# # #     doc_embeddings = compute_embeddings(contents, word_index)
# # #     query_embedding = embed_text(question, word_index)

# # #     # Compute similarity between the query and all documents
# # #     similarities = [cosine_similarity(query_embedding, doc_emb) for doc_emb in doc_embeddings]

# # #     # Handle case where no similarities found or all are 0
# # #     if not similarities or max(similarities) == 0:
# # #         return "Sorry, I couldn't find an answer to your question.", "N/A"

# # #     # Get best matching document
# # #     best_index = similarities.index(max(similarities))
# # #     best_score = similarities[best_index]
# # #     best_doc = documents[best_index]

# # #     # Debug info (optional)
# # #     print(f"Best match score: {best_score}")
# # #     print(f"Matched document: {best_doc['source']}")

# # #     # Use threshold to avoid wrong matches
# # #     if best_score >= SIMILARITY_THRESHOLD:
# # #         return best_answer, best_source
# # #     else:
# # #         return "Sorry, I couldn't find an answer to your question.", "N/A"


# def get_best_answer(query):
#     documents = load_documents()
#     doc_embeddings = compute_embeddings([doc['content'] for doc in documents])
#     query_embedding = compute_embeddings([query])[0]

#     similarities = [cosine_similarity(query_embedding, doc_emb) for doc_emb in doc_embeddings]

#     best_index = np.argmax(similarities)
#     best_score = similarities[best_index]

#     # ⚠️ Only return an answer if similarity is above a threshold
#     if best_score > 0.75:
#         best_doc = documents[best_index]
#         return best_doc['content'], best_doc['source']
#     else:
#         return "Sorry, I couldn't find an answer to your question.", "N/A"

# # **************
# # import json
# # import os
# # from sklearn.feature_extraction.text import TfidfVectorizer
# # from sklearn.metrics.pairwise import cosine_similarity

# # # Load knowledge base from local JSON file
# # with open("database.json", "r") as f:
# #     knowledge_base = json.load(f)

# # # Prepare documents and answers
# # documents = [item["question"] for item in knowledge_base]
# # answers = [item["answer"] for item in knowledge_base]
# # sources = [item["source"] for item in knowledge_base]

# # # Vectorize questions using TF-IDF
# # vectorizer = TfidfVectorizer()
# # doc_vectors = vectorizer.fit_transform(documents)

# # def get_answer(user_question):
# #     # Convert user's question to vector
# #     question_vector = vectorizer.transform([user_question])

# #     # Compute cosine similarity
# #     similarities = cosine_similarity(question_vector, doc_vectors).flatten()

# #     # Find the best match
# #     max_index = similarities.argmax()
# #     max_score = similarities[max_index]

# #     if max_score < 0.2:
# #         return "I'm not confident about the answer. Could you rephrase the question?", "N/A"

# #     return answers[max_index], sources[max_index]

# **************
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


