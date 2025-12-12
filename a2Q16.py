# 16. Count how many vowels are in the string: "Hello Python Programmer"
s="Hello Python Programmer"
vowel="aeiouAEIOU"
count=0
for j in s:
    if j in vowel:
        count+=1
print(f"Total vowels in string are {count}")