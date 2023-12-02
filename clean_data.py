#import pandas as pd
import json
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

file_path = "yelp_academic_dataset_business.json"

with open(file_path, 'r') as file:
    # Read each line in the file
    lines = file.readlines()

# Initialize an empty list to store the JSON objects
yelp_data = []

# Iterate over each line and load the JSON object
for line in lines:
    try:
        # Attempt to load the JSON object
        business = json.loads(line)
        
        # Check if "Restaurants" is in the categories
        categories = business.get("categories", "")
        if categories is not None and "Restaurants" in categories:
            yelp_data.append(business)

    except json.JSONDecodeError:
        print("Error decoding JSON on this line:", line)

# Now, yelp_data contains only the businesses with "Restaurants" in their categories
for business in yelp_data:
    print(business)