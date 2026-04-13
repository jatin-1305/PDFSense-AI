import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)

    return chunks


def main():
    #calling dot env, which stores the API keys in the .env file
    load_dotenv()

    st.set_page_config(page_title="PDFSense AI", page_icon=":books:")
    st.header("PDFSense AI :books:")
    st.text_input("Ask a question about your documents", placeholder="e.g. What is the main idea of the document?")
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click analyze",type="pdf", accept_multiple_files=True)
        if st.button("Analyze"):
            with st.spinner("Analyzing..."):
                #read the PDFs
                raw_text = get_pdf_text(pdf_docs)

                #split the text into chunks
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)
                #create a vector store
                # vectorstore = get_vectorstore(text_chunks)
                #create a chat history

if __name__ == "__main__":
    main() 