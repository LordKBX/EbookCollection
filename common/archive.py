import os, sys
import subprocess
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import common.vars


def inflate(src: str, dest: str):
    list_args = list()  # create list argument for external command execution
    list_args.append(common.vars.load_path_archiver() + os.sep + common.vars.env_vars['tools']['archiver'][os.name]['exe'])  # insert executable path
    temp_args = common.vars.env_vars['tools']['archiver'][os.name]['params_inflate'].split(' ')  # create table of raw command arguments
    for var in temp_args:  # parse table of raw command arguments
        # insert parsed param
        list_args.append(var.replace('%input%', src).replace('%output%', dest))
    # print(list_args)
    return subprocess.call(list_args, shell=True)  # execute the command


def deflate(src: str, dest: str):
    list_args = list()  # create list argument for external command execution
    list_args.append(common.vars.load_path_archiver() + os.sep + common.vars.env_vars['tools']['archiver'][os.name]['exe'])  # insert executable path
    temp_args = common.vars.env_vars['tools']['archiver'][os.name]['params_deflate'].split(' ')  # create table of raw command arguments
    for var in temp_args:  # parse table of raw command arguments
        # insert parsed param
        list_args.append(var.replace('%input%', src).replace('%output%', dest))
    print(list_args)
    ret = subprocess.call(list_args, shell=True)  # execute the command
    print(ret)
    return ret
