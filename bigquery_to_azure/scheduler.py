from typing import List
from datetime import datetime
import time

class Scheduler:
    def __init__(self, api):
        self.api = api

    def schedule_transfer(self, table: str, columns: List[str], schedule: str):
        """
        Schedules the data transfer from Google BigQuery to Azure database.

        Args:
            table (str): The name of the table to transfer data from.
            columns (List[str]): The list of columns to transfer.
            schedule (str): The schedule for the data transfer.
        """
        while True:
            current_time = datetime.now().strftime("%H:%M")
            if current_time == schedule:
                self.api.transfer_data(table, columns)
            time.sleep(60)
