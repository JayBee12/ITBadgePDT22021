
# Variables
a = 2
b = 3

# Print the variables to make it easier to read
print("a:", a, "b:", b, "\n")

# The code below evaluates A and B using various operators:
# == is used to test if the variables have the same value
# != is used to test if the variables DO NOT have the same value
# < is used to test if the variables on the left is less than the one on the right
# <= is used to test if the variables on the left is less than or equal to the one on the right
# > is used to test if the variables on the left is greater than the one on the right
# >= is used to test if the variables on the left is greater than or equal to the one on the right
#
# Once the evaluation has been made it results in either 'True' or 'False'
print(a==b)
print(a!=b, "\n")


# Below is an example of the if statement, in this configuration each 'if' is it's own conditional statement meaning each one that is met will be executed
# even if multiple conditions are met

# If A and B are equal, say so
if a==b: 
    print("A equals B is TRUE")

# If A and B are not equal, say so
if a!=b:
    print("A equals B is FALSE (A does not Equal B)")

# If A is less than B, say so
if a<b:
    print("A is less than B is TRUE")
 
 # If A is less than B or if A is equal to B, say so   
if a<=b:
    print("A is less than or equal to B is TRUE")

# If A is greater than B, say so
if a>b:
    print("A is greater than B is TRUE")

# If A is greater than B or if A is equal to B, say so
if a>=b:
    print("A is greater than or equal to B is TRUE")