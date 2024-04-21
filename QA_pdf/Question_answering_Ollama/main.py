import argparse
from data_loading import load_data
from embedding_vector import split_documents, initialize_embeddings, initialize_vector_store
from generation import generation


def main():
    """
    Main function to orchestrate the entire process.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--filename', type=str, default="../data/combined_summary_data.csv", help='Path with filename to the csv file')

    args = parser.parse_args()
    filename = args.filename

    print(f"Reading CSV file: {filename}")

    # Input question
    query = input("Enter your question: ")

    data = load_data(filename)
    all_splits = split_documents(data)

    model_name = "all-MiniLM-L6-v2"

    embeddings = initialize_embeddings(model_name=model_name)
    vectorstore = initialize_vector_store(all_splits, embeddings)

    # Generate response
    output = generation(vectorstore.as_retriever(), query)

    print(output)


if __name__ == "__main__":
    main()