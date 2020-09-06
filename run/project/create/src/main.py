#!/usr/bin/python3
import os

from formula import formula

project_name = os.environ.get("PROJECT_NAME")
framework = os.environ.get("FRAMEWORK")
run = os.environ.get("RUN")
formula.Run(project_name, framework, run)
