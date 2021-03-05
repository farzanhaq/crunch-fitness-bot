from dotenv import load_dotenv
from os.path import join, dirname
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
