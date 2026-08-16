import requests
 
## Making a GET request
# r = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# print(r.status_code)
# print(r.json())



## Making POST request
payload = {
    "title": "My New Post",
    "body": "This is the content.",
    "userId": 1
}

res = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)

print(f"Status Code: {res.status_code}")
print(res.json())