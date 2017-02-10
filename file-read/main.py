import os
import psutil


def main():
    process = psutil.Process(os.getpid())
    print("Memory before reading")
    print(process.memory_full_info().uss / float(2 ** 20))
    print("----")

    numbers = getNumbers()

    print("Numbers count: " + str(len(numbers)))
    print("Memory after reading")
    print(process.memory_full_info().uss / float(2 ** 20))
    print("----")

    del numbers
    print("Memory after removing result")
    print(process.memory_full_info().uss / float(2 ** 20))


def getNumbers():
    with open('numbers.txt') as f:
        return f.readlines()

if __name__ == "__main__":
    main()
