print("Program prints all Numbers in a Range Divisible by a Given Number.")

"""Take the range by asking the user for two numbers
that will be the starting and end points for the range"""

start_range = int(input("Enter starting number of range\n"))
end_range = int(input("Enter ending number of range\n"))

#User enters the number for which they want to check divisibilty for
divisibe_number = int(input("Enter number for which you want to check divisibilty\n"))


#Use for loop to print numbers in a range divisible by given Number.

for number in range(start_range, end_range):
    if number % divisibe_number == 0:
        print(number)
