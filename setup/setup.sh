#!/usr/bin/env bash

cd ../python-server

if ! hash pip 2>/dev/null; then
    sudo easy_install pip
fi

if ! hash virtualenv 2>/dev/null; then
    sudo pip install virtualenv
fi

virtualenv -p python2.7 venv
source venv/bin/activate
pip install -r requirements.txt

echo "To start: source venv/bin/activate && ./server.py"