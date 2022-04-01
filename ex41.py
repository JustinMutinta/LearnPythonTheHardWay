from unicodedata import name


class Person(object):

    name = "Tim"
    age = 23

    def sound(self):
        print("I'm a person.")

class Child(Person):
    dream = "Race car driver"
    def hope(self):
        print("I'm the child class")


tim = Person()
tim.sound()
