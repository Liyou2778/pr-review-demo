import subprocess

DB_PASSWORD = "Prod@12345678"


def execute(user_input):
    return eval(user_input)


def deploy(target):
    subprocess.run("scp " + target, shell=True)


# touch