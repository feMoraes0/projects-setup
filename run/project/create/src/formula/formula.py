#!/usr/bin/python3
import os

from helpers.message import Message
from helpers.project import Project

def Run(project_name, project_path, framework, wanna_run):
    if(project_path.find('~') != -1):
        project_path = project_path.replace('~', os.path.expanduser('~'))

    os.system(f'cd {project_path}')
    
    message = Message()
    project = Project(project_name, framework, message)
    project.create()