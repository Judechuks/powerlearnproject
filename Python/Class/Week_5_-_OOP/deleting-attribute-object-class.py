"""
Deleting Attribute, Object, Class
You can delete attributes, objects, or the class itself, using the del keyword, as shown below.

#deleting attribute
>>> std = Person('Mutemi', 65)
>>> del std.name # deleting attribute
>>> std.name
Traceback (most recent call last):
File "<pyshell#32>", line 1, in <module>
std.name
AttributeError: 'Person' object has no attribute 'name'

#deleting object
>>> del std  # deleting object
>>> std.name  
Traceback (most recent call last):
File "<pyshell#32>", line 1, in <module>
std.name
NameError: name 'std' is not defined

#deleting class
>>> del Person  # deleting class
>>> std = Person('Mutemi', 65)
Traceback (most recent call last):
File "<pyshell#32>", line 1, in <module>
std = Person()
NameError: name 'Person' is not defined

"""
