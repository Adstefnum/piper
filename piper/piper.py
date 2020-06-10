#user goes to file directory in terminal
#then type piper which must be saved to path
import os
import re
#still picking up some user modules and that is causing it to have errors
#get if they want virtual env or not
pip_or_pipenv = input(
	"============================\nEnter v to create a virtulenv and install libs or press enter to install globally:")

print("gathering files...")
#get the path to files(current directory)
path = os.getcwd()

#get all files with .py(or others)
files = []
for r,d,f in os.walk(path):
	for file in f:
		if '.py' in file:
			files.append(os.path.join(r,file))
#open and read the files get the imported module but first process libs
print("parsing files...")
libs = []
for x in files:
	with open(x,'rt') as lines:
		for l in lines:
			#find import statements in each file
			if re.search('^import ',l) or re.search('^from',l):
				libs.append(l.strip())
#getting the libs
("getting libraries...")
pre_final_libs = []
for x in libs:
	if re.search('^import ',x):
		#taking care of case:import lib,lib,lib,lib
		if re.search(',', x):
			get = x.split(',')
			stuck = get[0].split(" ")[1]
			pre_final_libs.append(stuck)

			for t in get[1:]:
				pre_final_libs.append(t)

		#take care of import jfjfj.jfjfj
		elif re.search('.',x):
			get = x.split(" ")
			stuck = get[1].split(".")[0]
			pre_final_libs.append(stuck)

		else:
			get = x.split(" ")
			pre_final_libs.append(get[1])
	#take care of from lib.sublib import subsublib
	elif re.search(r'^from',x):
		if re.search('.',x):
			get = x.split(" ")
			stuck = get[1].split(".")[0]
			pre_final_libs.append(stuck)
	
		
#check if its a user defined module and remove it so you don't run pip on it
hit  = False
for l in pre_final_libs:
	for f in files:
		if re.search(l,f):
			hit = True
	if hit:
		pre_final_libs.remove(l)
final_libs = set(pre_final_libs)

#write them to a requirements.txt file
print("exporting libraries")
print(final_libs)
file = open("requirements.txt","a")
for lib in final_libs:
	file.write("\n"+lib)
file.close()
#run pip commnad on them
if pip_or_pipenv.lower() == 'v':
	print("sssssh pipenv is working...")
	os.system("pipenv install -r requirements.txt")
else:
	print("sssssh pip is working...")
	os.system("pip install -r requirements.txt")
