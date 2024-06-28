import pandas as pd
from django.core.management.base import BaseCommand
from leads.models import HomeLead, HomeEmployee
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Load data from Parquet files'

    def handle(self, *args, **kwargs):
        leads_file = 'home_lead.parquet'
        employees_file = 'home_employee.parquet'

        try:
            leads_df = pd.read_parquet(leads_file)
            employees_df = pd.read_parquet(employees_file)

            for _, row in leads_df.iterrows():
                try:
                    lead = HomeLead.objects.create(
                        company_name=row['company_name_linkedin'],
                        number_of_employees=row['n_employees'],
                        raw_json=row['raw_json']
                    )
                    logger.info(f"Successfully saved HomeLead {lead.id}")
                except Exception as e:
                    logger.error(f"Error saving HomeLead: {str(e)}")

            for _, row in employees_df.iterrows():
                try:
                    # Assuming you have a lead_id or urn in employees_df to link to HomeLead
                    lead_id = row['lead_id']  # Adjust this to match your actual column name
                    lead = HomeLead.objects.get(urn=lead_id)  # Adjust to match your actual foreign key
                    employee = HomeEmployee.objects.create(
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        raw_json=row['raw_json'],
                        lead=lead
                    )
                    logger.info(f"Successfully saved HomeEmployee {employee.id}")
                except Exception as e:
                    logger.error(f"Error saving HomeEmployee: {str(e)}")

            self.stdout.write(self.style.SUCCESS('Successfully loaded data from Parquet files.'))

        except Exception as e:
            logger.error(f"Error loading data from Parquet files: {str(e)}")
            self.stdout.write(self.style.ERROR(f'Failed to load data: {str(e)}'))
