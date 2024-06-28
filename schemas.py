from ninja import Schema

class HomeLeadSchema(Schema):
    id: int
    company_name: str
    number_of_employees: int
    raw_json: dict

class HomeEmployeeSchema(Schema):
    id: int
    first_name: str
    last_name: str
    seniority: str
    role: str
    company_id: int
    raw_json: dict
