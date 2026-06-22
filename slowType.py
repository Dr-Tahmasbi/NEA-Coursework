import time
#------------------------------------------------------------------------------------------------------------------
#Slow Text Output Maker
def slowType(text, speed, newLine = True): # Function used to print text a little more fancier
    for i in text: # Loop over the message
        print(i, end = "", flush = True) # Print the one charecter, flush is used to force python to print the char
        time.sleep(speed) # Sleep a little before the next one
    if newLine: # Check if the newLine argument is set to True
        print() # Print a final newline to make it act more like a normal print statement