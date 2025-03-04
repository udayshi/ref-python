info=[{"name":"uday","age":40,'loc':'NP'},
      {"name":"Bijay","age":38,'loc':'NP'}
     ]
sorted_by_name=sorted(info,key=lambda k:k['name'])
sorted_by_age=sorted(info,key=lambda k:k['age'],reverse=True)

print(sorted_by_name)

