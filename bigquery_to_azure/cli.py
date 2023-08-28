from typing import Optional, Callable
from transfer_service import TransferService
from config import Config
from logger import Logger

class CLI:
    def __init__(self, transfer_service: TransferService, config: Config, logger: Logger):
        self.transfer_service = transfer_service
        self.config = config
        self.logger = logger

    def run(self) -> None:
        """
        Run the command-line interface.
        """
        # Implementation goes here
