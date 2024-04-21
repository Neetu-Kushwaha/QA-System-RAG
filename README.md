# Workflow Execution README

## Overview
This README provides an overview of two workflow execution scripts: one for automating data processing, image summarization, and table summary generation, and another for creating a QA system.

## 1. Data Processing Workflow
### Overview
This workflow automates the process of data processing, image summarization, and table summary generation.

#### Data Processing
<details>
<summary>Step Description</summary>
This step involves processing data to extract images and table summaries from PDF documents.
</details>

<details>
<summary>Actions Taken</summary>
- Executed `main.py`: Processes data and generates images. Handles table summarization internally.
- Generated `document_data.json`: Contains information about extracted tables, including page numbers and bounding box coordinates.
</details>

#### Image Summarization
<details>
<summary>Step Description</summary>
Focuses on summarizing images generated during the data processing phase.
</details>

<details>
<summary>Actions Taken</summary>
- Ran `script.sh`: Processes images using the unstructured library.
- Utilized the LLAVA model for summarization: Each figure is summarized, and summaries are saved in separate text files.
- Generated JSON summaries: Summaries for figures are created using `summary_json.py`. (Filename: `summary_figure.json`)
</details>

#### Table Summarization
<details>
<summary>Step Description</summary>
Involves summarizing tables extracted during the data processing phase.
</details>

<details>
<summary>Actions Taken</summary>
- Executed the summarization module: `summarization.py` creates table summaries.
- Utilized the Chatollama model: Generates table summaries.
- Saved table summaries: Summaries are stored in JSON format. (Filename: `document_data_with_summaries.json`)
</details>

### Running the Workflow
To run the workflow, execute `./summary_workflow.sh` in the terminal. Ensure the script has executable permissions using `chmod +x summary_workflow.sh`.

### Note
Bounding box information for images is not included in the JSON files.

## 2. QA System Workflow
### Overview
This workflow creates a QA system.

#### Input
Prompt the user to ask a question.

#### Execution Steps
- Prompt the user to input a question.
- Run `main.py`.
- Call the FAISS vector database to retrieve relevant information.
- Utilize `generation.py`, which employs Ollama2, to generate an answer based on the provided context and query.
- Display the output answer to the user.
- Alternatively, utilize the `meta_llama_QA` folder containing a QA utilizing the model `metallama/Llama-2-7b-chat-hf` from Hugging Face with Hugging

### Running the Workflow
To run the QA system, follow the execution steps mentioned above.

### Note
Ensure all dependencies are installed as per the requirements.

---

### LLAVA Model Usage

To use the LLAVA model locally on a Mac laptop, follow these steps:

1. Clone llama.cpp.
2. Download the LLaVA model: `mmproj-model-f16.gguf` and one of `ggml-model-[f16|q5_k|q4_k].gguf` from the LLaVA 7b repo.
3. Build:

mkdir build && cd build && cmake ..
cmake --build .
4. Run inference across images using `script.sh`.

---

### Installation Requirements

Ensure the following Python packages are installed:

!pip install langchain unstructured[all-docs] pydantic lxml