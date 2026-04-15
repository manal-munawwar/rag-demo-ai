# rag-demo-ai
### RAG algorithm using Hugging Face Embedding 

RAG is a technique that enhances the capabilities of LLMs by combining the informations retrival with the generation.
Instead of replying on pre-trained knowledge, RAG fetch the relevent data from external source and use it to generate more accurate response. 

### Packages 

streamlit 
python-dotenv
langchain # core framework 
langchain # core framework for building LLM applications
langchain-community # extra integrations and utilities for LangChain
faiss-cpu # fast vector database to store the embeddings
langchain-huggingface # connect huggingface models to perform embeddings 
langchain-text-splitters # to split the PDF text into smaller chunks for better processing
sentence-transformers # pre-trained models to convert chunks into vector embeddings
langchain-core # to handle documents, chains, of data etc ...

