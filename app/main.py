import sys


def main():
    i = 1
    while bool(i):
        sys.stdout.write("$ ")
        command = input()
        sys.stdout.write(command + ": command not found\n")
        if "exit 0" in command:
            i = 0
            print("exit with status code 0")
    else:
        print('hi')
        
    

if __name__ == "__main__":
    main()
