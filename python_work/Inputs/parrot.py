prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
# message = ""
active = True  # flag
while active:
    message = input(prompt)
    # if message != "quit":
    #     print(message)
    if message == "quit":
        active = False
    else:
        print(message)
