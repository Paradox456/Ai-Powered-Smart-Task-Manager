import os

class Config:
    SECRET_KEY = os.getenv('296f4d1a194093f6c9307f1e9e9c0c8fb417e28e03de40c96571ab2703f5e93c', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///tasks.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('5c127a2e7d84a973ba9d94efa5433c4a793d6a2a8144d63470779c0bbafeb3d8', 'superjwtsecretkey')
