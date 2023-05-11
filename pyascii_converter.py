
while True:
	a = input("enter sentace ")
	pyascii = ''
	for i in a:
		pyascii += '{' f"chr({ord(i)})" + '}'
	print(pyascii)
	with open("temp.txt",'w') as file:
		file.write(pyascii)
	print()
