# Para generar los embeddings de los chunks de un documento

from sentence_transformers import SentenceTransformer

# Elegir el modelo de embedding
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def load_model():
    return SentenceTransformer(EMBED_MODEL_NAME)

def generate_embeddings(model, texts):
    embeddings = model.encode(texts)

    return embeddings