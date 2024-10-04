#!/usr/bin/python3
"""Fabric function that generates .tgz from web_static folder"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """TGZ folder compiler and .tgz archiver"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        # files stored in their own new folder too
        files = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(files))
        # returns path/folder name if it doesnt it returns None
        return files
    except BaseException:
        return None
