import logging
from typing import List

from service.model import ModelService
from service.schemas.analysis import Analysis


class ModelApi:
    __slots__ = ['model']

    def __init__(self) -> None:
        self.model = ModelService()

    @staticmethod
    def ping() -> str:
        result_bool_obj: str = 'pong'
        return result_bool_obj

    async def analyse(self, data: Analysis) -> str | dict:
        logging.debug(data)
        result = self.model.analyse(data)
        return result

    async def get_history(self, data: dict) -> str:
        logging.debug(data)
        value = int(data.get('inn_supp'))
        result = self.model.get_history(value)
        return result
