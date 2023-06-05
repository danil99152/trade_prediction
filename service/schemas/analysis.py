from pydantic import BaseModel, conint, constr


class Analysis(BaseModel):
    customer_legal_form: conint()
    supplier_legal_form: conint()
    product_code: constr()
