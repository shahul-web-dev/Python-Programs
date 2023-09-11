def isEven(num):
    if num < 2:
        return (num % 2) == 0
    return isEven(num - 2)


givenNumber = int(input("Enter a number: "))


if isEven(givenNumber):
    print("Entered number is Even")
else:
    print("Entered number is Odd")
