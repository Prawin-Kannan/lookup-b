import pandas as pd
import json
import numpy as np
from django.core.management.base import BaseCommand
from api.models import HomeLead, HomeEmployee
import os

class Command(BaseCommand):
    help = 'Load data from Parquet files into the database'

    def handle(self, *args, **options):
        # Use absolute paths
        base_dir = os.path.dirname(os.path.abspath(__file__))
        leads_file_path = os.path.join(base_dir, 'home_employee.parquet')
        employees_file_path = os.path.join(base_dir, 'home_lead.parquet')

        # Check if files exist
        if not os.path.exists(leads_file_path):
            self.stdout.write(self.style.ERROR(f"Leads file not found: {leads_file_path}"))
            return
        if not os.path.exists(employees_file_path):
            self.stdout.write(self.style.ERROR(f"Employees file not found: {employees_file_path}"))
            return

        # Load data from Parquet files
        leads_df = pd.read_parquet(leads_file_path)
        employees_df = pd.read_parquet(employees_file_path)

        # Convert ndarray columns to JSON-serializable format
        leads_df['raw_json'] = leads_df['raw_json'].apply(lambda x: x.tolist() if isinstance(x, np.ndarray) else x)
        employees_df['raw_json'] = employees_df['raw_json'].apply(lambda x: x.tolist() if isinstance(x, np.ndarray) else x)

        # Load leads data into the HomeLead model
        for index, row in leads_df.iterrows():
            # Convert raw_json to JSON string if it's not already a string
            if not isinstance(row['raw_json'], str):
                row['raw_json'] = json.dumps(row['raw_json'])
                
            HomeLead.objects.create(
                created_at=row['created_at'],
                updated_at=row['updated_at'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                raw_json=row['raw_json'],  # Already converted to JSON string
                urn=row['urn'],
                lead_id=row['lead_id'],
            )

        # Load employees data into the HomeEmployee model
        for index, row in employees_df.iterrows():
            # Convert raw_json to JSON string if it's not already a string
            if not isinstance(row['raw_json'], str):
                row['raw_json'] = json.dumps(row['raw_json'])

            HomeEmployee.objects.create(
                created_at=row['created_at'],
                updated_at=row['updated_at'],
                linkedin_url=row['linkedin_url'],
                is_demo_lead=row['is_demo_lead'],
                description=row['description'],
                n_employees=row['n_employees'],
                raw_json=row['raw_json'],  # Already converted to JSON string
                company_name_linkedin=row['company_name_linkedin'],
                url=row['url'],
                urn=row['urn'],
                campaign_id=row['campaign_id'],
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from Parquet files'))
