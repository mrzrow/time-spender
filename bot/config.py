import os

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.environ.get('TOKEN')
API_URL = os.environ.get('API_URL')
IMG_PATH = os.environ.get('IMG_PATH')
