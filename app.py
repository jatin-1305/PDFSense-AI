import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings, HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from htmlTemplates import css, bot_template, user_template
from langchain_groq import ChatGroq


def get_pdf_text(pdf_docs):
    if not pdf_docs:
        return ""
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

def get_vectorstore(text_chunks):
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    embeddings = HuggingFaceInstructEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.warning(
            "Upload at least one PDF in the sidebar, click **Analyze**, then ask your question."
        )
        return
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history = response["chat_history"]


def _render_chat_history(chat_history):
    """Show newest Q&A turn at the top; within each turn, user then assistant."""
    if not chat_history:
        return
    msgs = list(chat_history)
    pairs = []
    i = 0
    while i + 1 < len(msgs):
        first, second = msgs[i], msgs[i + 1]
        # ConversationalRetrievalChain memory is human → ai per turn
        second_type = getattr(second, "type", "")
        if getattr(first, "type", "") == "human" and second_type in ("ai", "assistant"):
            pairs.append((first, second))
            i += 2
        else:
            i += 1
    for human_msg, ai_msg in reversed(pairs):
        st.write(
            user_template.replace("{{MSG}}", human_msg.content),
            unsafe_allow_html=True,
        )
        st.write(
            bot_template.replace("{{MSG}}", ai_msg.content),
            unsafe_allow_html=True,
        )

def main():
    #calling dot env, which stores the API keys in the .env file
    load_dotenv()

    st.set_page_config(page_title="PDFSense AI", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("PDFSense AI :books:")
    user_question = st.text_input(
        "Ask a question about your documents",
        placeholder="e.g. What is the main idea of the document?",
    )
    if user_question and user_question.strip():
        handle_userinput(user_question.strip())

    if st.session_state.chat_history:
        _render_chat_history(st.session_state.chat_history)

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click analyze",type="pdf", accept_multiple_files=True)
        if st.button("Analyze"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF before clicking **Analyze**.")
            else:
                with st.spinner("Analyzing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    if not raw_text.strip():
                        st.session_state.conversation = None
                        st.error(
                            "No text could be read from the PDF(s). "
                            "They may be image-only scans — try a text-based PDF or OCR."
                        )
                    else:
                        text_chunks = get_text_chunks(raw_text)
                        vectorstore = get_vectorstore(text_chunks)
                        st.success(f"Analyzed. You can ask questions now.")
                        st.session_state.conversation = get_conversation_chain(vectorstore)

if __name__ == "__main__":
    main() 