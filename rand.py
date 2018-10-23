import random
count = 0
t = int(input("enter count"))
tail = 0
while count < t :
	m = random.randint(0,1)
	while m:
		tail += 1	
		count +=0

print(100*tail/t)
input()