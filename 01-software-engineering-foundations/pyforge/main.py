from pyforge import AIClient
from pyforge.models import ChatRequest


def main():

    client = AIClient()

    request = ChatRequest(
        model="demo-model",
        prompt="Hello PyForge"
    )

    response = client.chat(request)

    print(response)


if __name__ == "__main__":
    main()