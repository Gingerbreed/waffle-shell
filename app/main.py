import sys
import os
import subprocess
from typing import Optional

def find_in_path(param):
    path = os.environ['PATH']
    for directory in path.split(":"):
        for (dirpath, dirnames, filenames) in os.walk(directory):
            if param in filenames:
                return f"{dirpath}/{param}"
    return None

def main():
    validcommands = ["echo", "exit", "type"]
    PATH = os.environ.get("PATH")
    while True:
        sys.stdout.write("$ ")
        command = input()
        match command.split(" "):
            case ["exit", "0"]:
                exit(0)
            case ["echo", *cmd]:
                print(" ".join(cmd))
            case ["type", *cmd]:
                match cmd:
                    case ["echo" | "exit" | "type"]:
                        print(f"{cmd[0]} is a shell builtin")
                    case _:
                        location = find_in_path(cmd[0])
                        if location:
                            print(f"{cmd[0]} is {location}")
                        else:
                            print(cmd +": not found")
            case _:
                if os.path.isfile(command.split(" ")[0]):
                    os.system(command)
                else:
                    print(f"{command}: command not found")

    

if __name__ == "__main__":
    main()
