from app import app
from controllers import create_or_update_pac
from flask import request


@app.route('/pac', methods=["POST"])
def pac():
    return create_or_update_pac(request)
