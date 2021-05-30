# For loops using the range() function are fairly simple:
# we use a variable to keep an index (a measure of which number we're up to) in this case we use 'i'
# we then use the range() function to create a list of steps to use the index to measure against.
# we can give range 3 numbers: a start number, a stop number, and how many numbers we want to step through:

# NOTE: Unless we tell it to, the computer will start counting at 0 meaning that 10 steps is actually the numbers 0-9

# in this example the range() function is only being provided the stop number, so it assumes we want to start at 0 and finish on the 10th number (9)
for i in range(10):
    print(i)

print("\n")
#in this example the range() function starts at 1 and finishes at the 20th number (19) counting every second number
for i in range(1, 20, 2):
    print(i)
    
print("\n")
    
#What does this loop do?
#for i in range(10, 0, -1):
#    print(i)