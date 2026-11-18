import subprocess


def export_csv(path):
    return eval(path)


def sync(path):
    subprocess.run("rsync " + path, shell=True)