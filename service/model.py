import logging

import pandas as pd
from catboost import CatBoostClassifier

from service.schemas.analysis import Analysis
from settings import settings


class ModelService:
    __slots__ = ['model', 'repository']

    def __init__(self, path=settings.MODEL_PATH):
        # self.repository = EEGRepository(DatabaseConfiguration.get_engine())
        self.model = CatBoostClassifier()
        self.model.load_model(path)

    def analyse(self, data: Analysis) -> str | dict:
        logging.debug(data)
        try:
            values = list(data.dict().values())
            cat_var = settings.cat_columns
            values = pd.DataFrame([values], columns=list(data.dict().keys()))
            values[cat_var] = values[cat_var].astype("str").astype('category')
            pred = self.model.predict_proba(values)[0][1]
            # self.repository.save(data)
            return f'{int(pred * 100)}%'
        except Exception as e:
            return {"result": f'Exception as {e}'}
