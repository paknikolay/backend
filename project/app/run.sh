#!/usr/bin/bash
sleep 10
export FLASK_APP=app
flask db init
flask db migrate
flask db upgrade
flask run --host=0.0.0.0 --port=5000
