import requests

url = "https://status.slack.com/api/v2.0.0/current"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Access individual fields directly from the parsed JSON data
    status = data['status']
    date_created = data['date_created']
    date_updated = data['date_updated']
    active_incidents = data['active_incidents']

    # Print the values
    print("Status:", status)
    print("Date Created:", date_created)
    print("Date Updated:", date_updated)
    print("Active Incidents:", active_incidents)

else:
    print("Failed to retrieve Slack status.")

