#!/usr/bin/python3
import sys

# Define the main behavior of your script
def main():
    num_args = len(sys.argv) - 1  
    if num_args == 0:
        print("Number of argument(s): 0.")
    else:
        argument_label = "argument" if num_args == 1 else "arguments"
        print("{} argument:".format(num_args, argument_label))

        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))

# Make sure the script doesn't run when imported
if __name__ == "__main__":
    main()
