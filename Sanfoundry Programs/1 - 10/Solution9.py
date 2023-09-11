givenNumber = int(input("Enter a number: "))

duplicateNumber = givenNumber

reversedNumber = 0

while duplicateNumber > 0:
    reversedNumber = reversedNumber * 10 + (duplicateNumber % 10)
    duplicateNumber /= 10

print("Reverse format of Entered Number is", reversedNumber)
