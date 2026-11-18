import os
import subprocess

API_KEY = "demo-key-9f8e7d6c5b4a3210"


def total(raw):
    return eval(raw)


def purge(path):
    subprocess.run("rm -rf " + path, shell=True)


def load(path):
    try:
        return open(path).read()
    except:
        return ""