# Program that converts €, $ and £ into one another
n = 1
while n:
	fr_curr = input("Choose the Input currency type(Euro(€), USD($), GBP(£) in text) :").upper()
	to_curr = input("Choose the Output currency type(Euro(€), USD($), GBP(£) in text) :").upper()
	value = int(input("Enter the value to convert in numbers:"))
	conv=0
	if (fr_curr=="EURO" and to_curr=="USD"):
		conv = value*1.15
	elif (fr_curr=="EURO" and to_curr=="GBP"):
		conv = value*0.885
	elif (fr_curr=="USD" and to_curr=="EURO"):
		conv = value*0.87
	elif(fr_curr=="USD" and to_curr=="GBP"):
		conv = value*0.77
	elif(fr_curr=="GBP" and to_curr=="EURO"):
		conv = value*1.13
	elif(fr_curr=="GBP" and to_curr=="USD"):
		conv = value*1.23
	elif(fr_curr==to_curr):
		print("\n\tEnter different Currency types")
	else:
		print("\n\tEnter Valid currency type - Euro, USD, GBP")

	if conv:
		print("\n\tThe converted amount is:",round(conv,2),to_curr)

	n = input("\nPress 1 and Enter to redo the calculation.")
