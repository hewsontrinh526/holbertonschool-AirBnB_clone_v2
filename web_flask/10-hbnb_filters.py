#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all states
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda amenity: amenity.name)

    specific_state = None

    if id:
        specific_state = next((state for state in states if state.id == id),
                              None)
        if specific_state is not None:
            specific_state.cities = sorted(specific_state.cities,
                                           key=lambda city: city.name)
        states = None

    return render_template('10-hbnb_filters.html', states=states,
                           specific_state=specific_state, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
