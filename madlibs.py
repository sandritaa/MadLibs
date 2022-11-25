"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    return render_template("compliment.html")

@app.route("/game")
def show_madlib_forme():
    
    play_game = request.args.get("playGame")
    
    if play_game == "yes":
        return render_template("game.html")
        
    else:
        return render_template("goodbye.html")


@app.route("/madlib")
def madlib():
    colors = request.args.get("color")
    nouns = request.args.get("noun")
    persons = request.args.get("person")
    adjectives = request.args.get("adjective")
    return render_template("madlib.html", color = colors, noun = nouns, person = persons, adjective= adjectives)


if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0", port=5003 )
