from flask import Flask, jsonify, request
from flights_data import flights
from utils import search_flight, get_index

app = Flask(__name__)


# GETTING INFORMATION

@app.route('/')
def hello():
    return {'hello': 'Universe'}

@app.route('/flights')
def get_flights():
    return jsonify(flights)

@app.route('/flights/<int:id>')
def get_flight_by_id(id):
    flight = search_flight(id, flights)
    return jsonify(flight)

@app.route('/flights', methods=['POST'])
def add_flight():
    flight = request.get_json()
    flights.append(flight)
    return flight

if __name__ == '__main__':
    app.run(debug=True)
