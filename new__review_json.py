import json

def merge_json_by_business_id(business_json_file, review_json_file, output_file):
    # Read the contents of the business JSON file
    with open(business_json_file, 'r') as file1:
        business_data = {item['business_id']: item['name'] for item in [json.loads(line) for line in file1]}

    # Read the contents of the review JSON file
    with open(review_json_file, 'r') as file2:
        # Read and parse each line as a separate JSON object
        review_data = [json.loads(line) for line in file2]

    # Add the 'name' from the business file to the review file based on 'business_id'
    for review in review_data:
        business_id = review.get('business_id')
        if business_id in business_data:
            review['business_name'] = business_data[business_id]

    # Write the combined data to a new JSON file
    with open(output_file, 'w') as output_file:
        json.dump(review_data, output_file, indent=2)

        
business_json_file = 'yelp_academic_dataset_business.json'
review_json_file = 'yelp_academic_dataset_review.json'
output_file = 'new_yelp_academic_dataset_review.json'

merge_json_by_business_id(business_json_file, review_json_file, output_file)