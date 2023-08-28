from typing import List
import pandas as pd

class BigQuery:
    def __init__(self, project_id: str, dataset_id: str):
        self.project_id = project_id
        self.dataset_id = dataset_id

    def extract_data(self, table: str, columns: List[str]) -> pd.DataFrame:
        """
        Extracts data from Google BigQuery.

        Args:
            table (str): The name of the table to extract data from.
            columns (List[str]): The list of columns to extract.

        Returns:
            pd.DataFrame: The extracted data as a pandas DataFrame.
        """
        # Implementation goes here
        pass


class Azure:
    def __init__(self, server: str, database: str, username: str, password: str):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def load_data(self, data: pd.DataFrame, table: str):
        """
        Loads data into Azure database.

        Args:
            data (pd.DataFrame): The data to load.
            table (str): The name of the table to load the data into.
        """
        # Implementation goes here
        pass


class API:
    def __init__(self, bigquery: BigQuery, azure: Azure):
        self.bigquery = bigquery
        self.azure = azure

    def get_table_list(self) -> List[str]:
        """
        Returns a list of table names in Google BigQuery.

        Returns:
            List[str]: The list of table names.
        """
        # Implementation goes here
        pass

    def get_column_list(self, table: str) -> List[str]:
        """
        Returns a list of column names for a given table in Google BigQuery.

        Args:
            table (str): The name of the table.

        Returns:
            List[str]: The list of column names.
        """
        # Implementation goes here
        pass

    def transfer_data(self, table: str, columns: List[str], schedule: str):
        """
        Transfers data from Google BigQuery to Azure database.

        Args:
            table (str): The name of the table to transfer data from.
            columns (List[str]): The list of columns to transfer.
            schedule (str): The schedule for the data transfer.
        """
        # Implementation goes here
        pass


class Scheduler:
    def __init__(self, api: API):
        self.api = api

    def schedule_transfer(self, table: str, columns: List[str], schedule: str):
        """
        Schedules the data transfer from Google BigQuery to Azure database.

        Args:
            table (str): The name of the table to transfer data from.
            columns (List[str]): The list of columns to transfer.
            schedule (str): The schedule for the data transfer.
        """
        # Implementation goes here
        pass
