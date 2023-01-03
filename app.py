def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))


def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))


print("A. ADDITION")
print("B. SUBTRACTION")
print("C. MULTIPLICATION")
print("D. DIVISION")
print("E. exit")

choice = input("Input your choice: ")

if choice == "a" or choice == "A":
    print("ADDITION")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    add(a, b)
elif choice == "b" or choice == "B":
    print("SUBTRACTION")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    sub(a, b)
elif choice == "c" or choice == "C":
    print("SUBTRACTION")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    mul(a, b)
elif choice == "d" or choice == "D":
    print("SUBTRACTION")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    div(a, b)
elif choice == "e" or choice == "E":
    print("programe ended")
    quit()
