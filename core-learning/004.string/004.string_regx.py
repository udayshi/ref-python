import re


'''
.   Matches any character 
*   0 or more times
+   1 or more times
\d  digit (Capital will be non digit)
\w  word (Capital will be non word)
\s  whitespace (Capital will be non whitespace)
\b  boundry (Capital will be non boundry)

'''
str='''
caT
mat
Mr. Uday
Mr Bijay
Mrs Sabita
Mrs. Sabi
Ms. Anu
Ms Arya
lol lollol

dat
this is test
this is test

'''





#Getting Name from string
regx=re.compile(r'(mr|ms|mrs)\.?\s+\w+',re.IGNORECASE)
for m in regx.finditer(str):
    print(m.group(0))



#Getting Name from string
regx=re.compile(r'\blol',re.IGNORECASE)
for m in regx.finditer(str):
    print(m.group(0))

#Getting Name from string
regx=re.compile(r'\Blol',re.IGNORECASE)
for m in regx.finditer(str):
    print(m.group(0))



regx=re.compile(r'.at')
for m in regx.findall(str):
    print(m) #mat dat


regx=re.compile(r'.at',re.I)
for m in regx.findall(str):
    print(m) #caT mat dat


regx=re.compile(r'[cm]at',re.I)
for m in regx.findall(str):
    print(m) #Cat mat

