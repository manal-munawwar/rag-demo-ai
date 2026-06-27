# RAG Demo AI 🤖

A Retrieval-Augmented Generation (RAG) demo: upload a PDF, ask questions about it, and get answers grounded in the document's actual content — powered by Hugging Face sentence embeddings, FAISS similarity search, and Google's Gemini model.

## How It Works

1. **Upload** — You upload a PDF through the Streamlit file uploader.
2. **Extract** — `PyPDF2` reads the PDF and concatenates the text of every page.
3. **Chunk** — LangChain's `CharacterTextSplitter` splits the raw text into chunks of **1,000 characters with 200-character overlap**, preserving context across chunk boundaries.
4. **Embed** — Each chunk is embedded using the Hugging Face sentence-transformers model **`all-MiniLM-L6-v2`** (via `langchain-huggingface` / `HuggingFaceEmbeddings`).
5. **Index** — The embeddings are stored in an in-memory **FAISS** vector store for fast similarity search.
6. **Ask** — When you type a question, the FAISS retriever finds the most relevant chunks.
7. **Generate** — The retrieved chunks are joined and passed, along with your question, into a prompt sent to **Gemini 2.5 Flash Lite**. The model is explicitly instructed to say it has no relevant content if it can't answer from the provided context, and to respond in bullet points.

## Tech Stack

| Component | Library |
|---|---|
| UI | Streamlit |
| PDF parsing | PyPDF2 |
| Chunking | `langchain-text-splitters` (`CharacterTextSplitter`) |
| Embeddings | `langchain-huggingface` + `sentence-transformers` (`all-MiniLM-L6-v2`) |
| Vector store | FAISS (`faiss-cpu`, via `langchain-community`) |
| Generation | `google-generativeai` (Gemini 2.5 Flash Lite) |
| Config | python-dotenv |

## Project Structure

```
rag-demo-ai/
├── rag_app.py          # Full RAG pipeline: upload → chunk → embed → retrieve → generate
├── requirements.txt    # streamlit, PyPDF2, langchain (+ community/core/huggingface/text-splitters),
│                        # faiss-cpu, sentence-transformers, google-generativeai, python-dotenv
├── LICENSE             # MIT
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.9+
- A [Google AI Studio](https://aistudio.google.com/) API key
- Note: the first run downloads the `all-MiniLM-L6-v2` embedding model from Hugging Face, so an internet connection is required on first launch.

### Installation

```bash
git clone https://github.com/manal-munawwar/rag-demo-ai.git
cd rag-demo-ai
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Run

```bash
streamlit run rag_app.py
```

### Usage

1. Wait for the embedding model to load (shown via a spinner on startup).
2. Upload a PDF document.
3. Once you see "Document processed and saved successfully," type your question in the input box.
4. Read the AI-generated answer, grounded in the retrieved chunks from your document.

## Notes & Limitations

- The FAISS index is **in-memory only** — it's rebuilt every time you upload a file and isn't persisted to disk, so it's lost when the app restarts.
- No chat history — each query is treated independently; there's no conversational memory across questions.
- Retrieval currently uses the default FAISS retriever settings (no configurable `k`, no re-ranking, no hybrid search).
- Large PDFs will take longer to chunk/embed since everything runs synchronously on each upload.
- If extracted PDF text is empty (e.g., scanned/image-only PDF), the app simply warns you to drop a valid PDF — there's no OCR fallback.

## Possible Improvements

- Persist the FAISS index to disk (or a proper vector DB) to avoid re-embedding on every session
- Add multi-turn conversational memory
- Show the retrieved source chunks alongside the answer for transparency
- Support multiple file uploads / a document library
- Add OCR support for scanned PDFs

## License

MIT — see [LICENSE](LICENSE).

## Author

**Manal Munawwar**
- GitHub: [@manal-munawwar](https://github.com/manal-munawwar)
