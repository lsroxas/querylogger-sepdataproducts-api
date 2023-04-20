import requests

# Define your API endpoint and parameters
url = "https://api.openai.com/v1/engines/davinci-codex/completions"
data = {
    "prompt": "Write a Python script that generates a random number between 1 and 10",
    "max_tokens": 50
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY_HERE"
}

# Make the API call
response = requests.post(url, json=data, headers=headers)

# Parse the response and print the generated text
json_data = response.json()
generated_text = json_data["choices"][0]["text"]
print(generated_text)
