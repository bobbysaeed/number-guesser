from random import randint


def main():
    number = randint(1, 100)
    point = 100
    while point:
        guess_num = input("Please guess a nuumber from 1 to 100:(or 'q' to exit!) ")
        if guess_num == "q":
            print("Hope to see you soon!")
            break
        try:
            guess_num = int(guess_num)
            hint = "it is bigger" if guess_num < number else "it is smaller"
            if guess_num != number:
                print(hint)
        except ValueError:
            print("please don't enter non integer")
            continue
        if guess_num not in range(1, 101):
            print("please enter a valid integer number")
            continue
        elif guess_num == number:
            print("CONGRATS")
            break
        point -= 10
        print(f"you have {point} points left")
    print(f"the correct number was {number}")


if __name__ == '__main__':
    main()