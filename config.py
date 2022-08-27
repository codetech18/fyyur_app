import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.  Must run with "python app.py" for this to be picked up
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Adeniyi7@localhost:5432/fyyur'