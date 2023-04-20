import requests
import argparse

# Define command line arguments
parser = argparse.ArgumentParser(description='Make an API call.')
parser.add_argument('url', type=str, help='API endpoint URL')
parser.add_argument('--param1', type=str, help='API parameter 1')
parser.add_argument('--param2', type=str, help='API parameter 2')
parser.add_argument('--apikey', type=str, required=True, help='API key')
args = parser.parse_args()

# Define API parameters and headers
params = {
    'param1': args.param1,
    'param2': args.param2
}
headers = {
    'Authorization': 'Bearer ' + args.apikey
}

# Make API call
response = requests.get(args.url, params=params, headers=headers)

# Print response
print(response.text)
