"This is a module which contains class of animal"

class Animal:
	"This is a class of animal which contains two attributes and three class methods with 1,2,3 parameters excluding self"
	tiger=10    # class attribute 
	chimpanzee=4   #class attribute

	def shelter(self,place):
		''' Prints the class of animal and the shelter it lives in'''
		print(f"This {self.__class__.__name__} lives in {place}" ) 


	def type(self,eater,vertebrate):
		''' Gives the animal along with the kind of eater the animal is omnivore, carnivore or herbivore along with if it is a vertebrate or invertebrate'''
		print(f" This {self.__class__.__name__} is a {eater} and it is {vertebrate}" )

	def kind(self,pet_nature,animal_class,blood_w_or_c):
		'''Gives the animal along with the kind of animal it is domestic or wild, class in which the animal belongs to as well as the blood type warm or cold blooded'''
		print(f" This {self.__class__.__name__} is {pet_nature} , it belongs to {animal_class} and it is {blood_w_or_c}" )

# unit test block
if __name__ == '__main__':
	print("unit test block executed in class module animal")

	#map(print
	Lion= Animal()
	Lion.shelter("Forest")
	print(f'the namespace of this instance object has at moment 1: {Lion.__dict__}')
	Lion.new_attribute1 = 1000
	Lion.tiger=200
	print(f'the namespace of this instance object has at moment 2: {Lion.__dict__}')
	Giraffe = Animal()
	print(f'the namespace of this instance object has at moment 1: {Giraffe.__dict__}')
	print(Lion.type('Omnivore','vertebrate'))
	print(Lion.kind('wild','mammal','warm'))
	print(f'the namespace of the class object has at this moment: {Animal.__dict__.keys()}')
	
	print(Animal.__doc__)
	print(help(Animal))
	print(Lion.shelter.__doc__)
	print(help(Lion.shelter))
	
