# Para recopilar todos los documentos de la carpeta docs

from pathlib import Path

from src.extract import extract_pdf
from src.chunking import chunk_pages
from src.embeddings import load_model, generate_embeddings
from src.vector_store import get_collection, store_chunks

# Obtener todos los PDF de docs/
docs = list(Path("docs").glob("*.pdf"))

# Cargo modelo y colección
model = load_model()
collection = get_collection()

# Procesar cada documento
for doc in docs:
    print(f"\nProcesando: {doc.name}")

    # Extraer texto para cada documento
    pages = extract_pdf(doc)

    # Crear chunks
    chunks = chunk_pages(pages)

    # Obtener textos de los chunks creados
    texts = [chunk["text"] for chunk in chunks]

    # Generar embeddings
    embeddings = generate_embeddings(model, texts)

    # Almacenar en ChromaDB
    store_chunks(collection, chunks, embeddings, doc.name)

    print(f"Chunks almacenados: {len(chunks)} para {doc.name}")

print(f"\nTotal de chunks en la colección: {collection.count()}")