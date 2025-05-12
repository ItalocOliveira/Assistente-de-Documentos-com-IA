# 🤖 Assistente de Documentos com IA

Este é um projeto prático que utiliza **RAG (Retrieval-Augmented Generation)** com a **API da OpenAI** para responder perguntas com base no conteúdo de arquivos PDF enviados pelo usuário. Ideal para extrair rapidamente informações de documentos extensos!

## 🧠 Funcionalidades

- Upload de arquivos PDF
- Divisão e vetorização do conteúdo
- Busca semântica com FAISS
- Respostas inteligentes utilizando o modelo GPT-3.5 da OpenAI

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [PyMuPDF](https://pymupdf.readthedocs.io/)

## 📦 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/assistente-pdf-ia.git
cd assistente-pdf-ia
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Crie um arquivo .env com sua chave da OpenAI:

```bash
OPENAI_API_KEY=sua-chave-aqui
```

▶️ Como Usar

```bash
streamlit run app.py
```
## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
