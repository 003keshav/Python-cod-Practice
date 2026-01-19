# s={"total":0}
# a="Rajasthan"
# for k in range(len(a)):
#     s["total"]=s["total"]+1
# print(s)

# s={}
# for k in "riyar":
#     if k not in s:
#        s[k]=1
#     else:
#        s[k]+=1
# print(s)


# vow={}
# s="My Name is Riya Singh"
# for k in s:
#     if k in "a,e,i,o,u,A,E,I,O,U":
#       if k not in vow:
#         vow[k]=1
#       else:
#         vow[k]+=1
# print(vow)







# a
# ab
# abc
# abcd

# b
# bc
# bcd

# c
# cd

# d
a="abcab"
s={}
for k in range(0,len(a)):
    b=""
    for l in range(k,len(a)):
      b=b+a[l]
      print(b)
    for i in b:
       if b not in i:
          s[i]=1
       else:
          s[i]+=1
    print("")
print(s)