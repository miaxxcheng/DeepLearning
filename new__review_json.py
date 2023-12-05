import json

def merge_reviews_with_names(business_file, review_file, output_file):
    # Read the business data from the first file
    try:
        with open(business_file, 'r') as business_file:
            business_data = {item['business_id']: item['name'] for line in business_file if (item := json.loads(line))}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in business file: {e}")
        return

    # Read the reviews from the second file
    try:
        with open(review_file, 'r') as review_file:
            reviews_data = [json.loads(line) for line in review_file]
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in review file: {e}")
        return

    # Merge reviews with business names
    merged_reviews = []
    for review in reviews_data:
        business_id = review.get('business_id')
        if business_id in business_data:
            review['business_name'] = business_data[business_id]
            merged_reviews.append(review)

    # Write the merged data to a new JSON file
    with open(output_file, 'w') as output_file:
        json.dump(merged_reviews, output_file, indent=2)


# Example usage

business_file = 'new_filtered_data_belleville.json'
review_file = 'yelp_academic_dataset_review.json'
output_file = 'new_yelp_academic_dataset_review_belleville3.json'

merge_reviews_with_names(business_file, review_file, output_file)

