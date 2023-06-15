import logging

import pandas as pd
from catboost import CatBoostClassifier

from service.schemas.analysis import Analysis
from settings import settings


class ModelService:
    __slots__ = ['model', 'repository', 'data']

    def __init__(self, path=settings.MODEL_PATH):
        # self.repository = EEGRepository(DatabaseConfiguration.get_engine())
        self.model = CatBoostClassifier()
        self.model.load_model(path)

        self.data = pd.read_csv(settings.contract_path,
                                dtype={'product_code': 'category',
                                       'customer_legal_form': 'category',
                                       'supplier_legal_form': 'category',
                                       'current_contract_stage': 'category'},
                                parse_dates=['execution_period_start'])
        self.data['execution_period_start'] = pd.to_datetime(self.data['execution_period_start'],
                                                             format="%Y-%m-%d",
                                                             errors='coerce')
        self.data['execution_period_end'] = pd.to_datetime(self.data['execution_period_end'],
                                                           format="%Y-%m-%d",
                                                           errors='coerce')

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

    def get_history(self, value: int) -> str:
        supp = self.data[(self.data['supplier_inn'] == value)]
        ec = len(supp[(supp['current_contract_stage'] == 'EC')])
        et = len(supp[(supp['current_contract_stage'] == 'ET')])
        return f'Хорошо проведенные: {ec} ' \
               f'Плохо проведенные: {et}'


    # def get_history(self, value: int) -> str:
    #     try:
    #         statement = select(supplier).where(supplier.c.inn == value)
    #         with self.engine.connect() as conn:
    #             result = conn.execute(statement).fetchall()
    #             conn.commit()
    #         response = pd.DataFrame([], columns=list(*Supplier.__annotations__))
    #         for res in result:
    #             d = {}
    #             for key, value in zip(Supplier.__annotations__, res):
    #                 d[key] = value
    #             response = pd.concat([response, pd.DataFrame(data=d)], ignore_index=True)
    #
    #         ec = len(response[(response['current_contract_stage'] == 'EC')])
    #         et = len(response[(response['current_contract_stage'] == 'ET')])
    #         return f'Хорошо проведенные: {ec} ' \
    #                f'Плохо проведенные: {et}'
    #     except Exception as e:
    #         return f"exception at get_history: {e}"