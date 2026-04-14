from pypdf import PdfReader

# 📄 Load PDF text
def load_pdf(file):
    try:
        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        return text

    except Exception as e:
        print("PDF LOADING ERROR:", e)
        return ""


# ✂️ Split text into chunks for embeddings
def split_text(text, chunk_size=500, overlap=50):
    try:
        chunks = []

        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start = end - overlap  # overlap for better context

        return chunks

    except Exception as e:
        print("CHUNKING ERROR:", e)
        return []