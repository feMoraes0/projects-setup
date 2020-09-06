#!/usr/bin/python3
import os

from formula import formula

project_name = os.environ.get("PROJECT_NAME")
project_path = os.environ.get("PROJECT_PATH")
framework = os.environ.get("FRAMEWORK")
run = os.environ.get("RUN")
formula.Run(project_name, project_path, framework, run)
