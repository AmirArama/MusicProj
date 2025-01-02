import requests

# OAuth endpoint
url = "https://auth.brightspace.com/core/connect/token"

# Credentials
username = "boostability.A1"  # or "boostability.S2"
password = "mkjuytrew3456789ikjhyt543wsxcvgy7ikjhg"
client_id = "your_client_id"  # Replace with your actual client ID
client_secret = "your_client_secret"  # Replace with your actual client secret
scope = "data:read"  # Replace with the scope required by Brightspace API

# Data for the POST request
data = {
    "grant_type": "password",
    "username": username,
    "password": password,
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": scope,
}

# Make the POST request
response = requests.post(url, data=data)

# Check for success
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data.get("access_token")
    print("Access Token:", access_token)
else:
    print("Failed to retrieve token. Status Code:", response.status_code)
    print("Response:", response.json())
