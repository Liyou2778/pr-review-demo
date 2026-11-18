import subprocess


def build(path):
    subprocess.run("make " + path, shell=True)