# 15. Print the smallest number in a list.
l=[223,6,9,4,6,35,543,42]
lowest=l[0]
for i in l:
    if i < lowest:
        lowest = i
print(lowest)