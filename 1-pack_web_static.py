#!/usr/bin/python3
'''Module to compress folder into tgz'''
import fabric
import datetime


def do_pack():
    '''Packs a folder into tgz'''
    try:
        fabric.operations.local('mkdir -p versions')
        name = str(datetime.datetime.now())
        name = name.replace("-", "")
        name = name.replace(" ", "")
        name = name[:16]
        name = name.replace(":", "")
        name = "versions/web_static_" + name
        fabric.operations.local("tar -czvf {}.tgz web_static".format(name))
        return name
    except:
        return None
