from transfer_service import TransferService
from config import Config
from logger import Logger
from cli import CLI

def main():
    # Initialize Config
    config = Config("config.json")

    # Initialize Logger
    logger = Logger("log.txt")

    # Initialize TransferService
    source_project_id = config.get("source_project_id")
    source_dataset_id = config.get("source_dataset_id")
    destination_connection_string = config.get("destination_connection_string")
    transfer_service = TransferService(source_project_id, source_dataset_id, destination_connection_string)

    # Initialize CLI
    cli = CLI(transfer_service, config, logger)

    # Run CLI
    cli.run()

if __name__ == "__main__":
    main()
