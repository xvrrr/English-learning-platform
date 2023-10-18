import random
import store_ZHANG

words = ['apple', 'banana', 'orange', 'cherry', 'pear', 'peach', 'abandon', 'aboard', 'absolutely', 'absorb',
             'excuse', 'execute']



def jumble(word):
    random_word = random.sample(word, len(word))
    jumble = ''.join(random_word)

    return jumble


def thank(n1p, n2p, p1, p2):
    print(n1p, 'your score is:', p1)
    print(n2p, 'your score is:', p2)
    check_win(n1p, n2p, p1, p2)
    print("thanks for your participation")


def check_win(n1player, n2player, grade1, grade2):
    if grade1 > grade2:
        print("winner is:", n1player)
    else:
        print("winner is:", n2player)


def play():
    n1pname = input("player 1, Please enter your name :")
    n2pname = input("Player 2 , Please enter your name: ")
    store_ZHANG.login(n1pname)
    store_ZHANG.login(n2pname)
    p1grade = 0
    p2grade = 0

    matches = 0
    while True:
        picked_word = random.choice(words)
        choice = jumble(picked_word)
        print("jumbled word is:", choice)
        if matches % 2 == 0:
            print("Your Turn.", n1pname)
            answer = input("Enter the result is: ")

            if answer == picked_word:
                p1grade += 1

                print('Your score is :', p1grade)
                matches += 1

            else:
                print("Wrong,sorry")

                print("Your turn.", n2pname)

                answer = input("Enter the result is:")

                if answer == picked_word:
                    p2grade += 1

                    print("Your Score is :", p2grade)
                else:
                    print("Wrong,sorry")
                    print("The correct answer is:", picked_word)
                tocontinue = input("press Y to continue and N to quit :")
                if tocontinue == "N":
                    thank(n1pname, n2pname, p1grade, p2grade)
                    break
        else:
            print("Your turn.", n2pname)
            answer = input("Enter the result is: ")
            if answer == picked_word:
                p2grade += 1

                print('Your score is :', p2grade)
                matches += 1

            else:
                print("Wrong,sorry")

                print("Your turn.", n1pname)

                answer = input("Enter the result is:")

                if answer == picked_word:
                    p1grade += 1

                    print("Your Score is :", p1grade)
                else:
                    print("Wrong,sorry")
                    print("The correct answer is:", picked_word)
                    tocontinue = input("press Y to continue and N to quit :")
                    if tocontinue == "N":
                        thank(n1pname, n2pname, p1grade, p2grade)
                        break
        tocontinue = input("press Y to continue and N to quit :")
        if tocontinue == "N":
            thank(n1pname, n2pname, p1grade, p2grade)
            break





