import re
import joblib
import os

def extract_pages_from_documents(documents):
    """
    Extracts pages from a list of documents based on a delimiter pattern.
    """ 
    all_pages = []
    for doc in documents:
        # Splitting the document text into pages using the specified regex pattern.
        pages = re.split(r'^-{3,}$', doc.text, flags=re.MULTILINE)
        all_pages.extend(pages)
    return all_pages


def save_pages_as_markdown(pages, filename):
    """
    Saves the list of pages to a Markdown file.
    """
    with open(filename, 'w') as md_file:
        for i, page in enumerate(pages):
            # Write each page with a header indicating the page number
            md_file.write(f"## Page {i + 1}\n")
            md_file.write(page)
            md_file.write("\n\n---\n\n")

def read_pickle_file(file_path):
    """
    Reads a pickle file and returns the data.
    """
    if os.path.exists(file_path):
        data = joblib.load(file_path)
        return data


file_path = 'output/hayward.pkl'
filename = 'output/hayward.md'
data = read_pickle_file(file_path)
pages = extract_pages_from_documents(data)
save_pages_as_markdown(pages, filename)