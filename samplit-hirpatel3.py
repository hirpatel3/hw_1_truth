import sys
import random

def skim(file_name):
    with open(file_name, "r") as file:
        for line in file:
            if random.random() < 0.01:
                sys.stdout.write(line) 


def main():
    file_name = sys.argv[1]
    skim(file_name)
    sys.stdout 

if __name__ == "__main__":
    main()