
print("Lets add two numbers together.")

while True:
    num1 = input("Input a number: ")
    num2 = input("Input another number: ")
    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        print("INVALID INPUT - Try again")
        continue
    break
print(str(num1 + num2))
