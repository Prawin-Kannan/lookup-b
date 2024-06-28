import os
import pandas as pd
from django.core.management.base import BaseCommand
from api.models import HomeLead, HomeEmployee

class Command(BaseCommand):
    help = 'Load data from Parquet files into the database'

    def handle(self, *args, **kwargs):
        # Get the path to the lookup_store directory
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        # Load leads
        leads_file_path = os.path.join(base_dir, 'lead.parquet')
        leads_df = pd.read_parquet(leads_file_path)
        for _, row in leads_df.iterrows():
            HomeLead.objects.create(
                company_name=row['company_name'],
                number_of_employees=row['number_of_employees'],
                raw_json=row.to_json()
            )

        # Load employees
        employees_file_path = os.path.join(base_dir, 'employee.parquet')
        employees_df = pd.read_parquet(employees_file_path)
        for _, row in employees_df.iterrows():
            HomeEmployee.objects.create(
                first_name=row['first_name'],
                last_name=row['last_name'],
                seniority=row['seniority'],
                role=row['role'],
                ranking=row['ranking'],
                selected_status=row['selected_status'],
                raw_json=row.to_json()
            )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
