from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class QAAgent:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def run(self, query, docs):
        context = "\n\n".join([doc["text"] for doc in docs])

        prompt = f"""
Answer the question using only the context below.
If the answer is not found, say:
I could not find this information in the uploaded PDFs.

Context:
{context}

Question:
{query}

Answer:
"""

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            max_length=1024,
            truncation=True
        )

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=250,
                do_sample=False
            )

        answer = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return answer