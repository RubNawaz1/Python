def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(2)

print(mytripler(14))

x = lambda a, b : a - b
print(x(5, 3))


animals=[ "dog","goadssdsdt","Camel"]
print(animals)
animals.append("Monkey")

print(animals)

x = len("goadssdsdt")
print(x)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name,p1.age)
print(p1.age)