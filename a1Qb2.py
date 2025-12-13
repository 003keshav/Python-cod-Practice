# 2. Count the number of vowels in a given string using a loop.
s='vowels in a string'
vowels='aeiouAEIOU'
count=0
for j in s:
    if j in vowels: count+=1
print("Total number of vowels in string are:",count)