import pandas as pd

class BigQuery:
    def __init__(self, project_id, dataset_id):
        self.project_id = project_id
        self.dataset_id = dataset_id

    def extract_data(self, table, columns):
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
