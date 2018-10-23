# Program to Sum square numbers within N
y=1
while y:
	n= int(input("Enter an Integer N to compute Sum of Even Square numbers till N: "))
	sum = 0
	if n>0:
		for i in range(2, n+1):
			if (i%2 == 0):
				sum = sum + i;
	if n<0:
		for i in range(n-1, 0):
			if (i%2 == 0):
				sum = sum + i;
	
	print("\n\tSum of Squared Even Numbers till", n, "(inclusive) is:", sum)
	print("\nEnter 1 to give new input or Simply hit 'Enter' to exit")
	y=input()
