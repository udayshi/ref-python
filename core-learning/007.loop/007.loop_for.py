a=[1,2]
for i in a:
    print(i) #1 2

a=[1,2]
for k,v in enumerate(a):
    print(k,v) #0 1 - 0 2

a=['uday','bijay']
for k,v in enumerate(a,start=1):
    print(k,v) #1 uday - 2 bijay


for i in range(2):
    print(i) #0 1

for i in range(2,4):
    print(i) #2 3

a={'name':'uday','age':'40'}
for i in a:
    print(i) #name age

a={'name':'uday','age':'40'}
for i in a.keys():
    print(i) #name age


a={'name':'uday','age':'40'}
for i in a.values():
    print(i) #uday 40

a=['name','age']
b=['uday','40']
for k,v in zip(a,b):
    print(k+' '+v) #name uday - age 40
