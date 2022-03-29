class Parent(object):
	
	def override(self):
		print("PARENT OVERRIDE()")
		
class Child(Parent):
	
	def override(self):
		print("CHILD OVERRIDE()")
		
dad = Parent()
child = Child()

dad.override()
child.override()