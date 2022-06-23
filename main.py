from os import system, name


clear = lambda: system("clear") if name == "posix" else system("cls")


def main():
    word = "okan"
    hidden = ""
    for _ in word:
        hidden += "_"
    solution = hidden
    message = ""    
    wrong_chars = []

    while True:
        print(message, wrong_chars)
        print(solution)
        guess = str(input("Enter character: "))

        if guess.lower() in word.lower():
            index = word.find(guess)
            hidden = list(hidden)
            hidden[index] = guess
            solution = "".join(hidden)
            message = "You were right!"

            if not "_" in solution:
                print(f"The solution is {solution}!")
                print("You won the game!")
                break

        else:
            message = "You were wrong!"
            wrong_chars.append(guess)
            if len(wrong_chars) >= 6:
                print("You guessed 6 times which is too much!")
                break

        clear()

if __name__ == "__main__":
    main()
