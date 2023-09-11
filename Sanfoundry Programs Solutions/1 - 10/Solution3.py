isEven = lambda num: 1 if num % 2 == 0 else 0

givenNumber = int(input("Enter a number: "))
if isEven(givenNumber):
    print("Entered number is Even")
else:
    print("Entered number is  Odd")
