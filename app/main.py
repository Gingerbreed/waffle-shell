import sys


def main():
    i = 1
    while i > 1000:
        sys.stdout.write("$ ")
        command = input()
        sys.stdout.write(command + ": command not found\n")
        i += 1
        
    

if __name__ == "__main__":
    main()
