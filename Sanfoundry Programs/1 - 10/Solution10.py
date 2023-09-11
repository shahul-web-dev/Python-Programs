start = int(input("Enter a lower limit: "))
end = int(input("Enter a higher limit: "))

print("Numbers which are not divisible by 2 and 3")
for i in range(start, end + 1):
    if (i % 2 != 0) and (i % 3 != 0):
        print(i)
