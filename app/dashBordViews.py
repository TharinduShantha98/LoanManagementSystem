from app import app
from flask import render_template


@app.route("/dashbord")
def dashbord():
    return  render_template("dashbord/dashbord.html")