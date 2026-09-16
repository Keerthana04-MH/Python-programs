n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
  
  Sample output
Enter the number of terms: 7
0
1
1
2
3
5
8
