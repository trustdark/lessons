import random

def game():
    rand_num = random.randint(1,10)
    print(rand_num)
    while True:
        user_num = int(input("Type a number between 1 and 10: "))
        if user_num == rand_num:
            print(" You are winner!")
            break
        else :
            print(rand_num)
            user_num

game()
