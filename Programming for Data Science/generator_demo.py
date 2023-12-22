# generator expression similar to list comprehension
gen1 = (x**2 for x in range(10) if x % 2==0)

#generator objects support iterator protocol and can be used over for loop
for i in gen1:
	print(i)

print('\n')

#rebuild the generator object to again fetch from it
gen1 = (x**2 for x in range(10) if x % 2==0)


#fetch from the generator object using next until it is exhausted raising StopIteration exception
#below we are fetching just 3 times and not exhausting the limit which is 10 in this case
print(next(gen1))
print(next(gen1))
print(next(gen1))


#fetching safely inisde try-except block as the previous generator still not exhausted
try:
	for i in range(10):
		print(f'iteration = {i} gen output = {next(gen1)}')
except StopIteration:
	print('we have already exhausted the generator can fetch no further from it')

#converting the above generator expression to generator function
#define the generator function
def gen_func(x):
	for i in range(x):
		yield i**2

#create the generator object
gen2 = gen_func(5)

print(type(gen2),'\n')

#fetch from the generator object using iterator protocol
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))

l1 = list(range(10))
gen1 = (x**2 for x in l1)
gen2 = (x for x in gen1 if x%2==0)

#print(list(gen1))
print(list(gen2))

def all_steps(x):
	step1 = x**2
	return step1 if step1%2==0 else None

print(list(map(all_steps,l1)))

l1 = list(range(10))
l2 = [2,3]*5
print(f'l1={l1} l2={l2}')
genX = (x**y for x,y in zip(l1,l2))
print(list(genX))

		
	

