# Elizabeth Fuller
# 11-13-19
# Test file for person class
from Person import Person

person1 = Person("Elizabeth", "Fuller", 19, "Liz")

print(person1.description())
person1.birthday()
person1.change_nickname("Eliza")
print(person1.description())
