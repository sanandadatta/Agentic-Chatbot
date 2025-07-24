import streamlit as st
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent

st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")

st.title("Agentic RAG Chatbot with MCP")

uploaded_files = st.file_uploader("Upload documents", type=["pdf", "docx", "pptx", "csv", "txt", "md"], accept_multiple_files=True)
user_query = st.text_input("Ask a question")

if uploaded_files:
    for file in uploaded_files:
        doc_chunks = ingestion_agent.handle(file)
        retrieval_agent.index_chunks(doc_chunks)
    st.success("Documents parsed and indexed!")

if user_query:
    retrieved = retrieval_agent.retrieve(user_query)
    answer = llm_agent.generate_response(user_query, retrieved)
    st.markdown(f"### Answer: {answer['answer']}")
    st.markdown("#### Source Chunks:")
    for chunk in answer['sources']:
        st.info(chunk)