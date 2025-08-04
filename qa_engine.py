from embedded_chunks import get_embedding_model, load_faiss_index, retrieve_similar_chunks

# Path to your FAISS index (update as per your project)
INDEX_PATH = "faiss_index"

# Initialize embedding model and FAISS index
embedding_model = get_embedding_model()
vector_index = load_faiss_index(INDEX_PATH, embedding_model)

# Generate a synthetic answer using retrieved content
def get_answer(query):
    chunks = retrieve_similar_chunks(vector_index, query)
    return "\n\n".join(chunks)
