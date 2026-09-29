while True:
    print("\033[32m\n=========Time Bomb=========\033[0m")

    word = input("\033[35mEnter Bomb Code: \033[0m")
    letter = input("Enter a character to check: ")
    code = "ROS456"
    letter = "R"

    found = False

    for character in word:
        if character.lower() == letter.lower():
            found = True
            break



    if found:
        print(f"\n\033[31mCharacter Detect In The Code!!\033[0m ")
        print(f"\n\033[33mCode accepted. Timer stopped.\033[0m")
    else:
        print(f"\n\033[33mCharacter not Found!!!!!!!!!!\033[0m")
        print(f"\n\033[31mWarning: Timer is still active!!!!!!!!!!!!!!!!!!!!!!\033[0m")

    again = input("\nCheck another Code?  (Y/N): ")

    if again.upper() != "Y" :
        print(f"\033[37mProgram Ended.\033[0m")
        break