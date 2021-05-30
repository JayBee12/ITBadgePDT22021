# While loops run until a certain condition is True or False:

# This loop will never run because 1 will never equal 2
while(1==2):
    print("this loop will never run")
    
# This loop will run forever (or at least until you stop the program or it crashes) because True will never be False
#while(True!=False):
#   print("oops")


# This loop will run until the user types the word stop (and only the word stop)
# Note the .lower() function means that any string input will be made lowercase so that it matches what we're expected rgardless of capitalisation
stop = "go"

while(stop.lower() != "stop"):
    print("Should I stop?")
    stop = input()