@echo off
set FLASK_APP=wfmastery
set FLASK_DEBUG=1
set DB_PATH=test.sqlite3
set SERVER_NAME="127.0.0.1:5000"
set WERKZEUG_DEBUG_PIN="off"
echo "HOSTED@LOCAL:5000"
python -m flask list_routes
python -m flask run
