#!/usr/bin/python3
""" deploy """
from fabric.api import *


env.hosts = ["3.85.168.142", "54.236.231.114"]
env.user = "ubuntu"


def do_clean(number=0):
    """ clean """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
