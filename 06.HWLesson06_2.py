print("Enter a natural number from 1 to 2 billion:")
n = int(input())
if n > 2000000000:
    print ("You have entered a number that is outside the conditions of the problem")
else:
    count = 2
    if n < 1:
        print("The number 0 is not natural. Try natural number from 1 to 2 billion")
    elif n == 1:
        count = 1
    else:
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                count += 1
        print("Number of natural divisors of a number", n, "is:", count)
