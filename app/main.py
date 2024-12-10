import sys

def main():
    i = 1
    while bool(i):
        sys.stdout.write("$ ")
        response = input()
        command = response.split()[0]
        if "exit" in command:
            break
        if "echo" in command:
            print(response[5:])
        else:
            sys.stdout.write(command + ": command not found\n")

    

if __name__ == "__main__":
    main()
