#!/usr/bin/python3
"""
This script generates a .tgz archive from the contents of the web_static folder
"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the web_static folder.

    Returns:
        str: Archive path if successfully generated, None otherwise.
    """
    d_t = datetime.utcnow()
    file_archive = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_t.year,
        d_t.month,
        d_t.day,
        d_t.hour,
        d_t.minute,
        d_t.second
    )
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_archive)).failed is True:
        return None
    return file_archive
