import os
import json
from . import mkdir


def get_config_path():
    user_dir = os.path.expanduser('~')
    program_name = 'connect'
    config_filename = 'config.json'

    config_path = os.path.join(user_dir, program_name, config_filename)

    return config_path


def save_config(config):
    config_path = get_config_path()
    json.dump(config, open(config_path, 'w'))


def init_config():
    config_path = get_config_path()

    config_dirname = os.path.dirname(config_path)
    mkdir(config_dirname)

    connect_name = input('请输入连接名称(拨号连接的名称， 如果没有请创建一个)：')
    username = input('请输入用户名：')
    password = input('请输入密码：')

    config = {
        'connect_name': connect_name,
        'username': username,
        'password': password
    }

    save_config(config)


def load_config():
    config_path = get_config_path()

    config = json.load(open(config_path))

    connect_name = config.get('connect_name', '')
    username = config.get('username', '')
    password = config.get('password', '')

    return (connect_name, username, password)


def update_config(**kwargs):
    config_path = get_config_path()

    config = json.load(open(config_path))
    config.update(kwargs)

    save_config(config)
