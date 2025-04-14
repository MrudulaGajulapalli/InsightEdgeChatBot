from utils import compute_embeddings, cosine_similarity

def search(query, docs):
    query_embedding = compute_embeddings([query])[0]
    results = []

    for doc in docs:
        doc_embedding = compute_embeddings([doc['content']])[0]
        score = cosine_similarity(query_embedding, doc_embedding)
        results.append((score, doc))

    return sorted(results, key=lambda x: x[0], reverse=True)
