start = int(input("Enter a lower limit: "))
end = int(input("Enter a higher limit: "))

print("Odd numbers from", start, "to", end)
for i in range(start, end + 1):
    if i % 2 == 1:
        print(i)
