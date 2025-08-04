from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter


# 1. Load the embedding model
def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 2. Chunk long text into smaller pieces
def chunk_text(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
    )
    return splitter.split_text(text)

# 3. Embed the chunks using the model
def embed_chunks(chunks: list[str]):
    model = get_embedding_model()
    return model

# 4. Save FAISS index to local path
def save_faiss_index(embeddings, chunks, index_dir="faiss_index"):
    vectorstore = FAISS.from_texts(chunks, embeddings)
    vectorstore.save_local(index_dir)

# 5. Load FAISS index
def load_faiss_index(index_path: str, embeddings):
    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

# 6. Retrieve similar chunks
def retrieve_similar_chunks(index, query, k=5):
    docs_and_scores = index.similarity_search_with_score(query, k=k)
    return [doc.page_content for doc, _ in docs_and_scores]

# Optional test
if __name__ == "__main__":
    sample = "Your startup pitch deck text goes here..." * 50
    chunks = chunk_text(sample)
    print(f"Total chunks: {len(chunks)}")
    print(chunks[0])
