# connecting-the-dots-1b
# Persona-Driven Document Intelligence – Round 1B

## Project Overview

This project is a solution for Round 1B of the Persona-Driven Document Intelligence challenge. It processes PDF documents to extract and rank information that is relevant to a specific persona and job-to-be-done (JTBD).

## Example Use Case
- Persona: Investment Analyst  
- Job to be Done: Analyze revenue trends, R&D investments, and market positioning strategies
  
## Folder Structure
```
connecting-the-dots-1b/
├── main.py                   # Entry point of the pipeline
├── requirements.txt          # Python dependencies
├── Dockerfile                # Containerization script
├── approach_explanation.md  # Description of approach used
├── input_pdfs/               # Folder containing input PDF files
│   ├── file1.pdf
│   ├── file2.pdf
│   └── file3.pdf
└── output.json               # Final extracted and ranked results
```


## Setup Instructions
### 1. Install Dependencies

Run the following command to install the required Python libraries:
pip install -r requirements.txt
### 2. Add PDF Files

Place at least three PDF files into the input_pdfs/ folder. Each file should contain 10 to 30 pages of mostly textual content.

### 3. Run the Script
   
You can run the system using the command line:


python main.py
Or, if using a Jupyter notebook:



!python main.py


You will be prompted to enter:
Persona:
Job to be Done:
The output will be saved to output.json.

## Docker Instructions
To build and run the solution in a Docker container:

docker build -t doc-intelligence .

docker run -v $(pwd)/input_pdfs:/app/input_pdfs doc-intelligence
