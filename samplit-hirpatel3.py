import sys
import random

def skim(file_n):
    with open(file_n, "r") as file:
        for line in file:
            if random.random() < 0.01:
                sys.stdout.write(line) 


def main():
    file_n = sys.argv[1]
    skim(file_n)
    sys.stdout 

if __name__ == "__main__":
    main()