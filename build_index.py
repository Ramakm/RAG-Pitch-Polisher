from extract_pdf import extract_text_from_pdf
from embedded_chunks import chunk_text, embed_chunks, save_faiss_index

if __name__ == "__main__":
    print("📄 Extracting pitch text...")
    text = extract_text_from_pdf("temp.pdf")

    print("✂️ Chunking...")
    chunks = chunk_text(text)

    print(f"🧠 Embedding {len(chunks)} chunks...")
    embeddings = embed_chunks(chunks)

    print("💾 Saving FAISS index...")
    save_faiss_index(embeddings, chunks)

    print("✅ Index built and saved!")
