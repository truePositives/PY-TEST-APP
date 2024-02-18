import os 
from pathlib import Path
import logging

#1. setup - logger
logging.basicConfig(level=logging.INFO, format="[%(asctime)s%]:%(message)s%")

#.2 setup - project neme
project_name = "py-test-app"

#3. setup - list of initial files & folders
list_of_files = [
    'src/test/features/',
    'src/test/pages/__init__.py',
    'src/test/steps/__init__.py',
    'src/test/utils/__init__.py',
    'src/test/results/__init__.py',
    'src/test/hooks/__init__.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py'
]

#4. loop through the list of files and create if not present or empty
for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"creationg directory: {file_dir}")

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w") as f:
            pass
            logging.info(f"creating empyt file: {file_name}")
    else:
        logging.info(f"{file_name} already exists")



