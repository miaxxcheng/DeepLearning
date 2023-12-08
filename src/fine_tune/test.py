
import openai

openai.api_key = "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"

# import openai
# openai.Completion.create(
#     model="ft:babbage-002:yonsei-univ::8TIWfiFc",
#     prompt="show me pizza places in the city center")

# print()

model_name = 'ft:babbage-002:yonsei-univ::8TIWfiFc'
prompt = "show me pizza places in the city center"

response = openai.Completion.create(
    model=model_name,
    prompt=prompt,
    temperature=0.7,
    max_tokens=150
)

generated_output = response['choices'][0]['text']
print(generated_output)

response = openai.Completion.create(
    model=model_name,
    prompt="Any vegan restaurants with a variety of plant-based options?",
    temperature=0.7,
    max_tokens=150
)

generated_output = response['choices'][0]['text']

print(generated_output)
