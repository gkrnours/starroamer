#!/usr/bin/env python

from flask import Flask
from utils import templated
app = Flask(__name__)

@app.route('/', endpoint="index")
@templated()
def hello():
    print("ping")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
