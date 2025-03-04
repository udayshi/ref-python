import requests,json
#requests.get('https://jsonplaceholder.typicode.com/users', auth=('user', 'pass'))

url='https://jsonplaceholder.typicode.com/users'
r=requests.get(url)
#r.status_code
#r.headers['content-type']
#print(r.headers['content-type'])
#json_py_obj=json.loads(r.content)
#print(json_py_obj)
print(r.json()[0])
