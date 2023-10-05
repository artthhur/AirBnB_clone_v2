#!/usr/bin/python3
"""
This script deletes out-of-date archives.
"""
import os
from fabric.api import *

env.hosts = ["34.232.72.195", "34.229.55.94"]


def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number (int): Number of archives to keep. Default is 0
        (keep only the most recent).

    Returns:
        bool: True if successful, False otherwise.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
