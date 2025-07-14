import json, sys

with open("latest_eval.json") as f:
    current = json.load(f)

with open("previous_eval.json") as f:
    previous = json.load(f)

if current["cosine_similarity"] < previous["cosine_similarity"] - 0.01:
    print("❌ Cosine score dropped!")
    sys.exit(1)


print("✅ Evaluation score is stable or improved.")
