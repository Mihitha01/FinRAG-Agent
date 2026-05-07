import re

def clean_text(text: str) -> str:
    """
    Normalizes raw text by fixing broken hyphens and squashing whitespaces.
    """
    # Fix hyphenated words split across lines (e.g., "finan-\ncial" -> "financial")
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    
    # Replace any sequence of whitespace (newlines, tabs, multiple spaces) with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading and trailing spaces
    return text.strip()

def clean_documents(documents: list[dict]) -> list[dict]:
    """
    Iterates through a list of document dictionaries and cleans their text.
    """
    cleaned_docs = []
    
    for doc in documents:
        cleaned_text = clean_text(doc["text"])
        
        # Only keep documents that still have text after cleaning
        if cleaned_text:
            cleaned_docs.append({
                "text": cleaned_text,
                "metadata": doc["metadata"] # Preserve original metadata
            })
            
    return cleaned_docs