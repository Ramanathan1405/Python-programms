# Ramanathan Moorthy(18201670)
# Palindrome Function

def palindrome(string):
    str_lower = string.lower()
    crc_str = ""
    crc_str = crc_str.join(x for x in str_lower if x.isalnum())
    
    n= int(len(crc_str)/2) + 1
    if n==1:
        return
    for i in range(0, n):
        if crc_str[i] != crc_str[-(i+1)]:
            print("\t\"" + string + "\" is NOT a Palindrome")
            return
    print("\t\"" + string + "\" is a Palindrome")

#Main Program

con = 1
while con:

    inp = input("Enter the Word or Phrase to check for Palindrome : ")
        #Try phrases like "A Man, A Plan, A Canal-Panama!"
        #"Madam In Eden, I’m Adam"
        
    palindrome(inp)

    con = input("""
Simply hit ENTER to exit
Hit 1 and Enter to check for another input
                """)


        
            
