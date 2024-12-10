import sys


def main():
    i = 1
    while bool(i):
        sys.stdout.write("$ ")
        command = input()
        if "exit" in command:
            break
        sys.stdout.write(command + ": command not found\n")
       
    else:
        print('hi')
        
    

if __name__ == "__main__":
    main()
