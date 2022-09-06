import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
from dotenv import load_dotenv

load_dotenv()

# Enable debug mode.
DEBUG = True

# Connect to the database

database_path = os.environ.get('database_path')