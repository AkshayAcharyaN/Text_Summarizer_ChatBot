# test_model.py

from transformers import T5Tokenizer, T5ForConditionalGeneration

def test_model():
    try:
        tokenizer = T5Tokenizer.from_pretrained("t5-base")
        model = T5ForConditionalGeneration.from_pretrained("t5-base")
        print("T5 model and tokenizer loaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":  
    test_model()
