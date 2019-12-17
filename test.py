t=[
    {
        'name':'chirchi',
        'age':'20'
    },
    {
        'name':'mrt',
        'age':'19'
    }
]
for i in t:
   if i['name']=='chirchi':
       t.remove(i)
print(t)