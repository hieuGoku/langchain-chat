"""Config server."""

import os
from dotenv import load_dotenv


load_dotenv()


APP_HOST = os.getenv("APP_HOST")
APP_PORT = os.getenv("APP_PORT")

