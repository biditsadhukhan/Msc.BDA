"this is my module to demonstrate the simplest of classes!!"

A_CONSTANT = 10

def func1():
	"a function in the module"

	return "i am a function not a method of a class!!"

class SimpleClass:
	"this is a class to demonstrate the basic concepts of a class and its relationship to namespaces"

	classAttribute1 = 10   #class attribute
	
	def method1(self):
		"instance method with no params and no returned value"

		print(f"this is an instance method of {self.__class__.__name__}")

	def method2(self, real_param1):
		'''
		instance method with single param and a return value
	
		return value: a concatenated string derived from input parameter
		'''
		return "hello " + str(real_param1)

	def method3(self):
		'''
		this is sort of a class method as called directly through class object
		'''
		return 'Hallo ' + str(self)