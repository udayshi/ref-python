info={'uday',40}
info.add('bijay')

'bijay' in info #True

c=set()
c.add('uday')#{'uday'}
c.add('world') #{'uday','world'}
c.add('world') #{'uday','world'}
c.remove('uday')#{'world'}
c.add('ram') #{'world','ram'}
