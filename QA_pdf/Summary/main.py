from table_json import create_bbox, create_page
import argparse
from pdf_processor import PDFProcessor
from text_processing import count_tables_text, categorize_by_type
from summarization import summarize_chains
import json


def main():
    """
    Main function to orchestrate the entire process.
    """
    print("start")
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--filename', type=str, default="../data/document.pdf", help='Path to the PDF file')
    parser.add_argument('--path', type=str, default='../data/',
                        help='Path to the directory containing the PDF file')
    args = parser.parse_args()
    filename = args.filename
    path = args.path

    print(f"Reading PDF file: {filename}")

    # Process PDF
    processor = PDFProcessor(path)
    raw_pdf_elements = processor.read_pdf(filename)

    # Count tables and text elements
    category_counts = count_tables_text(raw_pdf_elements)

    # Categorize PDF elements
    table_elements, text_elements, page_numbers, coordinates = categorize_by_type(raw_pdf_elements)

    # Creating JSON structure
    document_data = {
        "document_name": "example_document.pdf",
        "pages": []
    }

    # Creating JSON structure for the document
    # Loop through each coordinate set and page number
    for page_number, coords in zip(page_numbers, coordinates):
        # Creating JSON structure for the page
        page_data = {
            "page_number": page_number,
            "tables": [
                {"bounding_box": create_bbox(coords[0], coords[2])}
            ]
        }
        document_data["pages"].append(page_data)

    # Writing JSON to a file
    with open("document_data.json", "w") as json_file:
        json.dump(document_data, json_file, indent=4)

    print("JSON file created successfully.")

    # Summarize tables and text
    tables, table_summaries, texts, text_summaries = summarize_chains(table_elements, text_elements)

    # Read JSON file
    with open("document_data.json", "r") as json_file:
        document_data = json.load(json_file)

    # Add table summaries to the JSON
    for page_data, summary in zip(document_data["pages"], table_summaries):
        for table_data in page_data["tables"]:
            table_data["summary"] = summary.strip()

    # Write updated JSON to file
    with open("document_data_with_summaries.json", "w") as json_file:
        json.dump(document_data, json_file, indent=4)

    print("Table summaries added to JSON file.")


if __name__ == '__main__':
    main()


