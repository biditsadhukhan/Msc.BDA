import sys
cl1=0; cl2=0; cl3=0
try:
	cl1 = sys.argv[1]
	cl2 = sys.argv[2]
	print(f'cl1 = {cl1} cl2 = {cl2}')
	cl3 = sys.argv[3]
except IndexError:
	print('you need to supply 3 command line arguments for this portion of code to work!')

print(f'outside exception handling block: cl1 = {cl1} cl2 = {cl2} cl3 = {cl3}')

def f1(w,x,y=2,z=3):
	return pow((w+x)*10,y)*z

def f2(v,w,x,y=1,z=2):
	return pow(v+w+x,y*z)


fl = [f1,f2]

def f3(f,*args,**kwargs):
	if len(args)==2:
		return f[0](*args,**kwargs)
	else:
		return f[1](*args,**kwargs)

print(f3(fl,2,3))
print(f3(fl,2,3,4))
print(f3(fl,2,3,y=1,z=1))
print(f3(fl,2,3,4,z=3))