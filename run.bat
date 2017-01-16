@echo off
set FLASK_APP=wfmastery
set FLASK_DEBUG=1
set DB_PATH=test.sqlite3
set SERVER_NAME="127.0.0.1:5000"
echo "HOSTED@LOCAL:5000"
python -m flask run
