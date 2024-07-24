import streamlit as st
from PyPDF2 import PdfReader
from summarizer import summarize_text
from QA_chatbot import ask_question

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def main():
    st.title("PDF Text Summarization and Q&A Chatbot")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        raw_text = extract_text_from_pdf(uploaded_file)
        st.write("### Extracted Text")
        st.text_area("Extracted Text", raw_text, height=300)
        
        if st.button("Summarize"):
            summary = summarize_text(raw_text)
            st.write("### Summary")
            st.write(summary)
        
        st.write("### Ask Questions About the PDF")
        question = st.text_input("Enter your question:")
        if question:
            answer = ask_question(question, raw_text)
            st.write("### Answer")
            st.write(answer)

if __name__ == '__main__':
    main()
