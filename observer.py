import os
import time
from cloner import FolderCloner
from constant import REPLICA_FOLDER

class FolderObserver:
    def __init__(self, folder_path, logger, obs_timmer):
        self.folder_path = folder_path
        self.last_modification_time = self.get_modification_time()
        self.logger = logger
        self.obs_timmer = obs_timmer

    def get_modification_time(self):
        return os.path.getmtime(self.folder_path)

    def folder_modified(self):
        current_modification_time = self.get_modification_time()
        if current_modification_time != self.last_modification_time:
            self.last_modification_time = current_modification_time
            return True
        return False

    def start_observing(self):
        while True:
            if self.folder_modified():
                self.logger.write_on_log_and_console(f'{__class__.__name__.upper()} - Folder "{self.folder_path}" has been modified.')
                the_cloner = FolderCloner(self.folder_path, REPLICA_FOLDER, self.logger)
                the_cloner.clone()
            time.sleep(self.obs_timmer)