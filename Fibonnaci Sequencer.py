'''
Ye Bo Gong
This program calculates the Fibbonaci sequence up to a user given value.
'''
#printing the title
print("Project one (01) - Part A : Fibbonaci Sequence ")
#asking user for the sequence ending at value
#Variable will be used to determine when the sequence ends
sequence_end = int(input("Sequence ends at: "))

#Setting the first x_1 and x_2 values
#x_1 value is the first number in the fibbonaci sequence
x_1 = 0
#x_2 value is the second number in the fibbonaci sequence
x_2 = 1

#Sequence_count is used to
sequence_count = 0
while sequence_count <= sequence_end:
    #value formatted by commas
    x_1_formated = ('{:,}'.format(x_1))
    #print the sequence counter, raw value and formatted value
    print(str(sequence_count) + ": " + str(x_1) +" " + str(x_1_formated))

    #Fib sequence equation
    # x_3 is equal to x_1 + x_2
    x_3 = x_1 + x_2
    #move every value to the next
    #set x_1 to x_2
    x_1 = x_2
    #set x_2 to x_3
    x_2 = x_3
    #set x_3 to x_1
    x_3 = x_1
    #sequence_counter + 1 to count to the value of sequence_end
    sequence_count = sequence_count + 1








