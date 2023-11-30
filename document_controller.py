import os
from pdfminer.high_level import extract_text
import docx2txt
import tika
from tika import parser
import pdfminer
tika.initVM()

def extract_text(file_path):
  if file_path.endswith('.pdf'):
    return extract_text_from_pdf(file_path)
  elif file_path.endswith('.docx'):
    return extract_text_from_docx(file_path)
  else:
    return extract_text_from_file(file_path)



def extract_text_from_pdf(pdf_file):

  pdf_text = ""

  try:
    pages = pdfminer.high_level.extract_pages(pdf_file)
    for page in pages:
      pdf_text += page.extract_text()

  except:
    print(f"Error extracting pages from PDF: {pdf_file}")

  return pdf_text

def extract_text_from_docx(docx_file):
  docx_text = docx2txt.process(docx_file)
  return docx_text

def extract_text_from_file(file_path):
  parsed = parser.from_file(file_path)
  return parsed["content"]

def search_and_chat_with_documents(query, documents_folder):

  matching_docs = []

  for filename in os.listdir(documents_folder):
    if filename.endswith('.txt'):
      file_path = os.path.join(documents_folder, filename)
      with open(file_path) as f:
        doc_text = f.read()
      if query.lower() in doc_text.lower():
        matching_docs.append(doc_text)

  for filename in os.listdir(documents_folder):
    if filename.endswith('.pdf') or filename.endswith('.docx'):
      file_path = os.path.join(documents_folder, filename)
      doc_text = extract_text(file_path)
      if query.lower() in doc_text.lower():
        matching_docs.append(doc_text)

  if matching_docs:
    return matching_docs

  else:
    return "No matching documents found."
