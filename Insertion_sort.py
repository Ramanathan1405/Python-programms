#Ramanathan Moorthy - 18201670
#Insertion Sort Function
def Insertion_sort(int_lst):
    for i in range (1, len(int_lst)):
   		key = int_lst[i]
   		j=i-1
   		while j>=0 and key < int_lst[j]:
   			int_lst[j+1] = int_lst[j]
   			j -= 1
   		int_lst[j+1] = key
    #Print Sorted List
    print("Sorted List\n", int_list)

    #Write Sorted List into a New File
    file2 = open("sorted_integers.txt", "w")
    for x in range(len(int_list)):
        file2.write(str(int_list[x])+"\n")
    file2.close()
    print("Sorted list is successfully printed into a new file \"sorted_integers.txt\"")
    input()


# Main Program
file1 = open("integers.txt", "r")
list1 = file1.read().splitlines()
file1.close()
int_list = []
for x in range(len(list1)):
      int_list.append(int(list1[x]))

Insertion_sort(int_list)





