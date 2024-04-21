from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser


def summarize_chains(table_elements, text_elements):
    """
    Summarize tables and text elements.

    Parameters:
        table_elements (list): List of table elements.
        text_elements (list): List of text elements.

    Returns:
        tuple: A tuple containing summaries of tables and text.
    """
    try:
        # Prompt - for summarization
        prompt_text = """You are an assistant tasked with summarizing tables and text. \
        Give a concise summary of the table or text. Table or text chunk: {element} """
        prompt = ChatPromptTemplate.from_template(prompt_text)

        # Chain - for summarization
        model = ChatOllama(model="llama2:13b-chat")
        summarize_chain = {"element": lambda x: x} | prompt | model | StrOutputParser()

        # Table - Summaize each chunk
        tables = [i.text for i in table_elements]
        table_summaries = summarize_chain.batch(tables, {"max_concurrency": 5})

        # Texts - Summarize each chunk
        texts = [i.text for i in text_elements]
        text_summaries = summarize_chain.batch(texts, {"max_concurrency": 5})

        return tables, table_summaries, texts, text_summaries

    except Exception as e:
        # Handle any exceptions that occur during summarization
        print(f"An error occurred during summarization: {str(e)}")
        return None, None, None, None
