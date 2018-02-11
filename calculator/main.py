from calculator import *


def main():
    calculator = Calculator()

    calculator.execute()  # implement add 100
    print(calculator.currentValue())  # should show 100
    calculator.execute()  # implement subtract 50
    print(calculator.currentValue())  # should show 50
    calculator.execute()  # implement multiply by 4
    print(calculator.currentValue())  # should show 200
    calculator.execute()  # implement divide by 2
    print(calculator.currentValue())  # should show 100

    calculator.undo()
    calculator.undo()

    print(calculator.currentValue())  # should show 50


if __name__ == "__main__":
    main()
