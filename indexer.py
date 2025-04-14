from utils import compute_embeddings
import json

def index_documents(docs, output_path='database.json'):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(docs, f, indent=2)
