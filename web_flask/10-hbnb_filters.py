#!/usr/bin/python3
""" Nameless Module for Flask """
from flask import Flask, render_template
from models.__init__ import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """
    Print out HTML lisitng out all Cities by their States
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    cities = storage.all(City).values()
    cities = sorted(cities, key=lambda city: city.name)
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
