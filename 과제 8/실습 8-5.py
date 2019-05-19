def more(message):
    answer = input(message)
    while not (answer == "n" or answer == "y"):
        answer = input(message)
        continue
    if (answer == "y"):
        return True
    elif(answer == "n"):
        return False
