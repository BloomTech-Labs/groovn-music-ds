"""
Data science Flask API endpoint.
"""

from flask import Flask, jsonify
import os
import random
import numpy as np
import psycopg2 as pg

# EB looks for an 'application' callable by default.
app = Flask(__name__)

@app.route("/")
def test():
    """
    A test function
    """
    return "Groovn Music API active!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")