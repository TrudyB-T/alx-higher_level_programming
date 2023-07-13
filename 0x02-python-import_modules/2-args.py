#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)


    if length > 2 :
        print(f"{length - 1} arguments: ")
        for index, arg in enumerate(sys.argv[1:], start=1):
            print(f"{index}: {arg}")

    if length == 2:
        print(f"{length - 1} argument: ")
        for index, arg in enumerate(sys.argv[1:], start=1):
            print(f"{index}: {arg}")

    else:
        print("0 arguments.")
