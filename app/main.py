import sys

def main():
    validcommands = ["echo", "exit", "type"]
    i = 1
    while bool(i):
        sys.stdout.write("$ ")
        response = input()
        command = response.split()[0]
        if command in validcommands:
            if "exit" in command:
                break
            if "echo" in command:
                print(response[5:])
            if "type" in command:
                if response[5:] in validcommands:
                    print(response[5:] + " is a shell builtin\n")   
                else:
                    print(response[5:] + ": command not found\n")

        else:
            sys.stdout.write(command + ": command not found\n")

    

if __name__ == "__main__":
    main()
