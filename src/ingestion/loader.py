from pathlib import Path
from pypdf import PdfReader

def load_pdf(file_path: str) -> list[dict]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    reader = PdfReader(str(path))
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text:
            pages.append(
                {
                    "text": text,
                    "metadata": {
                        "source": path.name,
                        "source_path": str(path),
                        "page": page_number,
                        "file_type": "pdf",
                    },
                }
            )

    return pages

def load_txt(file_path: str) -> list[dict]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    text = path.read_text(encoding="utf-8")

    return [
        {
            "text": text,
            "metadata": {
                "source": path.name,
                "source_path": str(path),
                "page": None,
                "file_type": "txt",
            },
        }
    ]


def load_document(file_path: str) -> list[dict]:
    path = Path(file_path)
    file_type = path.suffix.lower()

    if file_type == ".pdf":
        return load_pdf(str(path))

    if file_type == ".txt":
        return load_txt(str(path))

    raise ValueError(f"Unsupported file type: {file_type}")