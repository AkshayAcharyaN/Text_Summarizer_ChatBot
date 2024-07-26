# summarizer.py

from transformers import T5Tokenizer, T5ForConditionalGeneration

class Summarizer:
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained("t5-base")
        self.model = T5ForConditionalGeneration.from_pretrained("t5-base")

    def summarize(self, text, max_length=200, min_length=30, num_beams=2):
        inputs = self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = self.model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=num_beams, early_stopping=True)
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
