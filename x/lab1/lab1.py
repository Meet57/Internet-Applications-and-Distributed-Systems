#dictionary literals
d1={"name": "Bob", "age": 35, (4, 10):['x', 'y', 'z'], '+1' : "Canada",  44: 99, 19:555} 

#dictionary using sequences
d2 = dict([("name","Livy"), ('age', 44), ((1, 3, 5), ['a', 'b', 'c']), (0, 'black'), (33, 67)]) 

#dictionary using keywords
d3 = dict(id=2277, name='Michael', siblings=['Janet', 'Martin', 'Richard'])  

d1.keys()
d2.values()
d3.get('id') 
d2.get('age') 
d3.get('age')
d3.get('name','Tim')
d2.items()
d3['siblings']
d2['siblings'] 
d2.update(d3)
d2[0]
d1.get((1,2))
d2['siblings']
d2['name']
d1 == d2
len(d2)

for key in d1.keys(): 
    print(key)



list1 = ["apple", 10, 3.14, [1, 2, 3], "class", 20, [4.5, 6.7], 5.5]
list2 = [8, "list in python", [9.1, 7.2], 15, "MAC", [2, 4, 6], 3.33, 12.5]

list1.append("university")

del list2[-1]
list1[5] = 100
list1
list2 += [44,50]
list2

