import os
import streamlit as st
import fitz  # PyMuPDF
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyMuPDFLoader

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da página
st.set_page_config(page_title="📄 Assistente de Documentos com IA", layout="wide")
st.title("🤖 Assistente de Documentos com IA")

st.markdown("Envie um **documento em PDF** e faça perguntas sobre o conteúdo!")

# === 1. Upload do PDF ===
pdf_file = st.file_uploader("📄 Envie o documento (PDF)", type=["pdf"])

if pdf_file:
    # Salvar o arquivo PDF
    os.makedirs("docs", exist_ok=True)
    pdf_path = f"docs/{pdf_file.name}"
    with open(pdf_path, "wb") as f:
        f.write(pdf_file.read())

    # === 2. Extração e fragmentação do texto ===
    loader = PyMuPDFLoader(pdf_path)
    docs = loader.load()

    splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_documents(docs)

    # === 3. Embeddings e banco vetorial ===
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(texts, embeddings)

    # === 4. Criação do modelo RAG ===
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)

    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    st.success("✅ Documento processado com sucesso!")

    # === 5. Perguntas do usuário ===
    user_question = st.text_input("❓ Faça uma pergunta sobre o documento:")

    if user_question:
        with st.spinner("🔎 Analisando com IA..."):
            resposta = rag_chain.run(user_question)
        st.markdown("### 🧠 Resposta da IA:")
        st.markdown(resposta)
