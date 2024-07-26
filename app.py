# app.py

import streamlit as st
from pdf_extractor import extract_text_from_pdf
from text_cleaner import clean_text
from summarizer import Summarizer

def main():
    st.title("PDF Text Summarization App")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Extract text from PDF
        with st.spinner('Extracting text from PDF...'):
            pdf_text = extract_text_from_pdf(uploaded_file)

        # Clean the extracted text
        with st.spinner('Cleaning extracted text...'):
            cleaned_text = clean_text(pdf_text)

        st.subheader("Extracted Text")
        st.write(cleaned_text[:5000])  # Display first 5000 characters of the extracted text

        if st.button("Summarize"):
            summarizer = Summarizer()
            with st.spinner('Generating summary...'):
                summary = summarizer.summarize(cleaned_text)
            
            st.subheader("Summary")
            st.write(summary)

if __name__ == "__main__":
    main()
