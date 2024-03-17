from datetime import datetime
import os
import sys

# python main.py FOLDER_NAME REPLICA_FOLDER SOURCE_FOLDER FOLDER_NAME_LOG LOG_FILE_NAME TIME
# example : python3 main.py files/ files/source/ files/replica/ logs/ 25

if not len(sys.argv) > 1:
    FOLDER_NAME = 'files/'
    SOURCE_FOLDER = FOLDER_NAME+'source/'
    REPLICA_FOLDER = FOLDER_NAME+'replica/'
    FOLDER_NAME_LOG = 'logs/'  
    OBS_TIMMER = 15 
else:
    FOLDER_NAME = sys.argv[1]
    SOURCE_FOLDER = sys.argv[2]
    REPLICA_FOLDER = sys.argv[3]
    FOLDER_NAME_LOG = sys.argv[4]
    OBS_TIMMER = int(sys.argv[5])

LOG_FILE_NAME='LOG_'+datetime.now().strftime("%Y-%m-%d_%H:%M:%S")+'.log'

if not os.path.exists(SOURCE_FOLDER and REPLICA_FOLDER and FOLDER_NAME_LOG):
    os.makedirs(SOURCE_FOLDER, exist_ok=True)
    os.makedirs(REPLICA_FOLDER, exist_ok=True)
    os.makedirs(FOLDER_NAME_LOG, exist_ok=True)