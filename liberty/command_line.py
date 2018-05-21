"""Elegant for Internet

Usage:
    connect
    connect init
    connect show
    connect <password>


Options:
    init        Initialize your Internet config.
    show        Show your current Internet config.
    password    If you want to override config's password.

"""
import os
from . import (load_config, update_config, init_config)
from docopt import docopt

command_template = 'rasdial {connect_name} {username} {password}'


def connect(connect_name, username, password):
    command = command_template.format(connect_name=connect_name,
                                      username=username,
                                      password=password)
    result = os.popen(command).read()
    print(result)


def show():
    connect_name, username, password = load_config()
    print('[ current_config ]')
    print('connect_name\t', connect_name)
    print('username\t', username)
    print('password\t', password)


def main():
    arguments = docopt(__doc__, version="liberty 1.0")

    if arguments['init']:
        init_config()
    elif arguments['show']:
        show()
    else:
        connect_name, username, password = load_config()
        if arguments['<password>']:
            password = arguments['<password>']
            update_config(password=password)
        connect(connect_name, username, password)
