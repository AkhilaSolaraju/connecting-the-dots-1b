# Approach Explanation

## Goal:
To extract and rank the most relevant sections from input PDFs based on a defined persona and job-to-be-done, under strict CPU, size, and time constraints.

## Step-by-Step Methodology:

1. **PDF Parsing**:
   - We use `PyPDF2` to extract plain text from each page of every PDF.
   - Each PDF is scanned page-by-page, and content is stored for evaluation.

2. **Relevance Ranking**:
   - We tokenize the persona and job description into keywords.
   - Each page of each PDF is scored based on the number of matching keywords.
   - Pages with high keyword matches are assumed more relevant and are ranked accordingly.

3. **Output Formatting**:
   - We generate a JSON output with three parts: metadata, top relevant sections, and detailed refined text snippets.
   - The result is saved to `output.json`.

## Constraints:
- Runs under 60 seconds for 3–5 PDFs (text-based).
- Entire solution <1GB including dependencies.
- No internet access, CPU-only environment.

## Generalizability:
- The system works across domains by dynamically identifying keywords from the given persona and task.

