import random

print(__name__)
def play_game():
    while True:
        play_one()
        play_again = input("還是要繼續玩嗎?(y,n)")
        if play_again == "n":
            break;

def play_one():
    min = 1
    max = 100
    count = 0
    random_value = random.randint(min,max)
    print(random_value)
    print("=============猜數字遊戲=================")

    while True:
        count += 1
        keyin = int(input(f"猜數字的範圍{min}~{max}:"))
        if keyin >= min and keyin <= max :
            if(keyin == random_value):
                print(f"猜對了,答案是:{random_value}")
                print(f"您總共猜{count}次")
                break
            elif keyin > random_value:
                print("再小一點")
                max = keyin - 1
            elif keyin < random_value:
                print("再大一點")
                min = keyin + 1
            print(f"您已經猜了{count}次")
        else:
            print("超出範圍")

    print("遊戲結束")
