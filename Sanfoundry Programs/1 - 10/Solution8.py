givenNumber = int(input("Enter a number: "))

duplicateNumber = givenNumber

reversedNumber = 0

while duplicateNumber > 0:
    reversedNumber = reversedNumber * 10 + (duplicateNumber % 10)
    duplicateNumber /= 10

if reversedNumber == duplicateNumber:
    print("Entered number is Palindrome")

else:
    print("Entered number is not a Palindrome")
