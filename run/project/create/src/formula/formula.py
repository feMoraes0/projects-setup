#!/usr/bin/python3
from colored import fg, attr


def is_valid(project_name):
    if(project_name.find(" ") != -1):
        return 0 # is not valid
    return 1 # is valid

def Run(project_name, framework, wanna_run):
    if(is_valid(project_name)):
        print('is valid')
    else:
        print('is not valid')
