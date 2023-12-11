from flask import Flask
from flask import request
import pyttsx3

app = Flask(__name__)


@app.route("/print")
def print_to_console():
    """Prints "print to console test" to the console and returns "Hello print to console" to the browser."""
    print("print to console test")  # print to console
    return "Hello print to console"  # shows up in browser


@app.route("/tts")
def tts_request(announcement="My face when"):  # default announcement
    """Uses pyttsx3 to say "My face when" and returns
    Hello text-to-speech example to the browser."""
    engine = pyttsx3.init()
    engine.say(announcement)
    engine.runAndWait()
    return "Hello text-to-speech example"


@app.route("/")
def hello():
    """Returns a form to set an alarm."""
    return '<form action="/setalarm" method="get"> \
            <input type="datetime-local" name="alarm"> \
            <input name="two"> \
            <input type="submit"> \
            </form>'


@app.route("/setalarm")
def setalarm():
    alarm = request.args.get("alarm")
    tts_request(alarm)
    return hello()


if __name__ == "__main__":
    app.run()
