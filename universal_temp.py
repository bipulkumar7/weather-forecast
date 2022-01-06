from flask import Flask, jsonify, request, redirect
import requests
app = Flask(__name__)

"""
Requesting from Data
"""
@app.route("/")
def index():
    return "<h1>Hello this app is to find the temperature of any location on earth<h1>"


@app.route('/theform', methods=['GET', 'POST'])
def theform():
    return '''<form method="POST" action="temperature">
                      <label for="fname">Latitude:</label>
                      <input type="text" name="latitude">
                      <label for="fname">Longitude:</label>
                      <input type="text" name="longitude">
                      <input type="submit" value="Submit">
                  </form>'''


@app.route('/temperature', methods=['POST'])
def process():
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    r = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")
    json_object = r.json()


    Location = json_object['properties']['relativeLocation']['properties']['city']
    Link = json_object['properties']['forecast']
    

    r = requests.get(Link)
    json_object = r.json()
    json_object['properties']['periods']
    var = 'Tonight'

    for i in json_object['properties']['periods']:
        for key, value in i.items():

            if key == 'name' and value == var:
                j = i
                break

    temp_f = float(j['temperature'])
    temp_c = int((temp_f - 32 ) * 5 / 9)


    return '<h1>Hello  the {} temperature is {} Celsius <h1>'.format(Location, temp_c)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
