##export PYTHONPATH="<absolute path to your directory which contains the package>"

import sys

#replace the path with your own path to include the directory containing the packages
sys.path.append("/Users/sudeepmallick/Documents/BDA22-24/Python/Modules_Packages")

original_sys_path = sys.path
print(original_sys_path)

from mypackage1.mod2 import a,b,c,f1,f2,f3
print(a)

import module_to_import as m1
print(f'x and y from module_to_import {m1.x} and {m1.y}')

#trying to put the new package home to be inserted at a specific point in the search path
#- NOT ADVISABLE - better to append to sys.path as shown earlier

b = ['/Users/sudeepmallick/Documents/BDA22-24/Python/']
b.extend(sys.path[1:])
sys.path = b

print(sys.path,'\n')

#after the module search has been modified if we try loading the same module again
#the module is loaded after searching using the new search paths

from imp import reload
reload(m1)

print(f'x and y from module_to_import {m1.x} and {m1.y}')

sys.path = original_sys_path
reload(m1)

print(f'x and y from module_to_import {m1.x} and {m1.y}')

