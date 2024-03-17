from datetime import datetime
import os
import shutil


class FolderCloner:
    def __init__(self, source_folder, destination_folder, logger):
        self.source_folder = source_folder
        self.destination_folder = destination_folder
        self.logger = logger

    def clone(self):
        if not os.path.exists(self.source_folder):
            self.logger.write_on_log_and_console(f" - {__class__.__name__} - Source folder '{self.source_folder}' does not exist.")
            return
        if os.path.exists(self.destination_folder):
            shutil.rmtree(self.destination_folder)
        try:
            shutil.copytree(self.source_folder, self.destination_folder)
            self.logger.write_on_log_and_console(f"{__class__.__name__.upper()} - Folder '{self.source_folder}' successfully cloned to '{self.destination_folder}'.")
        except Exception as e:
            self.logger.write_on_log_and_console(f"{__class__.__name__.upper()} - Error occurred: {e}")