
number = float(input("first number: "))
number2 = float(input("second number: "))

def add():
    add = lambda number, number2: number + number2
    return print(add(number, number2))

def substract():
    substract = lambda number, number2: number - number2
    return print(substract(number, number2))

def multiply():
    multiply = lambda number, number2: number * number2
    return print(multiply(number, number2))

def divide():
    try:
        divide = lambda number, number2: number / number2
        return print(divide(number, number2))
    except ZeroDivisionError:
        print("cant divide by zero")
        return

def menu():
    while True:
        print("\n---MENU---")
        print("1 - add")
        print("2 - substract")
        print("3 - multiply")
        print("4 - divide")
        print("5 - break")
        
        opcao = input("choose: ")

        if opcao == "1":
            add()
        elif opcao == "2":
            substract()
        elif opcao == "3":
            multiply()
        elif opcao == "4":
            divide()
        elif opcao == "5":
            print("encerrando")
            break
        else:
            print("opção invalida")

menu()