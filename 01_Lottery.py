import random

def lottery_function(): 
    count = 0
    lottery = []
    while count < 7:
        lucky_numb = random.randint(1,45)
        if lucky_numb not in lottery:
            lottery.append(lucky_numb)
        count += 1
    print("Your Lottery-Numbers:")
    print(lottery)

lottery_function()


