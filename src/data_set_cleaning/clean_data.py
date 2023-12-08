import json

file_path = 'yelp_academic_dataset_business.json'

# Initialize an empty list to store individual JSON objects
data = []

# Read the JSON file line by line
with open(file_path, 'r') as f:
    for line in f:
        try:
            # Try to load each line as a JSON object
            json_object = json.loads(line)
            data.append(json_object)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

# Define a filter condition
def filter_condition(bus):
    categories = bus.get("categories")
    city = bus.get("city")
    state = bus.get("state")
    if categories is not None and city is not None and state is not None and "Restaurant" in categories and "Belleville" in city and state == "IL":
        return True
    return False

# Apply the filter and create a new list with filtered data
filtered_data = [bus for bus in data if filter_condition(bus)]
print(len(filtered_data))

# Print the filtered data
with open('filtered_data.json', 'w') as f:
    json.dump(filtered_data, f, indent=2)
