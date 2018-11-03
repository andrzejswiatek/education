import random

dobre = 0
zle = 0

def mnozenie():
    global dobre
    global zle
    try:
        while True:
            x = random.randint(5, 9)
            y = random.randint(5, 9)
            print('%d x %d =' % (x, y))
            result = input()
            while x * y != int(result):
                zle = zle + 1
                print('ZLE')
                print('%d x %d =' % (x, y))
                result = input()
            dobre = dobre + 1
            print('OK')
    except KeyboardInterrupt:
        print('Bye')


def dzielenie():
    global dobre
    global zle

    try:
        while True:
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            print('%d : %d =' % (x * y, y))
            result = input()
            while x * y != int(result) * y:
                zle = zle + 1
                print('ZLE')
                print('%d : %d =' % (x * y, y))
                result = input()
            dobre = dobre + 1
            print('OK')
    except KeyboardInterrupt:
        print('Bye')


def main():
    print("Siema Dawson joy ")
    wybor = input("Z czego chcesz byc pytany: 1 - mnozenie, 2 - dzielenie:\r\n")

    print(wybor)

    if wybor == '1':
        print('zioomku wybrales mnozenie')
        mnozenie()
    elif wybor == '2':
        print('zioomku wybrales dzielenie')
        dzielenie()
    else:
        print('Nic nie wybrales')


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print('Dobrych odpowiedzi:', dobre)
        print('Zlych odpowiedzi:', zle)
