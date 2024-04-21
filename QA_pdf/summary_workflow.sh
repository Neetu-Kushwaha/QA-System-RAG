#!/bin/bash

# Step 1: Execute main.py in Summary directory
echo "Step 1: Executing main.py in Summary directory"
cd Summary
python main.py
cd ..

# Step 2: Execute script.sh in Summary/Image_summary directory
echo "Step 2: Executing script.sh in Summary/Image_summary directory"
cd Summary/Image_summary
./script.sh
cd ../..

# Step 3: Generate JSON summaries for images
echo "Step 3: Generating JSON summaries for images"
cd Summary/Image_summary
python summary_json.py
cd ../..

echo "Workflow completed."
