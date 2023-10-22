#!/usr/bin/python3
"""
This is a Flask web application.
"""

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="templates")


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    """
    Displays the main HBnB filters HTML page.
    """
    states = storage.all(State)
    states = dict(sorted(states.items(), key=lambda item: item[1].name))
    cities = storage.all(City)
    cities = dict(sorted(cities.items(), key=lambda item: item[1].name))
    amenities = storage.all(Amenity)
    amenities = dict(sorted(amenities.items(), key=lambda item: item[1].name))
    places = storage.all(Place)
    places = dict(sorted(places.items(), key=lambda item: item[1].name))
    users = storage.all(User)

    return render_template("100-hbnb.html", states=states, cities=cities,
                           amenities=amenities, places=places, users=users)


@app.teardown_appcontext
def teardown(error):
    """
    Removes the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
