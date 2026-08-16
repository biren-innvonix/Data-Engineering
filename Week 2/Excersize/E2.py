import requests
import json

api_url = "https://jsonplaceholder.typicode.com/posts"
output_file = "api_data.json"

response = requests.get(api_url)
data = response.json()

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Data successfully saved to '{output_file}'")