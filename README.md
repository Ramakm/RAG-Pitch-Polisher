# Startup Pitch Polisher

A powerful Streamlit-based AI assistant that helps startup founders refine and polish their pitch decks using insights from venture capital, market data, and retrieval-augmented generation (RAG).

---

## What It Does

**Startup Pitch Polisher** allows founders to:
- Upload or analyze pitch content
- Ask natural language questions about VC expectations
- Retrieve high-quality, context-aware answers based on indexed insights
- Polish startup ideas, mission, or GTM strategy with real-time feedback

Powered by:
- **LangChain (Community & Core)**
- **FAISS for semantic search**
- **HuggingFace Transformers**
- **Streamlit UI**

---

## Demo Screenshot

![Demo](assets/demo-screenshot.png)  
> Interface for refining your pitch using contextual retrieval.

---

## Features

✅ Retrieval-Augmented Generation (RAG)  
✅ FAISS-powered semantic search  
✅ HuggingFace embeddings  
✅ Clean and responsive Streamlit interface  
✅ Easily extensible for additional domains (health, fintech, etc.)

---

## Project Structure

```bash
pitch-polisher/
├── app.py                        # Main Streamlit app
├── embedded_chunks.py           # Embedding + FAISS functions
├── qa_engine.py                 # Question-answering logic
├── faiss_index/                 # Stored FAISS index
├── docs/ / pitch_data/          # Reference material to be indexed
├── requirements.txt             # Dependencies
├── README.md                    # You're reading it!
```

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/pitch-polisher.git
cd pitch-polisher
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt

# If you face errors related to embeddings, run:
pip install langchain-community huggingface-hub sentence-transformers
```
### 4. Build FAISS Index
Make sure you have a folder like pitch_data/ with .txt or .md files.

Then in embedded_chunks.py, run your index creation logic or create a script like:
```bash
from embedded_chunks import create_faiss_index

create_faiss_index("pitch_data", "faiss_index")
```
### 5. Run the app
```bash
streamlit run app.py
```

## Requirements

  - Python 3.9+
  - langchain-community
  - faiss-cpu
  - streamlit
  - sentence-transformers
  - huggingface-hub

(See requirements.txt for the full list)



MIT License © [Ramakrushna](https://x.com/techwith_ram) ❤️
