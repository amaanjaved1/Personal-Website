#!/usr/bin/env bash
set -e # exit on error

pip3 install -r requirements.txt

python3 manage.py collectstatic --no-input

python3 manage.py migrate --no-input