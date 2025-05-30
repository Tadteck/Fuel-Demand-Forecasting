from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    MONGO_URI = os.getenv("MONGO_URI")
    SECRET_ADMIN_KEY = os.getenv("SECRET_ADMIN_KEY")