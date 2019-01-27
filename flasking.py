from flask import Flask, render_template
import datetime

app  = Flask(__name__)

@app.route("/<string:name>")
def hello(name):
    now = datetime.datetime.now()
    is_new_years = now.month == 1 and now.day == 1
    return render_template("index,html", is_new_years=is_new_years)
