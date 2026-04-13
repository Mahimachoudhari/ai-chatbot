from pypdf import PdfReader
from langchain_text_splitters import CharacterTextSplitter

def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def split_text(text):
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_text(text)