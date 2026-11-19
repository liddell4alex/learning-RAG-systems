from src.embeddings import load_model
from src.vector_store import get_collection
from src.retrieval import retrieve
from src.generation import generate_answer

# Carga el modelo de embedding y la colección(base de datos vectorial)
model = load_model()
collection = get_collection()

print(f"Chunks disponibles: {collection.count()}")

while True:
    question = input("\nPreguntame ('q' para salir): ")

    if question.lower() == 'q':
        print("\nBye :D")
        break

    ress = retrieve(collection, model, question, n_result=10, max_distance=0.50)
    
    # Entra si no se encontró ningún resultado 
    if not ress["documents"][0]:
        print("No se encontró información suficientemente relevante.")
        continue

    # Construir el contexto para el LLM
    context_parts = []

    # Mostrar los resultados
    for i, doc in enumerate(ress["documents"][0]):
        metadata = ress["metadatas"][0][i]

        context_parts.append(
            f"Fuente: {metadata["source"]}, "
            f"Página: {metadata["page"]}\n"
            f"{doc}"
        )

    context = "\n\n".join(context_parts)

    # Generar respuesta
    answer = generate_answer(context, question)

    print("\nRespuesta:")
    print(answer)

    # Mostrar fuentes
    print()
    for i, metadata in enumerate(ress["metadatas"][0]):
        distance = ress["distances"][0][i]

        print(f"- {metadata["source"]} (página {metadata["page"]}) | Distancia: {distance:.4f}")

