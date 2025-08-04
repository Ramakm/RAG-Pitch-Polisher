import streamlit as st
from qa_engine import get_answer

st.set_page_config(page_title="Startup Pitch Polisher", layout="centered")

st.title("🚀 Startup Pitch Polisher")
st.markdown("Refine your pitch using VC insights and market data. Ask anything!")

query = st.text_input("Enter your startup idea or pitch-related question:")

if st.button("Polish My Pitch") and query:
    with st.spinner("Refining..."):
        answer = get_answer(query)
        st.success("Here’s how to polish your pitch:")
        st.write(answer)
