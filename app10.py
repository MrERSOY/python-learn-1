# command = ""
# while command.lower() != "quit":

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
