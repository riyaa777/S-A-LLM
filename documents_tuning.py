# Imports
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# Define a function to load documents
def load_documents(directory_path):
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(os.path.join(directory_path, filename), 'r') as file:
                document_text = file.read()
                documents.append(document_text)
    return documents

# Load documents
docs = load_documents("./documents_folder")

# Index documents
corpus = docs  # No need to use .text for each document, assuming it's already text data
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(corpus)

# Define a function to search documents
def search_documents(query, docs, vectorizer, n=5):
    query_vec = vectorizer.transform([query])
    cos_sim = cosine_similarity(query_vec, doc_vectors).flatten()
    relevant_docs = np.argsort(cos_sim)[-n:][::-1]

    # Extract answers
    answers = []

    for doc_id in relevant_docs:
        doc = docs[doc_id]
        answers.append(doc)  # Append the entire document, no keyword matching

    return "\n".join(answers)

# Example usage
query = "Your search query here"
result = search_documents(query, docs, vectorizer)
print(result)
