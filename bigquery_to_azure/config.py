## config.py

# BigQuery configuration
BIGQUERY_PROJECT_ID = "your_project_id"
BIGQUERY_DATASET_ID = "your_dataset_id"
BIGQUERY_TABLES = {
    "ga4": "your_ga4_table",
    "search_console": "your_search_console_table",
    "google_ads": "your_google_ads_table"
}

# Azure configuration
AZURE_SERVER = "your_azure_server"
AZURE_DATABASE = "your_azure_database"
AZURE_USERNAME = "your_azure_username"
AZURE_PASSWORD = "your_azure_password"

# API configuration
API_HOST = "your_api_host"
API_PORT = 8000

# Scheduler configuration
SCHEDULE_INTERVAL = "0 0 * * *"
