class Student:
  def __init__(self, name, age):
    print("adding new Student")
    self.name = name
    self.age = age

student1 = Student("Muhammed", 36)

print(student1.name)
print(student1.age)

student2 = Student("Ali", 39)
print(student2.name)
print(student2.age)


student3 = Student("Ahmed", 19)
print(student3.name)
print(student3.age)