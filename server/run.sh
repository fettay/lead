#/bin/bash

FLASK_APP=server.py \
FLASK_ENV=production \
FLASK_DEBUG=0 \
SQLALCHEMY_TRACK_MODIFICATIONS=False \
flask run --host 0.0.0.0 --port 9090