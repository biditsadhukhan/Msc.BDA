"simpleclass_module client - it uses the simpleclass_module"

from simpleclass_module import SimpleClass as SC

print(__name__)
print(globals().keys())

# unit test block
if __name__ == '__main__':

	#map(print
	sc1 = SC()
	sc1.method1()
	print(f'the namespace of this instance object has at moment 1: {sc1.__dict__}')
	sc1.new_attribute1 = 1000
	print(f'the namespace of this instance object has at moment 2: {sc1.__dict__}')
	sc2 = SC()
	print(f'the namespace of this instance object has at moment 1: {sc2.__dict__}')
	print(sc1.method2(10))
	print(sc1.method3())
	print(SC.method3('abc'))
	print(f'the namespace of the class object has at this moment: {SC.__dict__.keys()}')

	import simpleclass_module as scm
	print(f'the namespace of the module containing the class: {scm.__dict__.keys()}')

	print(SC.__doc__)
	print(help(SC))
	print(sc1.method1.__doc__)
	print(help(sc1.method1))
	
	