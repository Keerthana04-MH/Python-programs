n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits =", sum)

Sample output 
Enter a number: 12345
Sum of digits = 15
