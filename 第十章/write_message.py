filename='programing.txt'

with open(filename,'a')as file_object:
	name=input("please enter your name:")
	while(name!=' '):
		file_object.write(name+'\n')
		name=input("please enter your name:")