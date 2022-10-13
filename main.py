from os import system, name


clear = lambda: system("clear") if name == "posix" else system("cls")


def list_to_string(li):
    string = ""
    for i in li:
        string += i

    return string


def replace_char(str, index, replacement):
    str = list(str)
    str[index] = replacement

    return list_to_string(str)


def main():
    word = str(input("Enter the word which should be guessed: ")).lower().replace(" ", "")
    hidden = ""
    for _ in range(len(word)):
        hidden += "_"
    solution = hidden
    message = ""    
    wrong_chars = []

    clear()
    while True:
        print(message, wrong_chars)
        print(f"{solution} length: {len(solution)}")
        guess = str(input("Enter character: ")).lower()

        if guess in word:
            index = word.find(guess)
            word = replace_char(word, index, "0")
            hidden = list(hidden)
            
            hidden[index] = guess
            solution = list_to_string(hidden)
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
