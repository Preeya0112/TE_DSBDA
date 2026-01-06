Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Helo")
Helo
>>> fruits=["Apple","Mango"]
>>> print(fruits)
['Apple', 'Mango']
>>> fruits.append("orange")
>>> print(fruits)
['Apple', 'Mango', 'orange']
>>> fruits.insert(1,"banana")
>>> print(fruits)
['Apple', 'banana', 'Mango', 'orange']
>>> fruits.pop(0)
'Apple'
>>> print(fruits)
['banana', 'Mango', 'orange']
>>> fruits.reverse()
>>> print(fruits)
['orange', 'Mango', 'banana']
>>> fruits.sort()
>>> print(fruits)
['Mango', 'banana', 'orange']
>>> fruits.copy()
['Mango', 'banana', 'orange']
>>> fruits.count("banana")
1
>>> fruits.extend("banana")
>>> print(fruits)
['Mango', 'banana', 'orange', 'b', 'a', 'n', 'a', 'n', 'a']
>>> print.index(fruits["banana"])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print.index(fruits["banana"])
AttributeError: 'builtin_function_or_method' object has no attribute 'index'
>>> print(fruits.index["banana"])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(fruits.index["banana"])
TypeError: 'builtin_function_or_method' object is not subscriptable
print(fruits.index("banana"))
1
fruits.remove("banana")
print(fruits)
['Mango', 'orange', 'b', 'a', 'n', 'a', 'n', 'a']
fruits.clear()
print(fruits)
[]
x=[1,2,3,4,5]
print(x)
[1, 2, 3, 4, 5]
print(x[2])
3
for a in x:
    print(a)

    
1
2
3
4
5
x*5
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
x.insert(2,7)
print(x)
[1, 2, 7, 3, 4, 5]
x.remove(4)
print(x)
[1, 2, 7, 3, 5]
