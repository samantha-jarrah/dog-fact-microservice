from flask import Flask
import requests

app = Flask(__name__)
    
@app.route('/fact')
def get_fact():
    """Makes request to dogapi.dog to get a dog fact"""

    response = requests.get("https://dogapi.dog/api/v2/facts")
    if response.status_code == 200:
        return response.json()
    return "Error making request!"
    
if __name__ == '__main__':
    app.run(debug = True)
    