# 🚀 RAG Demo AI  
### Retrieval-Augmented Generation using Hugging Face + LangChain  

---

## 📌 Overview  

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that enhances Large Language Models (LLMs) by integrating **real-time document retrieval** with **AI-generated responses**.  

Instead of relying solely on pre-trained knowledge, the system:  
- Retrieves relevant information from external documents  
- Uses that context to generate **accurate, grounded responses**  

---

## 🧠 What is RAG?  

RAG (Retrieval-Augmented Generation) combines:  
- 🔍 **Information Retrieval** — Fetch relevant data  
- ✨ **Text Generation** — Generate contextual responses  

This approach reduces hallucinations and improves factual accuracy.  

---

## ⚙️ Tech Stack  

### 🔹 Frontend  
- **Streamlit** — Interactive user interface  

### 🔹 Backend & AI Framework  
- **LangChain** — LLM orchestration  
- **LangChain Core** — Chains, prompts, document handling  
- **LangChain Community** — Extended integrations  

### 🔹 Embeddings  
- **Sentence-Transformers** — Converts text into vector embeddings  
- **LangChain-HuggingFace** — Hugging Face integration  

### 🔹 Vector Database  
- **FAISS (faiss-cpu)** — Fast similarity search  

### 🔹 Utilities  
- **Python-dotenv** — Secure environment variable management  
- **LangChain Text Splitters** — Chunking large documents  

---

## 🔄 System Architecture  
User Query
↓
Embedding (Hugging Face)
↓
FAISS Vector Search
↓
Retrieve Relevant Chunks
↓
Pass Context to LLM
↓
Generated Response


---

## 🛠️ How It Works  

1. 📄 Load documents (PDF/text)  
2. ✂️ Split into smaller chunks  
3. 🔢 Convert chunks into embeddings  
4. 🗄️ Store embeddings in FAISS  
5. ❓ User submits a query  
6. 🔍 Retrieve similar chunks  
7. 🤖 Generate response using LLM + context  

---

## ✨ Features  

- Context-aware AI responses  
- Reduced hallucination using retrieval  
- Fast vector similarity search with FAISS  
- Modular and scalable architecture  
- Simple UI using Streamlit  

---

## 📦 Installation  

bash
# Clone the repository
git clone https://github.com/manal-munawwar/rag-demo-ai.git

# Navigate to project
cd rag-demo-ai

# Create virtual environment
python -m venv myenv
source myenv/bin/activate  # Mac/Linux
myenv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

## 💼 Author
Manal Munawwar
Fresh Graduate
AI Projects | Marketing Enthusiast
