# 3. run loop 60-170 & get total of all nums along with the total of nums divisible by 9
sum=0
total=0
for a in range(60,171):
    total+=a
    if a%9==0:
        sum+=a
print(f"Total of all numbers is {total} and Sum of all numbers divisible by 9 is {sum}")