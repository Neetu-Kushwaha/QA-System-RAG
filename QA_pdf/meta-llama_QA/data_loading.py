from langchain_community.document_loaders.csv_loader import CSVLoader


def load_data(file_path):
    loader = CSVLoader(file_path=file_path)
    return loader.load()
