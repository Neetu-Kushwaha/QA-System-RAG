import os
import json

# Directory containing the text files
directory = "./figures/"

# Initialize an empty dictionary to store the data
all_data = {}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Check if the file is a text file
    if filename.endswith(".txt"):
        # Read the contents of the text file
        with open(os.path.join(directory, filename), "r") as file:
            text = file.read()

        # Find the index of the last occurrence of the desired marker
        marker = "encode_image_with_clip: image encoded in"
        last_index = text.rfind(marker)

        # Find the index of the end of the line containing the marker
        end_of_line_index = text.find("\n", last_index)

        # Extract the text after the line containing the marker
        desired_text = text[end_of_line_index + 1:].strip()

        # Remove the file extension to get the key
        key = os.path.splitext(filename)[0]

        # Store the data in the dictionary
        all_data[key] = desired_text

# Write the dictionary to a JSON file
with open("summary_figure.json", "w") as json_file:
    json.dump(all_data, json_file, indent=4)
