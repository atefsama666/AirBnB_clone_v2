#!/usr/bin/python3
'''Module to compress folder into tgz'''
import fabric
from fabric.api import env
import datetime
from os import path


fabric.operations.env.user = 'ubuntu'
fabric.operations.env.hosts = ['35.237.127.243', '54.90.102.32']
env.key_filename = "~/.ssh/holberton"


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
        return name + ".tgz"
    except:
        return None


def do_deploy(archive_path):
    '''Distributes archive to web servers'''
    if not path.exists(archive_path):
        return False
    # Upload archive to tmp
    aRRchive = archive_path.split("/")
    name = aRRchive[1]
    remote_path = "/tmp/" + name
    fail = fabric.operations.put(archive_path, remote_path).failed
    if fail:
        return False
    # Decompress archive into desired path
    #   Creation of extraction folder
    file_no_ex = name.split(".")[0]
    extraction_path = "/data/web_static/releases/" + file_no_ex
    fail = fabric.operations.run("mkdir -p {}".format(extraction_path)).failed
    if fail:
        return False
    #   Decompression
    fail = fabric.operations.run(
        "tar -C {} -zxvf /tmp/{}".format(extraction_path, name)).failed
    if fail:
        return False
    #   Moving files out of web_static
    fail = fabric.operations.run(
        "mv {}/web_static/* {}/".format(
            extraction_path, extraction_path)).failed
    if fail:
        return False
    #   Removing web_static folder
    fail = fabric.operations.run(
        "rm -rf {}/web_static".format(extraction_path)).failed
    if fail:
        return False
    #   Cleaning tmp
    fail = fabric.operations.run("rm /tmp/{}".format(name)).failed
    if fail:
        return False
    #   Refresing sym link
    #       Deleting
    fail = fabric.operations.run("rm /data/web_static/current").failed
    if fail:
        return False
    #       Creating
    cmd = "ln -s {} /data/web_static/current".format(extraction_path)
    fail = fabric.operations.run(cmd).failed
    if fail:
        return False
    return True


def deploy():
    '''Deploys a new web app to servers'''
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
