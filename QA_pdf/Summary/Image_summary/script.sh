#!/bin/bash

# Define the directory containing the images
IMG_DIR=~/Documents/New_Assignment/figures/

# Loop through each image in the directory
for img in "${IMG_DIR}"*.jpg; do
    # Extract the base name of the image without extension
    base_name=$(basename "$img" .jpg)

    # Define the output file name based on the image name
    output_file="${IMG_DIR}${base_name}.txt"

    # Execute the command and save the output to the defined output file
    ./llava-cli -m models/llava/ggml-model-q4_k.gguf --mmproj models/llava/mmproj-model-f16.gguf --image "$img" --temp 0.1 -p "Please generate a summary of image that is a plot in detail" > "$output_file"
done
