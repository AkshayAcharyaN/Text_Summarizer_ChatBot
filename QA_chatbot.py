from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def ask_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']
