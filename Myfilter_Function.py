def myfilter(input):
    rng=[]
    for x in input:
        if x%2==0:
            rng.append(x)
    return rng

Set=range(20)
print(myfilter(Set))