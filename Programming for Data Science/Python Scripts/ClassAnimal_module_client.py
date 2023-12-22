"ClassAnimal_module client - it uses the ClassAnimal module"

from ClassAnimal import Animal as An

print(__name__)
print(globals().keys())

# unit test block
if __name__ == '__main__':
	print("unit test block executed in class module animal client")

	#map(print
	Lion= An()
	Lion.shelter("Forest")
	print(f'the namespace of this instance object has at moment 1: {Lion.__dict__}')
	Lion.new_attribute1 = 1000
	Lion.tiger=200
	print(f'the namespace of this instance object has at moment 2: {Lion.__dict__}')
	Giraffe = An()
	print(f'the namespace of this instance object has at moment 1: {Giraffe.__dict__}')
	print(Lion.type('Omnivore','vertebrate'))
	print(Lion.kind('wild','mammal','warm'))
	print(An.shelter('Snake','Conservation Forest'))
	print(f'the namespace of the class object has at this moment: {An.__dict__.keys()}')



	print(An.__doc__)
	print(help(An))
	print(Lion.shelter.__doc__)
	print(help(Lion.shelter))
	
import ClassAnimal as ca
print(f'the namespace of the module containing the class: {ca.__dict__.keys()}')
	

	