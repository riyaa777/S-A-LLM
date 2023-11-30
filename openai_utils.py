import openai

openai.api_key = "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"
model = "text-davinci-003"

def generate_response(prompt):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0.7,
        max_tokens=50
    )
    return response.choices[0].text.strip()
