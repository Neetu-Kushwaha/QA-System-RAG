from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def split_documents(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    return text_splitter.split_documents(data)


def initialize_embeddings(model_name):
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings


def initialize_vector_store(all_splits, embeddings):
    return FAISS.from_documents(all_splits, embeddings)

