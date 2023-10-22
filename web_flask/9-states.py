#!/usr/bin/python3
"""
This is a Flask web application.
"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Display a HTML page with the list of all State objects
    sorted by name (A->Z)
    """
    states = storage.all(State)
    states = dict(sorted(states.items(), key=lambda item: item[1].name))
    return render_template("9-states.html", not_found=False, data=states,
                           id=None)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    states = dict(sorted(storage.all(State).items(), key=lambda
                  item: item[1].name))
    for key, state in states.items():
        if state.id == id:
            s_all = storage.all(City)
            cities = {}
            for key, city in s_all.items():
                if state.id == city.state_id:
                    cities[key] = city
            cities = dict(sorted(cities.items(), key=lambda item: item[1].name)
                          )
            return render_template("9-states.html", name=state.name,
                                   not_found=False, data=cities, id=1)
    return render_template("9-states.html", not_found=True, data=states)


@app.teardown_appcontext
def teardown_context(exception):
    """
    Removes the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
