from commands import hello, version, echo


def run(command: str, *args):

    if command == "hello":
        hello()

    elif command == "version":
        version()

    elif command == "echo":

        if len(args) == 0:
            print("No message provided")
            return

        echo(" ".join(args))

    else:
        print(f"Unknown command: {command}")