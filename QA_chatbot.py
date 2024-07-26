from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")

# Initialize the pipeline for question answering
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

def ask_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']
