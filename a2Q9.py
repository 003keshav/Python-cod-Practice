# 9. Take 10 numbers from the user and print the highest number.
a1=int(input("Enter num1"))
a2=int(input("Enter num2"))
a3=int(input("Enter num3"))
a4=int(input("Enter num4"))
a5=int(input("Enter num5"))
a6=int(input("Enter num6"))
a7=int(input("Enter num7"))
a8=int(input("Enter num8"))
a9=int(input("Enter num9"))
a10=int(input("Enter num10"))
highest=a1
for k in [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]:
    if k > highest: highest = k
print("Highest Number is:",highest)
