import streamlit as st
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
# from langchain.llms import HuggingFaceHub
from streamlit_chat import message
def get_pdf_text(pdfs):
  text=""
  for pdf in pdfs:
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
      text+= page.extract_text()
  return text

def get_text_chunks(text):
  text_splitter = CharacterTextSplitter(separator="\n",
  chunk_size=1000, chunk_overlap = 200, length_function=len)
  chunks = text_splitter.split_text(text)
  return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
#     embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
#     llm = HuggingFaceHub(repo_id="google/flan-t5-xxl")
    llm = ChatOpenAI(max_tokens=2000)
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain
def user_input(user_question):
  response = st.session_state.conversation({'question':user_question})
  st.session_state.chat_history = response['chat_history']
  for i, messages in enumerate(st.session_state.chat_history):
      if i % 2 == 0:
          message(messages.content, is_user=True)
      else:
          message(messages.content)
def main():
  load_dotenv()
  st.set_page_config(page_title="ASK AITELA BOT")
  if "conversation" not in st.session_state:
    st.session_state.conversation = None
  if "chat_history" not in st.session_state:
    st.session_state.chat_history = None

  st.header("ASK AITELA BOT")
  user_question = st.text_input("Ask anything about AITELA...")
  if user_question:
    user_input(user_question)
  with st.sidebar:
    st.subheader("Your Documents")
    pdfs = st.file_uploader("Upload here", accept_multiple_files=True)
    if st.button("Process"):
      with st.spinner("Processing"):
        raw_text = get_pdf_text(pdfs)
#         print(raw_text)
        chunks = get_text_chunks(raw_text)
        vectorstore = get_vectorstore(chunks)
        st.session_state.conversation = get_conversation_chain(vectorstore)
        st.success("Processing Complete !")

if __name__ == '__main__':
  main()