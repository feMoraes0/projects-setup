#!/usr/bin/python3
from colored import fg, attr
import os

def success(message):
    print("%s ✔ {}%s".format(message) % (fg(3), attr(0)))

def error(message):
    print("%s ✘ {}%s".format(message) % (fg(2), attr(0)))

def create(project_name, framework):
    if(framework == 'React'):
        os.system(f'npx create-react-app {project_name}')
    elif(framework == 'React Native'):
        os.system(f'npx react-native init {project_name}')
    elif (framework == 'NodeJS'):
        os.system(f'mkdir {project_name} && cd {project_name} && npm init -y')

def is_valid(project_name):
    if(project_name.find(" ") != -1):
        return 0 # is not valid
    return 1 # is valid

def Run(project_name, framework, wanna_run):
    if(is_valid(project_name)):
        create(project_name, framework)
        success(f'Project {project_name} created with success!')
    else:
        error('Invalid project name - white spaces are not allowed!')
