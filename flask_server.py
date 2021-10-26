# -*- coding: utf-8 -*-

import json
from datetime import datetime, timedelta

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def health():
    return "OK"


@app.route("/ticket", methods=["POST"])
def manage_tickets():
    points = json.loads(request.data).get("story_points")
    expected_dateline = datetime.utcnow() + timedelta(days=points)
    return expected_dateline.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    app.run(port=3001)
