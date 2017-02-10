import random


def main():
    with open('numbers.txt', 'w') as file:
        for _ in range(1000000):
            file.write(str(random.randint(1, 100)) + "\r\n")

if __name__ == "__main__":
    main()
