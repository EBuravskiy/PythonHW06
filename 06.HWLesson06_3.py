print ("Enter integer numbers for the beginning and end of the segment with the condition that the initial number is greater than the final one")
print("Enter the first integer of the segment:")
a = int(input())
print("Enter the second integer of the segment:")
b = int(input())
if a > b:
    print("You have entered a second number greater than the first. This does not meet the requirements. Try again.")
else: 
    print("Introduced segment from", a, "to", b)
    s = ''
    while a <= b:
        if a % 2 == 0:
            s = s + str(a) + ' '
        a += 1
    print ("Even numbers of introduced segment:")
    print (s)
