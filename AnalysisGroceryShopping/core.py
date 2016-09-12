from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/shopping")
def shopping():
    return render_template('shopping.html')