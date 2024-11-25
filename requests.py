import requests

# Base URL of your website's API
base_url = 'https://your-website.com/api'

# Function to send GET request
def send_get_request(endpoint):
    url = f"{base_url}/{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        print("GET Request successful")
        print(response.json())  # Assuming the API returns JSON
    else:
        print(f"GET Request failed with status code {response.status_code}")

# Function to send POST request
def send_post_request(endpoint, data):
    url = f"{base_url}/{endpoint}"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print("POST Request successful")
        print(response.json())
    else:
        print(f"POST Request failed with status code {response.status_code}")

# Function to send PUT request
def send_put_request(endpoint, data):
    url = f"{base_url}/{endpoint}"
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 200:
        print("PUT Request successful")
        print(response.json())
    else:
        print(f"PUT Request failed with status code {response.status_code}")

# Function to send DELETE request
def send_delete_request(endpoint):
    url = f"{base_url}/{endpoint}"
    response = requests.delete(url)
    if response.status_code == 204:
        print("DELETE Request successful")
    else:
        print(f"DELETE Request failed with status code {response.status_code}")

# Example usage of the functions
if __name__ == "__main__":
    # Send GET request
    send_get_request("users")  # Adjust endpoint

    # Send POST request with sample data
    post_data = {"name": "John Doe", "email": "john.doe@example.com"}
    send_post_request("users", post_data)

    # Send PUT request to update a resource
    put_data = {"name": "Jane Doe", "email": "jane.doe@example.com"}
    send_put_request("users/1", put_data)  # Assuming the user ID is 1

    # Send DELETE request
    send_delete_request("users/1")  # Deleting the user with ID 1
