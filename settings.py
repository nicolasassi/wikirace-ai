import dotenv
import os

dotenv.load_dotenv('.env')

DATA_PATH = os.getenv("DATA_PATH", '')
