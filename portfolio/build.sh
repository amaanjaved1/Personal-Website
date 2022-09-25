#!/usr/bin/env bash
set -e # exit on error

python3 manage.py collectstatic --no-input

python3 manage.py migrate --no-input
