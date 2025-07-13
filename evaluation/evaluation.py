from sentence_transformers import SentenceTransformer, util
import requests
import pandas as pd
import os

model = SentenceTransformer('all-MiniLM-L6-v2')

API_URL = os.getenv("API_URL", os.environ.get("API_URL"))

df = pd.read_csv("./pdf_files/test_data.csv")
predictions = []
for _, row in df.iterrows():
    payload = {
        "question": row["question"],
        "pdf_path": row["pdf_file"]
    }
    print("current file:\n")
    print(row["pdf_file"])
    print("current question:\n")
    print(row["question"])
    try:
        res = requests.post(API_URL, json=payload)
        answer = res.json().get("answer", "[ERROR]")
    except Exception as e:
        answer = f"[ERROR] {e}"
    predictions.append(answer)

df["predicted_answer"] = predictions
df.to_csv("./pdf_files/test_data.csv", index=False)
print("Answers saved to test_data.csv")

def calc_similarity(pred, gold):
    emb1 = model.encode(pred, convert_to_tensor=True)
    emb2 = model.encode(gold, convert_to_tensor=True)
    return util.cos_sim(emb1, emb2).item()

df['predicted_answer_similarity'] = [calc_similarity(p, g) for p, g in zip(df['predicted_answer'], df['gpt_answer'])]

print(f"predicted_answer_similarity: {df['predicted_answer_similarity'].mean():.4f}")
