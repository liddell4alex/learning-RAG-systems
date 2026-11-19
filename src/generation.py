# Para tomar la colección de la bdv siendo este el contexto y generar la
# respuesta del LLM qwen2.5:3b

import ollama

LLM_MODEL_NAME = 'qwen2.5:3b-instruct'

def generate_answer(context, question):
    system_prompt = """
    You are an assistant that answers questions using retrieved documents.

    Follow these rules strictly:
    1. Use only the information provided in the context.
    2. Do not use external knowledge or assumptions.
    3. If the context does not contain enough information, explicitly say so.
    4. Do not invent facts or complete missing information.
    5. Keep your answers clear and concise. 
    """
    user_prompt = f"""
    CONTEXT:
    {context}

    QUESTION:
    {question}
    """

    response = ollama.chat(
        model=LLM_MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        options={
            "temperature": 0    # Controla cuanto varía la selección de respuestas
        }                       # Alta: respuestas variables
    )                           # Baja: respuestas más deterministas

    return response["message"]["content"]