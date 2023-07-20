lst = [2,5,8,3,98,4,9]

a = b = lst[0]


for i in lst[1:]:
    if a<i:
        b = a;
        a = i;
        continue;
    if b<i:
        b = i;
print("Second max is", b)
