import streamlit as st
from PyPDF2 import PdfReader

import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai

from langchain_community.embeddings import HuggingFaceEmbeddings
# to get embedding models
from langchain_core.documents import Document
# to store text and metadata in a structured way
from langchain_text_splitters import CharacterTextSplitter
# to split the large document into smaller chunks for better processing
from langchain_community.vectorstores import FAISS
# to store the embedding data from the given document for similarity search and retrieval

key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

model = genai.GenerativeModel('gemini-2.5-flash-lite')

def load_embeddings():
    return HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

with st.spinner('Loading embedding model... (ง •̀_•́)ง'):
    embedding_model = load_embeddings()

st.set_page_config('RAG Demo App', page_icon=':robot_face:', layout='wide')

st.title('RAG Assistant :blue[Using Embeddings and LLMs (╭ರ_•́)]')
st.subheader(':green[Your Intelligent Document Assistant (ง •̀_•́)ง]')

uploaded_file = st.file_uploader('Upload the file here in PDF document')

if uploaded_file:
    pdf = PdfReader(uploaded_file)
    
    raw_text = ''
    for page in pdf.pages:
        raw_text += page.extract_text()
        
    if raw_text.strip():
        # remove spaces and check whether the text is empty or not
        # and ensure that the given raw data is empty or not 
        
        doc = Document(page_content=raw_text)
        # to get the content in the given pdf and metadata
        
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        # max char in each chunk is 1000 and the overlap between chunks is 200 to maintain context
        
        
        
        chunk_text = splitter.split_documents([doc])
        # to split the document into smaller chunks for better processing and understanding
        
        text = [i.page_content for i in chunk_text]
        # to fet data as list of similar text 
        
        vector_db = FAISS.from_texts(text, embedding_model)
        
        retrive = vector_db.as_retriever()
        # create a search tool to find the relevent chunks 
        
        st.success('Document proccessed and saved sucessfully!! (ง •̀_•́)ง Ask your question now!!!')
        
        query = st.text_input('Ask your question here 🤝')
        
        if query:
            with st.chat_message('human'):
                
                with st.spinner('Analyzing the document ... ▄︻デ══━一💥'):
                    
                    relevent_data = retrive.invoke(query)
                    # invoke the embedding model and 
                    # search the similar chunks using FAISS
                    # for the given data
                    
                    content = '\n\n'.join([i.page_content for i in relevent_data])
                    
                    prompt = f''' 
                    you are a AI expert. Use the generated content {content} to answer the query {query}. 
                    If you are not sure about the answer, say "I have no content related to this question. 
                    Please ask relevent query to answer"
                    
                    Results in bulletin points '''
                    
                    response = model.generate_content(prompt)
                    
                    st.markdown('##:green[Results 👏]')
                    st.write(response.text)
                    
                    
                    
    else:
        st.warning('Drop the file in PDF Format')




