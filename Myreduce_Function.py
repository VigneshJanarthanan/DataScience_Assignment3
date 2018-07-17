def myreduce(i):
    Total=0
    for x in i:
        Total += x
    return Total

lst=[47,11,42,13]
print(myreduce(lst))