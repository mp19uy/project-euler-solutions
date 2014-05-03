import time

def is_palindrom(number):
	return str(number) == str(number)[::-1] #reverse the string

tStart = time.time() # time counter, just for performace purposes
found = False
nr1 = 999
nr2 = 999
max_pal = 0

while nr2**2 >= max_pal:
	while not found and nr1**2 >= max_pal:
		candidato = nr1*nr2
		if is_palindrom(candidato):
			found = True
		else:
			nr1 = nr1 - 1
	if found and candidato > max_pal:
		max_pal = candidato

	nr2 = nr2 - 1
	nr1 = 999
	found = False

print("biggest palindrom = " + str(max_pal))
print ("run time = " + str((time.time() - tStart)))