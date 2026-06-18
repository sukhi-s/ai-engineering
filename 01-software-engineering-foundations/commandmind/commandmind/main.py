import sys

from cli import run


def main():

    if len(sys.argv) < 2:
        print("No command provided")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    run(command, *args)


if __name__ == "__main__":
    main()