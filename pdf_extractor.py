# pdf_extractor.py

import io
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

def extract_text_from_pdf(uploaded_file):
    output_string = io.StringIO()
    with uploaded_file:
        extract_text_to_fp(uploaded_file, output_string, laparams=LAParams(), output_type='text')
    return output_string.getvalue()
