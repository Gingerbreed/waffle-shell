import sys
import os
import subprocess

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
        response = input()
        match response.split(" "):
            case ["exit", "0"]:
                exit(0)
            case ["echo", *cmd]:
                print(" ".join(cmd))
            case ["type", *cmd]:
                match cmd:
                    case ["echo" | "exit" | "type"]:
                        print(f"${cmd[0]} is a shell builtin")
                    case _:
                        cmd = response.split(" ")[1]
                        cmd_path = None
                        paths = PATH.split(":")
                        for path in paths:
                            if os.path.isfile(f"{path}/{cmd} "):
                                cmd_path = f"{path}/{cmd}"
                        if cmd_path:
                            print(f"{cmd} is {cmd_path}")    
                        else:
                            print(response[5:] + ": not found")
            case _:
                if os.path.isfile(command):
                    subprocess.run([command, response.split(" ")[1]])
                print(f"{response}: command not found")

    

if __name__ == "__main__":
    main()
