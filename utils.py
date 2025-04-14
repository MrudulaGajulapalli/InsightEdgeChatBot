import os
import numpy as np

def load_documents(folder_path='data'):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt') or filename.endswith('.md'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                documents.append({
                    'content': content,
                    'source': filename
                })
    return documents

import os

def load_documents(folder='Knowledge_base'):
    documents = []
    for filename in os.listdir(folder):
        if filename.endswith('.txt') or filename.endswith('.md'):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                documents.append({'content': content, 'source': filename})
    return documents

def build_vocab(texts):
    vocab = set()
    for text in texts:
        vocab.update(text.lower().split())
    vocab = sorted(vocab)
    word_index = {word: idx for idx, word in enumerate(vocab)}
    return word_index

def compute_embeddings(texts, word_index):
    embeddings = []
    for text in texts:
        vector = np.zeros(len(word_index))
        for word in text.lower().split():
            if word in word_index:
                vector[word_index[word]] += 1
        embeddings.append(vector)
    return embeddings

def embed_text(text, word_index):
    vector = np.zeros(len(word_index))
    for word in text.lower().split():
        if word in word_index:
            vector[word_index[word]] += 1
    return vector

def cosine_similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)
