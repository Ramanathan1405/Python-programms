import random
count = 0
t = int(input("enter count"))
tail = 0
while count < t :
        m = random.randint(0,1)
        count = count+1
        if m:
                tail= tail+1
print(tail)
