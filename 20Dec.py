# Basic for Loop and range() Usage
# 1. Write a program to print numbers from 1 to 10 using a for loop.
# for a in range(1,11):
#     print(a, end=" ")

# 2. Print numbers from 0 to 5 using range().
# for a in range
# 16. Print numbers from 1 to 20, skipping numbers whose sum of digits is even.
# for k in range(1,21):
#   s = sum(int(d) for d in str(k))
#   if s%2==0: continue
#   print(k, end=" ")

x=[1]
x.append(2)
x.insert(1,3)
x.extend(x)
x.remove(3)
print(x.index(2))
x.reverse()
print(x)
print(sum(x))
print(max(x))
print(min(x))
print(len(x))
