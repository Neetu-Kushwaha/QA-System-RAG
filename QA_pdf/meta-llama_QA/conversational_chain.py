from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFacePipeline


def initialize_conversational_chain(generate_text, vectorstore):
    llm = HuggingFacePipeline(pipeline=generate_text)
    return ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever(), return_source_documents=True)

