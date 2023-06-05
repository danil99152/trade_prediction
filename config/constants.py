import os
import pathlib


# from dotenv import load_dotenv


class Constants:
    def __init__(self):
        # load_dotenv()
        pass

    __slots__ = []

    @staticmethod
    def get_db_url():
        return f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("DBHOST")}' \
               f':{os.getenv("PORT")}/{os.getenv("TABLE")}'
