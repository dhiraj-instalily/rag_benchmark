import re

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
