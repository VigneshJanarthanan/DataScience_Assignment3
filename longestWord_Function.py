from functools import reduce
def longestWord(inp):
    return reduce(lambda x,y: y if len(y) > len(x) else x, inp)
    
inp=['ACADGILD','MACHINELEARNING','DATASCIENCE','PYTHON','NUMPY']
print("longest word is " +longestWord(inp))