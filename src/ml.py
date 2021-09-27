import random


class MLModel:
    """
    A fake ML Model class for illustrative purposes.
    """

    def predict(self, input: str):
        return {
            "prediction": random.choice(["Positive", "Neutral", "Negative"]),
            "confidence": random.random(),
            "original_text": input,
        }
