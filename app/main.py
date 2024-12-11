import sys
import os

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
                print(f"{response}: command not found")
        # # if command in validcommands:
        # if "exit" in command:
        #     break
        # if "echo" in command:
        #     print(response[5:])
        #     continue
        # if "type" in command:
        #     cmd = response.split(" ")[1]
        #     cmd_path = None
        #     paths = PATH.split(":")
        #     for path in paths:
        #         if os.path.isfile(f"{path}/{cmd} "):
        #             cmd_path = f"{path}/{cmd}"
        #     if response[5:] in validcommands:
        #         print(response[5:] + " is a shell builtin")
        #     elif cmd_path:
        #         print(f"{cmd} is {cmd_path}") 
        #     else:
        #         print(response[5:] + ": not found")
        #     continue
        # else:
        #     if os.path.isfile(command):
        #         os.system(response)
        #     print(command + ": command not found")

    

if __name__ == "__main__":
    main()
