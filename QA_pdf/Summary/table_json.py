import json


# Function to create JSON structure for a bounding box
def create_bbox(top_left, bottom_right):
    return {
        "top_left_x": top_left[0],
        "top_left_y": top_left[1],
        "bottom_right_x": bottom_right[0],
        "bottom_right_y": bottom_right[1]
    }


# Function to create JSON structure for a page
def create_page(page_number, tables):
    return {
        "page_number": page_number,
        "ables": tables
    }


