import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure Database


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect('birthdays.db')
    cursor = conn.cursor()
    if request.method == "POST":

        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        cursor.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", (name, month, day))

        return redirect("/")
    else:
        cursor.execute("SELECT * FROM birthdays")
        rows = cursor.fetchall()
        conn.close()

        return render_template("index.html", rows=rows)


