class Parent(object):
	
	def altered(self):
		print("PARENT altered()")
		
class Child(Parent):
	
	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")
		
dad = Parent()
child = Child()

dad.altered()
child.altered()