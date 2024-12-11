import sys
import os
import subprocess
from typing import Optional

def find_in_path(param):
    path = os.environ['PATH']
    print("Path: " + path)
    print(f"Param: {param}")
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
        command, *args = input().split(" ")
        match command:
            case ["exit", "0"]:
                exit(0)
            case ["echo", *cmd]:
                print(" ".join(cmd))
            case ["type", *cmd]:
                match cmd:
                    case ["echo" | "exit" | "type"]:
                        print(f"${cmd[0]} is a shell builtin")
                    case _:
                        if executable := find_in_path(cmd):
                            print(f"{cmd} is {executable}")    
                        else:
                            print(response[5:] + ": not found")
            case _:
                if executable := find_in_path(command):
                    subprocess.run([executable, *args])
                else:
                    print(f"{command}: command not found")

    

if __name__ == "__main__":
    main()
