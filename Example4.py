# We use def to define the structure of a function, functions can be created to expect 'arguments' which are data we provide to the function to do something with
# The examples below are 'pass by value' arguments in that the value is passed to the function rather than a reference or pointer to the variable itself

#This function has no arguments and simply calls the print funtion to print some text to the console
def noArguments():
    print("The function with no arguments was called")


#This function takes two variables adds them together and then prints them using the print function 
def hasArguments(a, b):
    print(a + b)
    
# This function has a return value meaning that when the function is called it will 'return' whatever is specified,  in this case it returns the sum of the
# values of the two variables passed to it
def hasReturns(a, b):
    return a + b

#function call
noArguments()


# Function call with arguments
hasArguments(6, 4)

# What do think this function will do
# hasArguments()

# Function wtih return to variable
x = hasReturns(3, 3)

# Print returned data in variable
print(x)

# Print return value directly
print(hasReturns(7, 7))
