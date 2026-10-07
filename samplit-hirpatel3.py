import sys
import random

def skim(file_name):
    with open(file_name, "r") as file:
        for line in file:
            if random.random() < 0.01:
                sys.stdout.write(line) 

def main():
    sec_input = sys.argv[1]
    skim(sec_input)
    sys.stdout 

if __name__ == "__main__":
    main()