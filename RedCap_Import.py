"""
Author: Laura Falk
Date: 2024-11-21
Description: Basic RedCap import template for python users.
Version: 1.0
"""

import requests
import pandas as pd

# This import assumes that no formatting must be done to import from a csv file (column headers match RedCap column headers, values are all valid, etc)

# USER DEFINES THE FOLLOWING 3 VALUES. All other code will remain unaltered.
redcap_uri = "YOUR URL"  # Replace with your REDCap URL
token = "YOUR TOKEN"  # Replace with your REDCap API token
csv_file_path = "c:\\YOURFILEPATH\\testfile.csv"  # Replace with your raw CSV file path. use double backslashes (\\) to avoid issues.

# Load the CSV file into a pandas DataFrame
data = pd.read_csv(csv_file_path)

# Convert the DataFrame to CSV format (this is the format that REDCap expects)
csv_data = data.to_csv(index=False)

# Prepare the parameters for the API request
params = {
    'token': token,
    'content': 'record',  # 'record' means you're uploading records to REDCap
    'format': 'csv',      # Format is CSV
    'type': 'flat',       # 'flat' means each row is a record in REDCap
    'data': csv_data,     # The actual CSV data to upload
    'overwriteBehavior': 'normal',  # 'normal' won't overwrite existing records
    'returnFormat': 'json'  # Response will be in JSON format (useful for checking success or errors)
}

# Make the POST request to the REDCap API
response = requests.post(redcap_uri, data=params)

# Check the response from the REDCap API
if response.status_code == 200:
    print("Data successfully uploaded!")
    print(response.text)  # Print the response from the server (success or error message)
else:
    print(f"Error: {response.status_code}")
    print(response.text)  # Print the error message if the request failed
