
# Variables
a = 2
b = 3

# Print the variables to make it easier to read
print("a:", a, "b:", b, "\n")

# Below is an example of the "elif" keyword, using elif means that the whole structure is considered: The first conditional statement will that is met will execute 
#and the conditional structure will be exited
if a==b: 
    # If A and B are equal, say so
    print("A equals B is TRUE")
elif a!=b:
    # If A and B are not equal, say so
    print("A equals B is FALSE (A does not Equal B)")
elif a<b:
    # If A is less than B, say so
    print("A is less than B is TRUE")
elif a<=b:
    # If A is less than B or if A is equal to B, say so
    print("A is less than or equal to B is TRUE")
elif a>b:
    # If A is greater than B, say so
    print("A is greater than B is TRUE")
elif a>=b:
    # If A is greater than B or if A is equal to B, say so
    print("A is greater than or equal to B is TRUE")
else:
    print("Not sure how you got here but good job!")