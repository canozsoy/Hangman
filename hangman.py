import random
import string


def pickWord():
    # random.seed(0)
    fileName = "sowpods.txt"
    f = open(fileName, "r")
    txt = f.read()
    f.close()
    txt.strip()
    splitText = txt.splitlines()
    myWord = random.choice(splitText)
    print("My word is " + myWord + "!")
    return myWord


def printHang(n):
    gal = [["---- "],
           ["|  | "],
           ["|    "],
           ["|    "],
           ["|    "]]
    if n < 6:
        gal[2] = ["|  o "]
    if n < 5:
        gal[3] = ["| /  "]
    if n < 4:
        gal[3] = ["| / \\"]
    if n < 3:
        gal[3] = ["| /|\\"]
    if n < 2:
        gal[4] = ["| /  "]
    if n < 1:
        gal[4] = ["| / \\"]
    for i in gal:
        print(''.join(i))


def main():
    myWord = pickWord()
    length = myWord.__len__()
    print("Welcome to Hangman!")
    myList = "_" * length
    print(myList)
    myList = list(myList)
    counter = 0
    result = 0
    guessList = []
    letters = string.ascii_uppercase

    while counter < 6 and result != 1:
        playerInp = input("Guess your letter: ")
        playerInp = playerInp.upper()

        if playerInp not in letters:
            print("Please enter a letter!")
            continue

        if playerInp in guessList:
            print("You previously guessed this letter!")
            continue

        guessList.append(playerInp)

        if playerInp not in myWord:
            txt = "Incorrect, you have {} more guesses!"
            guessNumber = 6 - counter - 1
            print(txt.format(guessNumber))
            printHang(guessNumber)
            counter += 1
            if counter == 6:
                print("Sorry! You have lost the game, the word is " + myWord + ".")
        else:
            for i in range(length):
                if playerInp == myWord[i]:
                    myList[i] = playerInp

            print("".join(myList))

        if "_" not in myList:
            result = 1
            print("Congratulations, you guessed it correctly!")


if __name__ == '__main__':
    answer = "y"
    while answer == "y":
        main()
        answer = input("Do you want to play again (y/n)? ")
        answer = answer.strip().lower()
        print("\n")
