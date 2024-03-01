from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_slack_status():
    url = "https://status.slack.com/api/v2.0.0/current"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        status = data['status']
        date_created = data['date_created']
        date_updated = data['date_updated']
        active_incidents = data['active_incidents']
        return status, date_created, date_updated, active_incidents
    else:
        return None, None, None, None

@app.route('/')
def index():
    status, date_created, date_updated, active_incidents = get_slack_status()
    return render_template('index.html', status=status, date_created=date_created, date_updated=date_updated, active_incidents=active_incidents)

if __name__ == '__main__':
    app.run(debug=True)
