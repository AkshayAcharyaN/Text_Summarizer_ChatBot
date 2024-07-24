# test_model.py

from transformers import LEDTokenizer, LEDForConditionalGeneration

def test_model():
    try:
        tokenizer = LEDTokenizer.from_pretrained("allenai/led-base-16384")
        model = LEDForConditionalGeneration.from_pretrained("allenai/led-base-16384")
        print("LED model and tokenizer loaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_model()
