# import logging
# import os
# from datetime import datetime
# import sys

# #LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H')}.log"
# logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# logging.basicConfig(
#     format="[%(asctime)s] - %(name)s - %(levelname)s - %(module)s file - LineNum:%(lineno)d - %(message)s",
#     level=logging.INFO,
#     handlers=[
#         logging.FileHandler(LOG_FILE_PATH),
#         logging.StreamHandler(sys.stdout)
#     ]
# )

# logger=logging.getLogger("Hotel-Reservation-Prediction")

import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
