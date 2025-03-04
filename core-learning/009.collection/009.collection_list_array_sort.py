info=['uday','bijay','sanjay']
info.sort(reverse=False)
print(info)#['bijay', 'sanjay', 'uday']

#Sort based on length
info.sort(key=lambda k:len(k))
print(info) #['uday', 'bijay', 'sanjay']