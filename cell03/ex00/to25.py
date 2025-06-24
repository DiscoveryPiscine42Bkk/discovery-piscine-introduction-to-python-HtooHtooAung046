i = int(input("Enter a number less than 25 : "))
if i > 25:
    print("Error")
else:
    print(i)
    for i in range(i,26):
        print("Inside the loop, my variable is",i)