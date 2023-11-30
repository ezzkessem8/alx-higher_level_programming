#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    num_args = len(arguments)

    if num_args == 0:
        print(f"{num_args} argument{'.' if num_args == 0 else 's' + ':'}")
    else:
        print(f"{num_args} argument{'.' if num_args == 0 else 's' + ':'}")
        for i in range(num_args):
            print(f"{i + 1}: {arguments[i]}")

