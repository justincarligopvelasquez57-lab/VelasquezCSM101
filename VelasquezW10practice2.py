while True:
    word = input("Enter a word: ")
    letter = input("Enter a character to search for: ")

    found = False

    for character in word:
        if character.lower() == letter.lower():
            found = True
            break

        if found:
            print("Character found!!! ")
        else:
            print("Character not found. ")

        again = input("Try Again? (Y/N):  ")

        if again.upper() != "Y":
            break
