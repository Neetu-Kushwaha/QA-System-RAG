import json
import csv


# Read the JSON file containing figure descriptions
with open("./Summary/Image_summary/summary_figure.json", "r") as f:
    figure_descriptions = json.load(f)

# Read the JSON file containing table data and its summaries
with open("./Summary/document_data_with_summaries.json", "r") as f:
    table_data = json.load(f)

# Combine figure and table keys and their corresponding summaries
combined_data = {}

# Assign numerical keys to figure summaries
count = 1
for figure_key, figure_summary in figure_descriptions.items():
    print(figure_key)
    combined_data[figure_key] = figure_summary
    count += 1

# Extract summaries and associate them with page numbers
for page_info in table_data['pages']:
    page_number = page_info['page_number']
    page_tables = page_info.get('tables', [])

    page_summary = ""
    for table in page_tables:
        page_summary += table['summary'] + "\n\n"

    combined_data[page_number] = page_summary.strip()

# Write the combined data to a new JSON file
with open("combined_summary_data.json", "w") as f:
    json.dump(combined_data, f, indent=4)

# Write the combined data to a new CSV file
with open(".data/combined_summary_data.csv", "w", newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Key', 'Summary']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for key, summary in combined_data.items():
        writer.writerow({'Key': key, 'Summary': summary})

print("Combined summary data written to combined_summary_data.json")