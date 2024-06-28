import pandas as pd

# Update these paths according to your setup
leads_file_path = r'lookup_store\api\home_employee.parquet'
employees_file_path = r'lookup_store\api\home_lead.parquet'

# Load and inspect the data
leads_df = pd.read_parquet(leads_file_path)
print("Leads Columns:", leads_df.columns)
print(leads_df.head())

employees_df = pd.read_parquet(employees_file_path)
print("Employees Columns:", employees_df.columns)
print(employees_df.head())
