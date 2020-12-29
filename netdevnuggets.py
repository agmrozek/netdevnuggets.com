#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
     #return "You are calling me from "+ request.remote_addr
     return render_template("index.html")

if __name__ == "__main__":
     sample.run(port=8888, host="0.0.0.0")
