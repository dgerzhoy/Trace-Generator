import random

f = open('./test.txt', 'w')

PAGE_SIZE=4096
TOTAL_PAGES=1048576
MEMORY_SIZE= PAGE_SIZE*TOTAL_PAGES

NUM_ACCESSES= 1000000

for i in range(NUM_ACCESSES):
	cycle = 10000*i #Cycle number 
	rw = random.randint(0,1) #Read/Write pattern
	address = 64*i #Change this line for different address pattern
#	address = 64*random.randint(0,MEMORY_SIZE)
	
	f.write(str(cycle))
	f.write(" ")
	f.write(str(rw))
	f.write(" ")
	f.write(str(address))
	f.write("\n")

f.close()
