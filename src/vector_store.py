# Para la base de datos vectorial; crearla o abrirla y administrarla

import chromadb

# Crear o abrir colección (db)
def get_collection():
    # Para guardar la db en la carpeta database del proyecto
    client = chromadb.PersistentClient(path="database")

    # Para crear la db, utilizamos distancia del coseno para las busquedas
    collection = client.get_or_create_collection(
        name="rag_documents",
        metadata={"hnsw:space": "cosine"}
    )

    return collection

def store_chunks(collection, chunks, embeddings, source):
    ids = []        # Identificadores, distinguir registros
    documents = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        # ids con formato fuente(nombre de archivo)-p(num. pagina)-c(indice)
        ids.append(f"{source}-p{chunk['page']}-c{i}")
        # En documents: el texto del chunk
        documents.append(chunk["text"])
        # En metadata: fuente(nombre de archivo) pagina(pagina del chunk)
        metadatas.append({
            "source": source,
            "page":chunk["page"]
        })

    # Inserta los regitors, si ya existe un id, lo actualiza no lo duplica
    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(), # tolist porque es un arreglo numpy no una lista
        metadatas=metadatas
    )
