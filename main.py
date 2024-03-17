from constant import *
from observer import FolderObserver
from logger import TheLogger

# python main.py FOLDER_NAME REPLICA_FOLDER SOURCE_FOLDER FOLDER_NAME_LOG LOG_FILE_NAME TIME
# example : python3 main.py files/ files/source/ files/replica/ logs/ 25

if __name__ == '__main__': 
    THE_LOGGER = TheLogger(LOG_FILE_NAME, FOLDER_NAME_LOG)
    observer = FolderObserver(SOURCE_FOLDER, THE_LOGGER, OBS_TIMMER)
    THE_LOGGER.write_on_log_and_console(f'FOLDERSSYNCHRONIZATION  - Script is running.')
    observer.start_observing()
    