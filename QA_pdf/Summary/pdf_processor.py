import os
from unstructured.partition.pdf import partition_pdf
from unstructured_inference.models.base import DEFAULT_MODEL


class PDFProcessor:
    """Class to handle PDF processing."""
    def __init__(self, path):
        """
        Initialize PDFProcessor with the specified path.

        Parameters:
            path (str): Path to the directory containing PDF files.
        """
        self.path = path

    def read_pdf(self, filename):
        """
        Read a PDF file and extract its elements.

        Parameters:
            filename (str): Name of the PDF file to read.

        Returns:
            list: A list of elements extracted from the PDF.
        """

        try:
            # Get elements
            raw_pdf_elements = partition_pdf(
                filename=os.path.join(self.path, filename),

                # Using pdf format to find embedded image blocks# Using pdf format to find embedded image blocks
                extract_images_in_pdf=False,

                # Use layout model (YOLOX) to get bounding boxes (for tables) and find titles
                # Titles are any sub-section of the document
                infer_table_structure=True,

                # Post processing to aggregate text once we have the title
                chunking_strategy="by_title",

                # Chunking params to aggregate text blocks
                # Attempt to create a new chunk 3800 chars
                # Attempt to keep chunks > 2000 chars
                # Hard max on chunks
                max_characters=4000,
                new_after_n_chars=3800,
                combine_text_under_n_chars=2000,
                image_output_dir_path=self.path,
            )
            return raw_pdf_elements

        except Exception as e:
            print(f"Error reading PDF file: {e}")
            return None