from ninja import NinjaAPI
from .models import HomeLead, HomeEmployee
from .schemas import HomeLeadSchema, HomeEmployeeSchema
from typing import List

api = NinjaAPI()

@api.get('/leads/', response=List[HomeLeadSchema])
def list_leads(request):
    return HomeLead.objects.all()

@api.get('/employees/', response=List[HomeEmployeeSchema])
def list_employees(request):
    return HomeEmployee.objects.all()

@api.get('/leads/{lead_id}', response=HomeLeadSchema)
def get_lead(request, lead_id: int):
    return HomeLead.objects.get(id=lead_id)

@api.get('/employees/{employee_id}', response=HomeEmployeeSchema)
def get_employee(request, employee_id: int):
    return HomeEmployee.objects.get(id=employee_id)

@api.get('/leads/filter/', response=List[HomeLeadSchema])
def filter_leads(request, company_name: str = None, num_employees: int = None):
    leads = HomeLead.objects.all()
    if company_name:
        leads = leads.filter(company_name__icontains=company_name)
    if num_employees:
        leads = leads.filter(number_of_employees=num_employees)
    return leads

@api.get('/employees/search/', response=List[HomeEmployeeSchema])
def search_employees(request, name: str = None, seniority: str = None, role: str = None):
    employees = HomeEmployee.objects.all()
    if name:
        employees = employees.filter(first_name__icontains=name) | employees.filter(last_name__icontains=name)
    if seniority:
        employees = employees.filter(seniority__icontains=seniority)
    if role:
        employees = employees.filter(role__icontains=role)
    return employees
