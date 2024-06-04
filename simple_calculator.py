
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Simple calculator~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
number1=float(input
              ("Enter the first number here:  "))
number2=float(input
              ("Enter the second number here:  "))

print("Press 1 for addition \npress 2 for subtraction\npress 3 for multiplicition\npress 4 for divisoin")
choice = int(input
             ("Enter the choice from 1-4: "))


if choice == 1:
    print(number1+number2)
elif choice  == 2:
    print(number1-number2)
elif choice == 3:
    print(number1*number2)
elif choice == 4:
    print(number1/number2)

else:
    print("invalid input")