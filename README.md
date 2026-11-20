# Simple RAG system powered by books on machine learning

## Author

**Name**: Alejandro Cons Andablo <br>
**Affiliation**: Universidad Nacional Autónoma de México (UNAM) <br>
**Course**: Sistemas de Información y Servicios Web <br>
**Contact**: alexmixsep@gmail.com

## Requirements

Using
- Ollama qwen2.5:3b-instruct as LLM
- sentence-transformers/all-MiniLM-L6-v2 as embedding model
- ChromaDB as vector database

The embedding model and ChromaDB are installed from requirements.txt

I recommend installing Ollama using your system's package manager; otherwise, uninstalling it later can be tricky. Then to install the used model:

```
ollama pull qwen2.5:3b-instruct
```

## Preparing Environment for Linux

You need to clone the repo on your PC. With the repo cloned and in the root of the project:

```
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Once with the environment set up we need to download the documents (if you want to add your own documents skip this):

```
grep -oE 'https?://[^ ]+' download_docs.txt | wget -i -
```

After downloading the documents, we need to process their text, split it into chunks, generate embeddings, and store them in the vector database. This is done using:

```
python indexate.py
```

And that's all. The environment is prepared for running

## Running

```
python main.py
```

### Example

![RAG running example](demo.gif)