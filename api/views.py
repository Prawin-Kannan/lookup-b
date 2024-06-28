from ninja import NinjaAPI
from .models import HomeLead, HomeEmployee
from ninja.orm import create_schema

api = NinjaAPI()

HomeLeadSchema = create_schema(HomeLead)
HomeEmployeeSchema = create_schema(HomeEmployee)

@api.get("/leads", response=list[HomeLeadSchema])
def list_leads(request, company_name: str = None, number_of_employees: int = None):
    leads = HomeLead.objects.all()
    if company_name:
        leads = leads.filter(company_name__icontains=company_name)
    if number_of_employees:
        leads = leads.filter(number_of_employees=number_of_employees)
    return leads

@api.get("/employees", response=list[HomeEmployeeSchema])
def list_employees(request, first_name: str = None, last_name: str = None, seniority: str = None, role: str = None):
    employees = HomeEmployee.objects.all()
    if first_name:
        employees = employees.filter(first_name__icontains=first_name)
    if last_name:
        employees = employees.filter(last_name__icontains=last_name)
    if seniority:
        employees = employees.filter(seniority__icontains=seniority)
    if role:
        employees = employees.filter(role__icontains=role)
    return employees
