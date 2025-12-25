# 3. run loop 60-170 & get total of all nums along with the total of nums divisible by 9
# sum=0
# total=0
# for a in range(60,171):
#     total+=a
#     if a%9==0:
#         sum+=a
# print(f"Total of all numbers is {total} and Sum of all numbers divisible by 9 is {sum}")


# x=0
# i=1
# while x<3:
#     if i%9==0 or i%2==0 or i%10243==0:
#         x+=1
#         print("Divided by 9 , 2, 10243",i,x)
#     i+=1




count=0
i=450
while count<5:
    if i%7==0 and i%9==0:
        count+=1
        print(i)
    i-=1