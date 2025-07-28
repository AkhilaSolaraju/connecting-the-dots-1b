import os
import json
from PyPDF2 import PdfReader
from datetime import datetime

def extract_relevant_sections(text, persona, job):
    keywords = persona.lower().split() + job.lower().split()
    sections = []
    for i, page_text in enumerate(text):
        lower_text = page_text.lower()
        score = sum(1 for kw in keywords if kw in lower_text)
        if score > 0:
            sections.append({
                "document": "unknown",
                "page_number": i + 1,
                "section_title": f"Page {i+1}",
                "importance_rank": score
            })
    sections.sort(key=lambda x: -x["importance_rank"])
    return sections[:5]

def extract_text_from_pdfs(folder_path):
    all_text = []
    doc_names = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder_path, filename))
            text_per_page = [page.extract_text() or "" for page in reader.pages]
            all_text.append((filename, text_per_page))
            doc_names.append(filename)
    return all_text, doc_names

def analyze_documents(persona, job, pdf_folder="input_pdfs"):
    docs, doc_names = extract_text_from_pdfs(pdf_folder)
    output = {
        "metadata": {
            "input_documents": doc_names,
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for doc_name, text in docs:
        sections = extract_relevant_sections(text, persona, job)
        for sec in sections:
            sec["document"] = doc_name
            output["extracted_sections"].append(sec)
            output["subsection_analysis"].append({
                "document": doc_name,
                "refined_text": text[sec["page_number"] - 1],
                "page_number": sec["page_number"]
            })

    with open("output.json", "w") as f:
        json.dump(output, f, indent=2)
    print("✅ Extraction complete. Output saved to output.json")

if __name__ == "__main__":
    persona = input("Enter Persona: ")
    job = input("Enter Job to be Done: ")
    analyze_documents(persona, job)
