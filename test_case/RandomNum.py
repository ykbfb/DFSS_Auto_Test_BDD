import random

def getRadom():
    # num = [random.randint(1000000, 9999999) for _ in range(1)]
    num = random.randint(0, 15)
    print(num)

def guess():
    num = 30
    num1 = int(input('pleae enter num1: '))
    running = True

    while running:
        if int(num) != num1:
            num1 = input('pleae enter num1 again: ')

        else:
            print('you are clever, you are right: num = ',num + 'num1 = ',num1)



if __name__ == '__main__':
    getRadom()
    # guess()