# 8. From numbers 1 to 20, skip odd numbers and print only squares of even numbers.
for l in range(1,21):
    square=l*l
    if l%2!=0: continue
    else: print(square)