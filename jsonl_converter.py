import json

def convert_to_wildcats_format(json_data):
    converted_data = []

    for entry in json_data:
        prompt = entry["prompt"]
        completion = entry["completion"]

        messages = [
            {"role": "system", "content": "Wildcats is a restaurant recommender for Belleville, IL."},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": completion}
        ]

        converted_entry = {"messages": messages}
        converted_data.append(converted_entry)

    return converted_data

# Read the original JSON Lines data from finetune_training_data_prepared_cleaned.jsonl
input_filename = "finetune_training_data_prepared_cleaned.jsonl"
with open(input_filename, 'r') as file:
    original_json = [json.loads(line) for line in file]

# Convert to Wildcats format
converted_json = convert_to_wildcats_format(original_json)

# Save the converted data to a JSON Lines file named finetune_training_data_gpt3.5.jsonl
output_filename = "finetune_training_data_gpt3.5.jsonl"
with open(output_filename, 'w') as file:
    for entry in converted_json:
        file.write(json.dumps(entry) + '\n')

print(f"The data has been saved to {output_filename}")
