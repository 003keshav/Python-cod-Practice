# 4. Take a number from the user and print its multiplication table (1–10).
num=int(input("Enter number:"))
for i in range(1,11): 
    print(f"{num} X {i} = {num*i}")