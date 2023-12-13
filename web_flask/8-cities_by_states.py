#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all states
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
