# 11. Print the sum of all numbers from 1–100 but skip numbers divisible by 3.
sum=0
for j in range(1,101):
    if j%3==0:
        continue
    sum+=j
print(sum)