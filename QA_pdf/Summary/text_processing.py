from element import Element


def count_tables_text(raw_pdf_elements):
    """
    Count the number of tables and text elements in a list of PDF elements.

    Parameters:
        raw_pdf_elements (list): List of PDF elements.

    Returns:
        dict: A dictionary containing the counts of tables and text elements.
    """

    # Create a dictionary to store counts of each type
    category_counts = {}
    for element in raw_pdf_elements:
        category = str(type(element))
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1

    # Unique_categories will have unique elements
    unique_categories = set(category_counts.keys())

    return category_counts


def categorize_by_type(raw_pdf_elements):
    """
    Categorize PDF elements into tables and text.

    Parameters:
        raw_pdf_elements (list): List of raw PDF elements.

    Returns:
        tuple: A tuple containing lists of table elements and text elements.
    """

    # Categorize by type
    categorized_elements = []
    coordinates_tables = []
    page_number_tables = []
    for element in raw_pdf_elements:
        if "unstructured.documents.elements.Table" in str(type(element)):
            categorized_elements.append(Element(type="table", text=str(element)))
            page_number_tables.append(element.metadata.page_number)
            coordinates_tables.append(element.metadata.coordinates.points)

        elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
            categorized_elements.append(Element(type="text", text=str(element)))

    # Tables
    table_elements = [e for e in categorized_elements if e.type == "table"]

    # Text
    text_elements = [e for e in categorized_elements if e.type == "text"]

    return table_elements, text_elements, page_number_tables, coordinates_tables
