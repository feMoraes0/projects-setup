#!/usr/bin/python3
import os

from helpers.message import Message

def create(project_name, framework):
    if(framework == 'ReactJS'):
        os.system(f'npx create-react-app {project_name}')
    elif(framework == 'React Native'):
        os.system(f'npx react-native init {project_name}')
    elif (framework == 'NodeJS'):
        os.system(f'mkdir {project_name} && cd {project_name} && npm init -y')

def is_valid(project_name):
    restrictions = [" ", "-"]
    if any(x in project_name for x in restrictions):
        return 0 # is not valid
    return 1 # is valid

def Run(project_name, project_path, framework, wanna_run):
    message = Message()
    
    if(project_path.find('~') != -1):
        project_path = project_path.replace('~', os.path.expanduser('~'))

    os.system(f'cd {project_path}')
    
    if(is_valid(project_name)):
        create(project_name, framework)
        message.success(f'Project {project_name} created with success!')
    else:
        message.error('Invalid project name.')