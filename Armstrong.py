n = int(input("Enter a number: "))

original = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10

if original == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

Sample output 
Enter a number: 153
Armstrong Number
