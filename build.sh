#!/bin/bash

#Build the project

echo "Building the project..."
python3.9.13 manage.py makemigrations --noinput
pytho3.9.13 manage.py migrate --noinput



echo "Collect Static..."
python3.9.13 manage.py collectstatic --noinput --clear
