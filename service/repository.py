from sqlalchemy import text
from sqlalchemy.engine import Engine


class EEGRepository:
    __slots__ = ["engine"]

    def __init__(self, engine: Engine):
        self.engine = engine

    def save(self, data: dict):
        self.engine.execute(
            text(
                f"""
                INSERT INTO public.Data(
                    {data.keys()}
                )
                VALUES(
                    {data.keys()}
                )
                """
            ),
            {
                data
            }
        )
