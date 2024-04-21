from hf_init import initialize_model, initialize_tokenizer
from text_processing import initialize_stopping_criteria, initialize_stop_token_ids, initialize_generate_text_pipeline
from data_loading import load_data
from embedding_vector import split_documents, initialize_embeddings, initialize_vector_store
from conversational_chain import initialize_conversational_chain
import torch


if __name__ == "__main__":
    model_id = 'meta-llama/Llama-2-7b-chat-hf'
    hf_auth = ''
    query = input("Enter your query: ")
    filename = input("Enter filename.csv: ")

    model = initialize_model(model_id, hf_auth)
    tokenizer = initialize_tokenizer(model_id, hf_auth)

    stop_list = ['\nHuman:', '\n', '\n']
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    stop_token_ids = initialize_stop_token_ids(stop_list, tokenizer, device)
    stopping_criteria = initialize_stopping_criteria(stop_token_ids)

    generate_text = initialize_generate_text_pipeline(model, tokenizer, stopping_criteria)

    data = load_data(filename)
    all_splits = split_documents(data)

    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {"device": "cuda"}

    embeddings = initialize_embeddings(model_name=model_name, model_kwargs=model_kwargs)
    vectorstore = initialize_vector_store(all_splits, embeddings)

    chain = initialize_conversational_chain(generate_text, vectorstore)

    chat_history = []
    result = chain({"question": query, "chat_history": chat_history})

    print(result['answer'])


