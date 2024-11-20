# Why do we need a template.py?
# we are creating an end-to-end ML project and
# we will be working with a lots of files and 
# folders. If we create these files and folders
# manually it will be a tedious job. If we write
# a python script to do this for us, it will be a
# one time effort and once we execute this 
# template.py later, it will generate the folder
# structure for us

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s: %(message)s:]')

# The logging.basicConfig() function in Python sets up the configuration
# for the logging module.

# logging.basicConfig: configures the root logger
# level = logging.INFO: specifies the log level to capture, means only
#                       messages with a severity level of INFO or higher
#                       will be logged
# Severity levels: DEBUG (10) : detailed debug information
#                  INFO (20) : general operational messages
#                  WARNING (30) : indicates a potential issue
#                  ERROR (40) : error occurred
#                  CRITICAL (50) : a severe error 
# '[%(asctime)s: %(message)s:]': defines the format of log messages
# %(asctime)s: timestamp of when the log messasge is created
# %(message)s: the actual log message

project_name = 'mlProject'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
] 
# this is the folder structure we will need for the project
# This structure aligns with best practices for a Python project, 
# separating concerns like configuration, utilities, entities, and 
# application logic. It supports scalability and maintainability, 
# especially for projects requiring configurations, web interfaces, 
# or Docker deployments.

for filepath in list_of_files: # Each filepath in the list_of_files is processed individually
    filepath = Path(filepath) # Converts the string filepath into a Path object for better path handling (requires the pathlib module).
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else: logging.info(f"{filename} already exists!")