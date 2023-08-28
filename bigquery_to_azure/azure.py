import pandas as pd

class Azure:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def load_data(self, data, table):
        """
        Loads data into Azure database.

        Args:
            data (pd.DataFrame): The data to load.
            table (str): The name of the table to load the data into.
        """
        # Implementation goes here
        pass
