# Para las consultas a la base de datos vectorial

# 0 vector practicamente identico
# 1 vector sin similitud coseno (vectores ortogonales)
# 2 vectores en direcciones opuestas
def retrieve(collection, model, question, n_result=4, max_distance=0.5):
    # Convertir pregunta(query) en embedding
    query_embedding = model.encode([question])

    # Buscar chunks similares
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=n_result
    )

    # Para identificar resultados dentro de un umbral de significado
    valid_indices = [
        i for i, distance in enumerate(results["distances"][0]) if distance <= max_distance
    ]

    # Construir resultados filtrados
    filtered_results = {
        "documents": [
            [results["documents"][0][i] for i in valid_indices]
        ],
        "metadatas": [
            [results["metadatas"][0][i] for i in valid_indices]
        ],
        "distances": [
            [results["distances"][0][i] for i in valid_indices]
        ]
    }

    return filtered_results