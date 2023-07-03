print("Enter the number of integers (N):")
n = int(input())
counter = 0
print("Enter whole numbers")
for i in range(n):
    a = int(input())
    if (a == 0):
        counter += 1
print("Number of entered numbers equal to zero:", counter)
