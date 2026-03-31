import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..','.env')
load_dotenv(dotenv_path)

DATABASE_PATH = os.getenv('DATABASE_PATH', 
os.path.join(os.path.dirname(__file__), '..', 'data', 'database.sqlite')
)
