from pydantic import BaseModel, conint, constr, confloat


class Analysis(BaseModel):
    customer_legal_form: conint()
    price: confloat()
    product_code: constr()
    supplier_legal_form: conint()
    time: confloat()
