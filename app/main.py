import sys
import os
import subprocess
from typing import Optional

def locate_executable(command) -> Optional[str]:
    path = os.environ.get("PATH", "")
    for directory in path.split(":"):
        file_path = os.path.join(directory, command)
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path

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
                        if executable := locate_executable(cmd):
                            print(f"{cmd} is {executable}")    
                        else:
                            print(response[5:] + ": not found")
            case _:
                if executable := locate_executable(command):
                    subprocess.run([executable, *args])
                else:
                    print(f"{command}: command not found")

    

if __name__ == "__main__":
    main()
