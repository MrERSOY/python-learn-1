def greet(name):
    print(f"Selam {name}")


def get_greeting(name):
    return f"Selam {name}"


message = get_greeting("Ali")
file = open("greeting.txt", "w")
file.write(message)
