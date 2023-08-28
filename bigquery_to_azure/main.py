import pandas as pd
from typing import List
from datetime import datetime
import time
from config import (
    BIGQUERY_PROJECT_ID,
    BIGQUERY_DATASET_ID,
    AZURE_SERVER,
    AZURE_DATABASE,
    AZURE_USERNAME,
    AZURE_PASSWORD,
    API_HOST,
    API_PORT,
    SCHEDULE_INTERVAL
)
from bigquery import BigQuery
from azure import Azure
from api import API
from scheduler import Scheduler

def main():
    # Initialize BigQuery and Azure instances
    bigquery = BigQuery(BIGQUERY_PROJECT_ID, BIGQUERY_DATASET_ID)
    azure = Azure(AZURE_SERVER, AZURE_DATABASE, AZURE_USERNAME, AZURE_PASSWORD)

    # Initialize API and Scheduler instances
    api = API(bigquery, azure)
    scheduler = Scheduler(api)

    # Schedule the data transfer
    scheduler.schedule_transfer(table="your_table", columns=["column1", "column2"], schedule=SCHEDULE_INTERVAL)

if __name__ == "__main__":
    main()
