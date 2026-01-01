# Voice Assistant - Beginner Version
# Oasis Infobyte Python Programming Internship

import datetime

print("=== Simple Voice Assistant ===")
print("Available commands: hello, time, date, exit")

while True:
    command = input("\nYou: ").lower()

    if command == "hello":
        print("Assistant: Hello! How can I help you?")

    elif command == "time":
        print("Assistant: Current time is",
              datetime.datetime.now().strftime("%H:%M:%S"))

    elif command == "date":
        print("Assistant: Today's date is",
              datetime.datetime.now().strftime("%d %B %Y"))

    elif command == "exit":
        print("Assistant: Goodbye!")
        break

    else:
        print("Assistant: Sorry, I didn't understand that.")
