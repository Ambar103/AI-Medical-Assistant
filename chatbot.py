from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-large")

def generate_answer(context, question):
    prompt = f"""
Answer the question using the context.

Context:
{context}

Question:
{question}

Answer clearly:
"""

    result = generator(
        prompt,
        max_length=150,
        do_sample=False
    )

    raw_answer = result[0]['generated_text']

    # 🔥 POST-PROCESSING (THIS IS THE KEY)
    causes = []
    symptoms = []
    conditions = []

    for line in context.split("\n"):
        text = line.lower()

        if "caused by" in text or "include" in text:
            if "caused by" in text:
                parts = text.split("caused by")[-1]
                causes.extend([c.strip() for c in parts.split(",")])

        if "symptoms include" in text:
            parts = text.split("symptoms include")[-1]
            symptoms.extend([s.strip() for s in parts.split(",")])

        # extract condition names
        if "symptoms include" in text:
            condition = text.split(" symptoms")[0]
            conditions.append(condition.strip())

    # clean duplicates
    causes_text = "\n- ".join(causes[:5])
    symptoms_text = "\n- ".join(symptoms[:5])
    conditions_text = "\n- ".join(conditions[:5])

    # 🔥 FINAL STRUCTURED OUTPUT
    final_answer = f"""
Possible causes:
- {causes_text}

Symptoms:
- {symptoms_text}

Related conditions:
- {conditions_text}
"""
    return final_answer.strip()