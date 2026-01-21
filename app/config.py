from dotenv import load_dotenv
import os 

load_dotenv()

class Config():
    SECRET_KEY=os.getenv('SECRET_KEY')
    DB_PWD=os.getenv('DB_PWD')
    DB_NAME=os.getenv('DB_NAME')
    DB_HOST=os.getenv('DB_HOST')
    DB_USER=os.getenv('DB_USER')
