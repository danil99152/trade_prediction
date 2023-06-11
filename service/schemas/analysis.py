from pydantic import BaseModel, conint, constr, confloat


class Analysis(BaseModel):
    customer_legal_form: conint()
    supplier_legal_form: conint()
    product_code: constr()
    time: conint()
    price: confloat()
