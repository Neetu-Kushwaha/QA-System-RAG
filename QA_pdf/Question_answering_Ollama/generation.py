from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_community.chat_models import ChatOllama


def generation(retriever, question):
    """
    Generate responses based on prompts and embeddings.

    Parameters:
        retriever (object): Object for retrieving relevant information.
        question (str): User question.

    Returns:
        str: Generated response to the user question.
    """
    try:
        # Prompt template
        template = """Answer the question based only on the following context, which can include text and tables:
        {context}
        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)

        # LLM
        model = ChatOllama(model="llama2:13b-chat")
        # Option 2: Multi-modal LLM
        # model = LLaVA

        # RAG pipeline
        chain = (
                {"context": retriever, "question": RunnablePassthrough()}
                | prompt
                | model
                | StrOutputParser()
        )

        output = chain.invoke(question)

        return output

    except Exception as e:
        print(f"Error generating response: {e}")
        return None
