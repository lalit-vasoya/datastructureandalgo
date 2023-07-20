lst = [8,2,5,7,6,9,0,11]

a = b = c = lst[0]
for i in lst[0:]:
    if a<i:
        c = b
        b = a
        a = i
        continue
    elif b<i:
        c = b
        b = i
        continue
    elif c<i:
        c=i
        continue

print("Three max number is: {} {} {}".format(a,b,c))
