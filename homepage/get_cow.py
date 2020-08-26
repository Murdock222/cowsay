import subprocess


def get_cow(words):
    print("words is ", words)
    cow_command = "cowsay " + str(words)
    cow_object = subprocess.check_output(cow_command, shell=True)
    return cow_object