import torch
from transformers import BertModel, BertTokenizer


class Embedder:
    def __init__(self, model = "cointegrated/rubert-tiny2", max_length = 500, overlap = 100):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.tokenizer = BertTokenizer.from_pretrained(model)
        self.model = BertModel.from_pretrained(model)

        self.max_length = max_length
        self.overlap = overlap


    def get_embedding(self, text : str) -> torch.tensor:
        text = text.split()

        embeddings = []

        i = 0
        while i < len(text):
            encoding = self.tokenizer.encode_plus(
                text[i:min(i + self.max_length, len(text))],
                padding=True,
                truncation=True,
                return_tensors="pt"
            ).to(device=self.device)

            with torch.no_grad():
                embeddings.append(self.model(
                    encoding["input_ids"],
                    attention_mask=encoding["attention_mask"]
                ).last_hidden_state.mean(dim=1))

            i += self.max_length - self.overlap

        embeddings = torch.stack(embeddings, dim=0).mean(dim=0)

        return embeddings