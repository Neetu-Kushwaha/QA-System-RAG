from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.storage import InMemoryStore
from langchain_core.documents import Document
import uuid
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings


# def embeddings(figure_summaries, table_summaries):
def embeddings(summaries):
    # """
    # Create embeddings for text chunks.
    #
    # Parameters:
    #     figure_summaries (list): Summaries of text chunks.
    #     table_summaries (list): Summaries of table chunks.
    #
    # Returns:
    #     object: Object containing text embeddings.
    # """

    # Check if any of the input values are None
    # if figure_summaries is None or table_summaries is None:
    #     # Handle the case where summarization failed
    #     print("Summarization failed. Exiting.")
    #     return None

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # The vectorstore to use to index the child chunks
    vectorstore = Chroma(
        collection_name="summaries",
        embedding_function=embeddings
    )
    # The storage layer for the parent documents
    store = InMemoryStore()
    id_key = "doc_id"

    # The retriever (empty to start)
    retriever = MultiVectorRetriever(
        vectorstore=vectorstore,
        docstore=store,
        id_key=id_key,
    )

    # Add Figure summaries
    doc_ids = [str(uuid.uuid4()) for _ in summaries]
    summary_texts = [Document(page_content=s, metadata={id_key: doc_ids[i]}) for i, s in enumerate(summaries)]
    retriever.vectorstore.add_documents(summary_texts)
    retriever.docstore.mset(list(zip(doc_ids, summary_texts)))

    # # Add Figure summaries
    # doc_ids = [str(uuid.uuid4()) for _ in figure_summaries]
    # summary_texts = [Document(page_content=s, metadata={id_key: doc_ids[i]}) for i, s in enumerate(figure_summaries)]
    # retriever.vectorstore.add_documents(summary_texts)
    # retriever.docstore.mset(list(zip(doc_ids, summary_texts)))
    #
    # # Add tables
    # table_ids = [str(uuid.uuid4()) for _ in table_summaries]
    # summary_tables = [Document(page_content=s, metadata={id_key: table_ids[i]}) for i, s in enumerate(table_summaries)]
    # retriever.vectorstore.add_documents(summary_tables)
    # retriever.docstore.mset(list(zip(table_ids, summary_tables)))

    return retriever




