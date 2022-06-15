#Take input from the user for the string they want to reverse
inp_string = input("Enter the string you want to reverse.\n")

length_str = len(inp_string)
#Declaring empty string to store the reversed string
reverse_str = ""

#Use for loop to traverse the string backwards and store it in new string
for count in range(length_str-1, -1, -1):
    reverse_str += inp_string[count]
    
#Print the output
print(reverse_str)