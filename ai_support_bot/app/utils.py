from pypdf import PdfReader
from langchain_text_splitters import CharacterTextSplitter

def load_pdf(file):
    try:
        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content

        return text

    except Exception as e:
        print("Error:", e)
        return ""

def split_text(text):
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_text(text)