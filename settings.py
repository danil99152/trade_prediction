import pathlib

from pydantic import BaseSettings, conint, constr
from pydantic.validators import IPv4Address


class Settings(BaseSettings):
    DEBUG: bool = True

    APP_TITLE: constr(min_length=1, max_length=255) = 'CKD_API'
    APP_VERSION: constr(min_length=1, max_length=15) = '1'
    APP_HOST: constr(min_length=1, max_length=15) = str(IPv4Address('127.0.0.1' if DEBUG else '0.0.0.0'))
    APP_PORT: conint(ge=0) = 5000
    APP_PATH: constr(min_length=1, max_length=255) = str(pathlib.Path(__file__).parent.resolve())

    # MODEL_REQUEST_QUEUE: constr(min_length=1, max_length=255) = 'MODEL_REQUEST_QUEUE'
    MODEL_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/resources/catboost"

    cat_columns: dict = {
        'customer_legal_form': "Номер заказчика",
        'supplier_legal_form': "Номер поставщика",
        'product_code': "Номер продукта"
    }


settings = Settings()
