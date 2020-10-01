import os

def isBinod(filename):
	with open(filename,'r') as f:
		filecontent = f.read()
		if 'binod' in filecontent.lower():
			return True
		else:
			return False	


dir_contents = os.listdir()

print(dir_contents)

nBinod = 0
totalcount = 0
for item in dir_contents:
	if item.endswith('txt'):
		print(f'Detecting Binod in {item}...')
		totalcount += 1
		flag = isBinod(item)

		if (flag):
			print('***************Binod found in ' + item)
			nBinod += 1
		else:
			print("***************Binod not found in " + item)	


print("Summary of files checked")
print(f"{totalcount} files checked ")
print(f'{nBinod} files found with word Binod')