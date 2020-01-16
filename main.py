from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def home():
    print(request.form['longitude'])
    print(request.form['latitude'])
    print(request.form['direction'])
    print(request.form['speed'])
    return "Received!"

@app.route("/post-requests", methods=['GET', 'POST'])
def post_request():

    if request.method == 'POST':
        longitude = request.form['longitude']
        latitude = request.form['latitude']
        direction = request.form['direction']
        speed = request.form['speed']

        return '''<h1>The longitude value is: {}</h1>
                    <h1>The latitude value is: {}</h1>
                    <h1>The direction value is {}</h1>
                    <h1>The speed value is {}</h1>'''.format(longitude, latitude, direction, speed)
        

    return '''<form method="POST">
                Longitude: <input type="text" name="longitude"><br>
                Latitude: <input type="text" name="latitude"><br>
                Direction: <input type="text" name="direction"><br>
                Speed: <input type="text" name="speed"><br>
                <input type="submit" value="Submit"><br>
            </form>'''

@app.route("/json-post-requests", methods=['POST'])
def json_request():
    req_data = request.get_json()

    longitude = req_data['longitude']
    latitude = req_data['latitude']
    direction = req_data['direction']
    speed = req_data['speed']

    return '''
            Longitude: {}
            Latitude: {}
            Direction: {}
            Speed: {}'''.format(longitude, latitude, direction, speed)

if __name__ == "__main__":
    app.run(debug=True)
