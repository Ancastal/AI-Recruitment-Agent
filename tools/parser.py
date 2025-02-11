import pdfplumber
import docx2txt

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF resume."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(docx_path: str) -> str:
    """Extract text from a DOCX resume."""
    return docx2txt.process(docx_path)

def read_text_from_file(file_path: str) -> str:
    """Read text from a file."""
    with open(file_path, "r") as file:
        return file.read()

if __name__ == "__main__":
    print(extract_text_from_pdf("resumes/test.pdf"))
    print(extract_text_from_docx("resumes/test.docx"))
