# Elizabeth Fuller
# 11/13/19
# Person Class file


class Person:
    def __init__(self, first, last, age, nickname):
        self.first = first
        self.last = last
        self.age = age
        self.nickname = nickname

    def description(self):
        return self.first + " " + self.last + " is " + str(self.age) + " and has the nickname " + self.nickname + "."

    def birthday(self):
        self.age = self.age + 1

    def change_nickname(self, new_nickname):
        self.nickname = new_nickname

