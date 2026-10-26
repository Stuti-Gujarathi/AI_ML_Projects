"""Command-line interface for the AIML chatbot."""
from bot import create_bot, reply


def main():
    kernel = create_bot()
    print("AIMLBot ready. Type 'quit' to exit.\n")
    while True:
        try:
            user = input("You  : ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot  : Goodbye!")
            break
        if user.lower() in {"quit", "exit"}:
            print("Bot  : Goodbye!")
            break
        if user:
            print("Bot  :", reply(kernel, user))


if __name__ == "__main__":
    main()
