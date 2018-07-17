lst= 'ACADGILD'
A=[i for i in lst]
print(A)

'''
Out--> ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
'''

Str= 'xyz'
B=[Str[x]*y for x in range(len(Str)) for y in list(range(1,5,1))]
print(B)

'''
Out--> ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
'''

Str1= 'xyz'
B=[Str1[x]*y for y in list(range(1,5,1)) for x in range(len(Str1))]
print(B)

'''
Out--> ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
'''

input=[2,3,4]
Output=[[num+itr] for num in input for itr in range(0,3)]
print(Output)

'''
Out--> [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
'''

inp=[2,3,4,5]
Out=[[num1+itr1 for num1 in inp] for itr1 in range(0,5)]
print(Out)

'''
Out--> [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
'''

set=[1,2,3]
comb=[(a,b) for a in set for b in set]
print(comb)

'''
Out--> [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
'''