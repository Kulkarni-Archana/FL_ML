import requests

def upload_to_ipfs(file_path):
    # API endpoint for adding a file to IPFS
    ipfs_api_url = 'http://localhost:5001/api/v0/add'

    # Open the file and read its contents
    with open(file_path, 'rb') as file:
        files = {'file': file}

        # Make a POST request to the IPFS API
        response = requests.post(ipfs_api_url, files=files)

        # Check if the request was successful
        if response.status_code == 200:
            ipfs_hash = response.json()['Hash']
            print(f'File uploaded successfully to IPFS with hash: {ipfs_hash}')
            return ipfs_hash
        else:
            print(f'Failed to upload file to IPFS. Status code: {response.status_code}')
            return None

# Example usage
file_path = 'data.csv'  # Replace this with the path to your file
upload_to_ipfs(file_path)
